# Version of python API 0.1.0
from typing import Union
from enum import Enum

from .fs import FsObjId, FsObjInfo


class LogLvl(Enum):
    DEBUG = 0
    INFO = 1
    WARN = 2
    ERROR = 3
    FATAL = 4


_ncc: any


def _pyfrm_set_conn(cloud_connector):
    global _ncc
    _ncc = cloud_connector


class CloudApi:
    @staticmethod
    def log(log_lvl: Union[int, LogLvl], mod_name: str, content: Union[str, list, tuple]) -> None:
        if isinstance(log_lvl, LogLvl):
            log_lvl = log_lvl.value
        _ncc.log(log_lvl, mod_name, content)

    @staticmethod
    def dir_list(fs_id: FsObjId = None) -> list:
        if fs_id is not None:
            return _ncc.fs_list(fs_id.user_id, fs_id.file_id)
        return _ncc.fs_list()

    @staticmethod
    def file_info(fs_id: FsObjId = None) -> Union[FsObjInfo, None]:
        if fs_id is not None:
            return _ncc.fs_info(fs_id.user_id, fs_id.file_id)
        return _ncc.fs_info()