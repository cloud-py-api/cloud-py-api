from typing import Union
from enum import Enum
from io import BytesIO
import json

from . import _ncc
from .exceptions import FsNotFound


class FsObj:
    id = {}
    info = {}

    def __init__(self, user_id: str = '', file_id: int = 0, load: bool = False):
        self.id['user'] = user_id
        self.id['file'] = file_id
        if load:
            self.load()

    def init_from(self, data):
        if not isinstance(data, dict):
            data = json.loads(data)
        self.id = data['id']
        self.info = data['info']
        return self

    def __repr__(self):
        return json.dumps({'id': str(self.id), 'info': str(self.info)})

    def load(self) -> None:
        _info = FsApi().info(self)
        if not _info:
            raise FsNotFound(f'No info for:{str(self.id)}')
        self.init_from(_info)

    def list(self) -> list:
        _r = []
        _is_dir = self.info.get('is_dir')
        if _is_dir is not None:
            if not _is_dir:
                return _r
        _objs = FsApi().list(self)
        for _obj in _objs:
            _r.append(FsObj().init_from(_obj))
        return _r

    def read(self):
        pass

    def write(self):
        pass

    def create(self):
        pass

    def delete(self):
        pass

    def move(self):
        pass


class FsResultCode(Enum):
    NO_ERROR = 0
    NOT_PERMITTED = 1
    LOCKED = 2
    NOT_FOUND = 3
    IO_ERROR = 4


class FsApi:
    def list(self, fs_obj: Union[None, dict, FsObj] = None) -> list:
        return _ncc.NCC.fs_list(*self.__arg_to_fs_id(fs_obj))

    def info(self, fs_obj: Union[None, dict, FsObj] = None) -> dict:
        return _ncc.NCC.fs_info(*self.__arg_to_fs_id(fs_obj))

    def create(self, name: str, is_dir: bool = False, parent_dir: Union[None, dict, FsObj] = None,
               content: bytes = b'') -> [FsResultCode, dict]:
        if is_dir and len(content) > 0:
            raise ValueError('Content can be specified only for files.')
        __write_after = False
        if len(content) > _ncc.NCC.task_init_data.config.maxCreateFileContent:
            __write_after = True
        _result, _user_id, _file_id = _ncc.NCC.fs_create(*self.__arg_to_fs_id(parent_dir),
                                                         name, not is_dir, content if not __write_after else b'')
        if _result != FsResultCode.NO_ERROR:
            return _result, {}
        _created_object = {'user': _user_id, 'file': _file_id}
        if __write_after:
            _result = self.write_file(_created_object, BytesIO(content))
        return _result, _created_object

    def read_file(self, fs_obj: Union[dict, FsObj], output_obj: BytesIO,
                  offset: int = 0, bytes_to_read: int = 0) -> FsResultCode:
        return _ncc.NCC.fs_read(*self.__arg_to_fs_id(fs_obj, deny_root=True), output_obj, offset, bytes_to_read)

    def write_file(self, fs_obj: Union[dict, FsObj], content: BytesIO) -> FsResultCode:
        return _ncc.NCC.fs_write(*self.__arg_to_fs_id(fs_obj, deny_root=True), content)

    def delete(self, fs_obj: Union[dict, FsObj]) -> FsResultCode:
        return _ncc.NCC.fs_delete(*self.__arg_to_fs_id(fs_obj, deny_root=True))

    def move(self, fs_obj: Union[dict, FsObj], target_path: str, copy: bool = False) -> [FsResultCode, dict]:
        if target_path:
            raise ValueError('target_path must be specified.')
        _result, _user_id, _file_id = _ncc.NCC.fs_move(*self.__arg_to_fs_id(fs_obj, deny_root=True), target_path, copy)
        if _result != FsResultCode.NO_ERROR:
            return _result, {}
        return _result, {'user': _user_id, 'file': _file_id}

    @staticmethod
    def __arg_to_fs_id(arg: Union[None, dict, FsObj], deny_root: bool = False) -> [str, int]:
        if arg is None:
            if deny_root:
                raise ValueError('fs_id can not be None for this method.')
            return '', 0
        if not isinstance(arg, (dict, FsObj)):
            raise ValueError('fs_id can be None, dict or FsObj only.')
        if isinstance(arg, FsObj):
            arg = arg.id
        elif arg.get('id') is not None:
            arg = arg.get('id')
        if deny_root:
            return arg['user'], arg['file']
        return arg.get('user', ''), arg.get('file', 0)