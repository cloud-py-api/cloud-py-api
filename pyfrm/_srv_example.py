import sys
import os
import re
from subprocess import PIPE, Popen, TimeoutExpired
from concurrent import futures
from pathlib import Path

import grpc
from core_pb2 import taskStatus, logLvl, Empty, \
    TaskInitReply, fsId, FsNodeInfo, FsListReply
import core_pb2_grpc as core_pb2_grpc


def run_python_script(python_script_path, *args):
    fd = os.open('./../tmp/errors.log', os.O_WRONLY + os.O_CREAT + os.O_TRUNC)
    process = Popen([sys.executable, python_script_path, *args],
                    bufsize=0, stdin=PIPE, stdout=PIPE, stderr=fd, text=False)
    os.close(fd)
    return process


class TaskParameters:
    def __init__(self, log_lvl, data_folder, frm_app_data, user_id, use_file_direct, use_db_direct,
                 app_name, mod_name, mod_path, func_name, args):
        self.app_name = app_name
        self.mod_name = mod_name
        self.mod_path = mod_path
        self.func_name = func_name
        self.args = args
        self.log_lvl = log_lvl
        self.data_folder = data_folder
        self.frm_app_data = frm_app_data
        self.user_id = user_id
        self.use_file_direct = use_file_direct
        self.use_db_direct = use_db_direct


class ServerCloudPA(core_pb2_grpc.CloudPyApiCoreServicer, TaskParameters):
    connection_alive: bool = False
    task_status: taskStatus = taskStatus.ST_UNKNOWN
    task_error: str = ''
    result: str
    logs_storage: list = []
    _fs_emulation = {}

    def TaskInit(self, request, context):
        self.connection_alive = True
        _reply = TaskInitReply(appName=self.app_name,
                               modName=self.mod_name,
                               modPath=self.mod_path,
                               funcName=self.func_name,
                               config=TaskInitReply.cfgOptions(
                                   log_lvl=self.log_lvl,
                                   dataFolder=self.data_folder,
                                   frameworkAppData=self.frm_app_data,
                                   userId=self.user_id,
                                   useFileDirect=self.use_file_direct,
                                   useDBDirect=self.use_db_direct))
        if self.args is not None:
            if isinstance(self.args, (list, tuple)):
                for _each_arg in self.args:
                    _reply.args.append(_each_arg)
            elif isinstance(self.args, str):
                _reply.args.append(self.args)
            else:
                raise TypeError('Only str, tuple of str and list of str types are supported.')
        return _reply

    def TaskStatus(self, request, context):
        if self.task_status != request.st_code:
            print(f'Server: pyfrm status changed from '
                  f'{taskStatus.Name(self.task_status)} to {taskStatus.Name(request.st_code)}')
        if self.task_error != request.error:
            print(f'Server: pyfrm error changed from `{self.task_error}` to `{request.error}`')
        self.task_status = request.st_code
        self.task_error = request.error
        return Empty()

    def TaskLog(self, request, context):
        mod_name = request.module if len(request.module) else 'Unknown'
        for record in request.content:
            print(f'Client: {mod_name} : {logLvl.Name(request.log_lvl)} : {record}')
            self.logs_storage.append(f'{mod_name}:{record}')
        return Empty()

    def TaskExit(self, request, context):
        self.result = request.result
        print('Server: receive TaskExit')
        print(f'Server: result length = {len(self.result)}, result: {self.result}')
        self.connection_alive = False
        return Empty()

    def __fs_add_file(self, obj_path) -> int:
        _new_id = 1 + self._fs_emulation.get('l_id', 0)
        self._fs_emulation['l_id'] = _new_id
        self._fs_emulation[_new_id] = obj_path
        return _new_id

    def __fs_emulate_list_handler(self, obj_path, file_id):
        if self.__fs_get_path_by_id(file_id):
            return file_id
        return self.__fs_add_file(obj_path)

    def __fs_entry_to_node(self, obj_path, file_id) -> FsNodeInfo:
        _fs_id = fsId(userId=self.user_id, fileId=file_id)
        _target = Path(obj_path)
        _target_stat = _target.stat()
        return FsNodeInfo(fileId=_fs_id, is_dir=_target.is_dir(), is_local=True,
                          name=_target.name, internal_path=os.path.relpath(_target),
                          abs_path=str(_target.resolve()),
                          mtime=_target_stat.st_mtime_ns,
                          size=0 if _target.is_dir() else _target_stat.st_size)

    def __fs_get_path_by_id(self, file_id) -> str:
        _path = self._fs_emulation.get(file_id, '')
        return _path

    def FsList(self, request, context):
        # This is not a real function, just stuff for development testing.
        print(f'Server: client requested list files of: userId={request.dirId.userId}, fileId={request.dirId.fileId}')
        if not request.dirId.fileId:
            _target_path = self.data_folder         # in production this must be root folder of User.
        else:
            _target_path = self.__fs_get_path_by_id(request.dirId.fileId)
            if not _target_path:
                return FsListReply()
        _nodes = []
        with os.scandir(_target_path) as _target_obj:
            for entry in _target_obj:
                _file_id = self.__fs_emulate_list_handler(os.path.abspath(entry.path), request.dirId.fileId)
                _nodes.append(self.__fs_entry_to_node(os.path.abspath(entry.path), _file_id))
        return FsListReply(nodes=_nodes)

    def FsGetInfo(self, request, context):
        # This is not a real function, just stuff for development testing.
        print(f'Server: request file info for: userId={request.fileId.userId}, fileId={request.fileId.fileId}')
        _path = self.__fs_get_path_by_id(request.fileId.fileId)
        if _path:
            return FsListReply(nodes=[self.__fs_entry_to_node(os.path.abspath(_path), request.fileId.fileId)])
        return FsListReply()


def srv_example(address, port, app_name, module_name, module_path, function_to_call, args=None):
    print('')
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=2))
    servicer = ServerCloudPA(log_lvl=logLvl.DEBUG,
                             data_folder='./../tmp/data_folder',
                             frm_app_data='./../tmp/frm_app_data',
                             user_id='user_name',
                             use_file_direct=False,
                             use_db_direct=False,
                             app_name=app_name,
                             mod_name=module_name,
                             mod_path=module_path,
                             func_name=function_to_call,
                             args=args
                             )
    core_pb2_grpc.add_CloudPyApiCoreServicer_to_server(servicer, server)
    connect_address = address
    if not address.startswith('unix:'):
        if not port:
            port = '0'
        listen_port = server.add_insecure_port(f'{address}:{port}')
        connect_address += ':' + str(listen_port)
    else:
        server.add_insecure_port(address)
    print(f'Server: connect address = {connect_address}')
    p_obj = run_python_script('pyfrm.py', connect_address)
    server.start()
    if server.wait_for_termination(timeout=5.0):
        if servicer.connection_alive:
            while True:
                if not server.wait_for_termination(timeout=0.5):
                    break
                if not servicer.connection_alive:
                    break
        elif servicer.task_status == taskStatus.ST_UNKNOWN:
            print('Server: timeout, client did not connected')
    server.stop(grace=0.5)
    try:
        p_obj.wait(timeout=3.0)
    except TimeoutExpired:
        print('Server: timeout waiting child process')
    print(f'Server: task finished with status {taskStatus.Name(servicer.task_status)}')
    print('Server: exiting')
    return servicer.task_status, servicer.task_error, servicer.result, servicer.logs_storage


if __name__ == '__main__':
    status, error, result, logs = srv_example('unix:./../tmp/test.sock', '0', 'fs_example', 'fs_example',
                                              '../tests/python/apps_example/fs_example', 'func_fs_list_info')
    sys.exit(0)


import pytest


@pytest.mark.parametrize(
    "address, port, app_name, module_name, module_path, function_to_call, args,"
    "expected_status, expected_error, expected_result, logs_must_contain",
    (
        ('unix:./../tmp/test.sock', '', 'hello_world', 'hello_world',
         '../tests/python/apps_example/hello_world', 'func_hello_world', None,
         taskStatus.ST_SUCCESS, '', 'OK', r'HelloWorld'),
        ('localhost', '0', 'hello_world', 'hello_world',
         '../tests/python/apps_example/hello_world', 'func_hello_world', None,
         taskStatus.ST_SUCCESS, '', 'OK', r'HelloWorld'),
        ('0.0.0.0', '', 'hello_world', 'hello_world',
         '../tests/python/apps_example/hello_world', 'func_hello_world', None,
         taskStatus.ST_SUCCESS, '', 'OK', r'HelloWorld'),
        ('[::]', '60051', 'hello_world', 'hello_world',
         '../tests/python/apps_example/hello_world', 'func_hello_world', None,
         taskStatus.ST_SUCCESS, '', 'OK', r'HelloWorld'),
    ),
    ids=(
        'unix',
        'local_random',
        'all_random',
        'ip6_port',
    ),
)
def test_hello_world(address, port, app_name, module_name, module_path, function_to_call, args,
                     expected_status, expected_error, expected_result, logs_must_contain):
    _status, _error, _result, _logs = srv_example(address, port,
                                                  app_name, module_name, module_path,
                                                  function_to_call, args)
    assert _status == expected_status
    assert _error == expected_error
    assert _result == expected_result
    if logs_must_contain:
        assert len([s for s in _logs if re.search(logs_must_contain, s) is not None]) > 0


@pytest.mark.parametrize(
    "address, port, app_name, module_name, module_path, function_to_call, args,"
    "expected_status, expected_error, expected_result, logs_must_contain",
    (
        ('unix:./../tmp/test.sock', '', 'invalid_app_name', 'hello_world',
         '../tests/python/apps_example/hello_world', 'func_hello_world', None,
         taskStatus.ST_INIT_ERROR, 'Directory with python packages for app cannot be accessed.', '', r''),
        ('localhost', '0', 'hello_world', 'invalid_module_name',
         '../tests/python/apps_example/hello_world', 'func_hello_world', None,
         taskStatus.ST_ERROR, 'Error loading invalid_module_name module.', '', r'cpa_core:Error.*module'),
        ('0.0.0.0', '', 'hello_world', 'hello_world',
         '../tests/python/invalid_path', 'func_hello_world', None,
         taskStatus.ST_ERROR, 'Error loading hello_world module.', '', r'cpa_core:Error.*module'),
        ('[::]', '60051', 'hello_world', 'hello_world',
         '../tests/python/apps_example/hello_world', 'invalid_function', None,
         taskStatus.ST_ERROR, 'Function invalid_function not found.', '', r'cpa_core:Function.*not\sfound'),
        ('[::]', '0', 'hello_world', 'hello_world',
         '../tests/python/apps_example/hello_world', 'func_hello_world', 'args_error',
         taskStatus.ST_EXCEPTION, 'TypeError', '', r'cpa_core:Exception\(TypeError\)'),
    ),
    ids=(
        'unix__invalid_app_name',
        'local_random__invalid_module_name',
        'all_random__invalid_path',
        'ip6_port__invalid_function',
        'ip6_random__args_error',
    ),
)
def test_error_handling(address, port, app_name, module_name, module_path, function_to_call, args,
                        expected_status, expected_error, expected_result, logs_must_contain):
    _status, _error, _result, _logs = srv_example(address, port,
                                                  app_name, module_name, module_path,
                                                  function_to_call, args)
    assert _status == expected_status
    assert _error == expected_error
    assert _result == expected_result
    if logs_must_contain:
        assert len([s for s in _logs if re.search(logs_must_contain, s) is not None]) > 0


@pytest.mark.parametrize(
    "address, port, app_name, module_name, module_path, function_to_call, args,"
    "expected_status, expected_error, expected_result, logs_must_contain",
    (
        ('unix:./../tmp/test.sock', '', 'hello_world', 'hello_world',
         '../tests/python/apps_example/hello_world', 'func_hello_world_fixed_two_args', ('one_', 'two'),
         taskStatus.ST_SUCCESS, '', 'one_two', r''),
        ('unix:./../tmp/test.sock', '', 'hello_world', 'hello_world',
         '../tests/python/apps_example/hello_world', 'func_hello_world_args', None,
         taskStatus.ST_SUCCESS, '', 'get 0 argument(s)', r''),
        ('localhost', '0', 'hello_world', 'hello_world',
         '../tests/python/apps_example/hello_world', 'func_hello_world_args', '1',
         taskStatus.ST_SUCCESS, '', 'get 1 argument(s)', r'hello_world_args:\(\'1\',\)'),
        ('0.0.0.0', '', 'hello_world', 'hello_world',
         '../tests/python/apps_example/hello_world', 'func_hello_world_args', ('1', '2'),
         taskStatus.ST_SUCCESS, '', 'get 2 argument(s)', r'hello_world_args:\(\'1\',\s\'2\'\)'),
        ('[::]', '60051', 'hello_world', 'hello_world',
         '../tests/python/apps_example/hello_world', 'func_no_result', None,
         taskStatus.ST_SUCCESS, '', '', r'cpa_core:Result length=`None`'),
        ('[::]', '0', 'hello_world', 'hello_world',
         '../tests/python/apps_example/hello_world', 'func_exception', None,
         taskStatus.ST_EXCEPTION, 'ValueError', '', r'cpa_core:Exception\(ValueError\):`TEST`'),
    ),
    ids=(
        'unix__fixed_two_args',
        'unix__none_args',
        'local_random__one_arg',
        'all_random__two_args',
        'ip6_port__no_result',
        'ip6_random__exception',
    ),
)
def test_other_basics(address, port, app_name, module_name, module_path, function_to_call, args,
                      expected_status, expected_error, expected_result, logs_must_contain):
    _status, _error, _result, _logs = srv_example(address, port,
                                                  app_name, module_name, module_path,
                                                  function_to_call, args)
    assert _status == expected_status
    assert _error == expected_error
    assert _result == expected_result
    if logs_must_contain:
        assert len([s for s in _logs if re.search(logs_must_contain, s) is not None]) > 0