# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: core.proto
"""Generated protocol buffer code."""
from google.protobuf.internal import enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor.FileDescriptor(
  name='core.proto',
  package='OCA.Cloud_Py_API.Proto',
  syntax='proto3',
  serialized_options=None,
  create_key=_descriptor._internal_create_key,
  serialized_pb=b'\n\ncore.proto\x12\x16OCA.Cloud_Py_API.Proto\"\x07\n\x05\x45mpty\"\x8d\x02\n\x08\x64\x62\x43onfig\x12\x0e\n\x06\x64\x62Type\x18\x01 \x01(\t\x12\x0e\n\x06\x64\x62User\x18\x02 \x01(\t\x12\x0e\n\x06\x64\x62Pass\x18\x03 \x01(\t\x12\x0e\n\x06\x64\x62Host\x18\x04 \x01(\t\x12\x0e\n\x06\x64\x62Name\x18\x05 \x01(\t\x12\x10\n\x08\x64\x62Prefix\x18\x06 \x01(\t\x12\x13\n\x0biniDbSocket\x18\x07 \x01(\t\x12\x11\n\tiniDbHost\x18\x08 \x01(\t\x12\x11\n\tiniDbPort\x18\t \x01(\t\x12\x16\n\x0e\x64\x62\x44riverSslKey\x18\n \x01(\t\x12\x17\n\x0f\x64\x62\x44riverSslCert\x18\x0b \x01(\t\x12\x15\n\rdbDriverSslCa\x18\x0c \x01(\t\x12\x1c\n\x14\x64\x62\x44riverSslVerifyCrt\x18\r \x01(\t\"\xc4\x03\n\rTaskInitReply\x12\x0f\n\x07\x61ppName\x18\x01 \x01(\t\x12\x0f\n\x07modName\x18\x02 \x01(\t\x12\x0f\n\x07modPath\x18\x03 \x01(\t\x12\x10\n\x08\x66uncName\x18\x04 \x01(\t\x12\x0c\n\x04\x61rgs\x18\x05 \x03(\t\x12@\n\x06\x63onfig\x18\x06 \x01(\x0b\x32\x30.OCA.Cloud_Py_API.Proto.TaskInitReply.cfgOptions\x12/\n\x05\x64\x62\x43\x66g\x18\x07 \x01(\x0b\x32 .OCA.Cloud_Py_API.Proto.dbConfig\x12\x0f\n\x07handler\x18\x08 \x01(\t\x1a\xdb\x01\n\ncfgOptions\x12/\n\x07log_lvl\x18\x01 \x01(\x0e\x32\x1e.OCA.Cloud_Py_API.Proto.logLvl\x12\x12\n\ndataFolder\x18\x02 \x01(\t\x12\x18\n\x10\x66rameworkAppData\x18\x03 \x01(\t\x12\x0e\n\x06userId\x18\x04 \x01(\t\x12\x15\n\ruseFileDirect\x18\x05 \x01(\x08\x12\x13\n\x0buseDBDirect\x18\x06 \x01(\x08\x12\x14\n\x0cmaxChunkSize\x18\x07 \x01(\x05\x12\x1c\n\x14maxCreateFileContent\x18\x08 \x01(\x05\"Z\n\x14TaskSetStatusRequest\x12\x33\n\x07st_code\x18\x01 \x01(\x0e\x32\".OCA.Cloud_Py_API.Proto.taskStatus\x12\r\n\x05\x65rror\x18\x02 \x01(\t\"!\n\x0fTaskExitRequest\x12\x0e\n\x06result\x18\x01 \x01(\t\"b\n\x0eTaskLogRequest\x12/\n\x07log_lvl\x18\x01 \x01(\x0e\x32\x1e.OCA.Cloud_Py_API.Proto.logLvl\x12\x0e\n\x06module\x18\x02 \x01(\t\x12\x0f\n\x07\x63ontent\x18\x03 \x03(\t*=\n\x06logLvl\x12\t\n\x05\x44\x45\x42UG\x10\x00\x12\x08\n\x04INFO\x10\x01\x12\x08\n\x04WARN\x10\x02\x12\t\n\x05\x45RROR\x10\x03\x12\t\n\x05\x46\x41TAL\x10\x04*s\n\ntaskStatus\x12\x0e\n\nST_SUCCESS\x10\x00\x12\x12\n\x0eST_IN_PROGRESS\x10\x01\x12\x11\n\rST_INIT_ERROR\x10\x02\x12\x10\n\x0cST_EXCEPTION\x10\x03\x12\x0c\n\x08ST_ERROR\x10\x04\x12\x0e\n\nST_UNKNOWN\x10\x05\x62\x06proto3'
)

_LOGLVL = _descriptor.EnumDescriptor(
  name='logLvl',
  full_name='OCA.Cloud_Py_API.Proto.logLvl',
  filename=None,
  file=DESCRIPTOR,
  create_key=_descriptor._internal_create_key,
  values=[
    _descriptor.EnumValueDescriptor(
      name='DEBUG', index=0, number=0,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='INFO', index=1, number=1,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='WARN', index=2, number=2,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='ERROR', index=3, number=3,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='FATAL', index=4, number=4,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
  ],
  containing_type=None,
  serialized_options=None,
  serialized_start=1001,
  serialized_end=1062,
)
_sym_db.RegisterEnumDescriptor(_LOGLVL)

logLvl = enum_type_wrapper.EnumTypeWrapper(_LOGLVL)
_TASKSTATUS = _descriptor.EnumDescriptor(
  name='taskStatus',
  full_name='OCA.Cloud_Py_API.Proto.taskStatus',
  filename=None,
  file=DESCRIPTOR,
  create_key=_descriptor._internal_create_key,
  values=[
    _descriptor.EnumValueDescriptor(
      name='ST_SUCCESS', index=0, number=0,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='ST_IN_PROGRESS', index=1, number=1,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='ST_INIT_ERROR', index=2, number=2,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='ST_EXCEPTION', index=3, number=3,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='ST_ERROR', index=4, number=4,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='ST_UNKNOWN', index=5, number=5,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
  ],
  containing_type=None,
  serialized_options=None,
  serialized_start=1064,
  serialized_end=1179,
)
_sym_db.RegisterEnumDescriptor(_TASKSTATUS)

taskStatus = enum_type_wrapper.EnumTypeWrapper(_TASKSTATUS)
DEBUG = 0
INFO = 1
WARN = 2
ERROR = 3
FATAL = 4
ST_SUCCESS = 0
ST_IN_PROGRESS = 1
ST_INIT_ERROR = 2
ST_EXCEPTION = 3
ST_ERROR = 4
ST_UNKNOWN = 5



_EMPTY = _descriptor.Descriptor(
  name='Empty',
  full_name='OCA.Cloud_Py_API.Proto.Empty',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=38,
  serialized_end=45,
)


_DBCONFIG = _descriptor.Descriptor(
  name='dbConfig',
  full_name='OCA.Cloud_Py_API.Proto.dbConfig',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='dbType', full_name='OCA.Cloud_Py_API.Proto.dbConfig.dbType', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='dbUser', full_name='OCA.Cloud_Py_API.Proto.dbConfig.dbUser', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='dbPass', full_name='OCA.Cloud_Py_API.Proto.dbConfig.dbPass', index=2,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='dbHost', full_name='OCA.Cloud_Py_API.Proto.dbConfig.dbHost', index=3,
      number=4, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='dbName', full_name='OCA.Cloud_Py_API.Proto.dbConfig.dbName', index=4,
      number=5, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='dbPrefix', full_name='OCA.Cloud_Py_API.Proto.dbConfig.dbPrefix', index=5,
      number=6, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='iniDbSocket', full_name='OCA.Cloud_Py_API.Proto.dbConfig.iniDbSocket', index=6,
      number=7, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='iniDbHost', full_name='OCA.Cloud_Py_API.Proto.dbConfig.iniDbHost', index=7,
      number=8, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='iniDbPort', full_name='OCA.Cloud_Py_API.Proto.dbConfig.iniDbPort', index=8,
      number=9, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='dbDriverSslKey', full_name='OCA.Cloud_Py_API.Proto.dbConfig.dbDriverSslKey', index=9,
      number=10, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='dbDriverSslCert', full_name='OCA.Cloud_Py_API.Proto.dbConfig.dbDriverSslCert', index=10,
      number=11, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='dbDriverSslCa', full_name='OCA.Cloud_Py_API.Proto.dbConfig.dbDriverSslCa', index=11,
      number=12, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='dbDriverSslVerifyCrt', full_name='OCA.Cloud_Py_API.Proto.dbConfig.dbDriverSslVerifyCrt', index=12,
      number=13, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=48,
  serialized_end=317,
)


_TASKINITREPLY_CFGOPTIONS = _descriptor.Descriptor(
  name='cfgOptions',
  full_name='OCA.Cloud_Py_API.Proto.TaskInitReply.cfgOptions',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='log_lvl', full_name='OCA.Cloud_Py_API.Proto.TaskInitReply.cfgOptions.log_lvl', index=0,
      number=1, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='dataFolder', full_name='OCA.Cloud_Py_API.Proto.TaskInitReply.cfgOptions.dataFolder', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='frameworkAppData', full_name='OCA.Cloud_Py_API.Proto.TaskInitReply.cfgOptions.frameworkAppData', index=2,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='userId', full_name='OCA.Cloud_Py_API.Proto.TaskInitReply.cfgOptions.userId', index=3,
      number=4, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='useFileDirect', full_name='OCA.Cloud_Py_API.Proto.TaskInitReply.cfgOptions.useFileDirect', index=4,
      number=5, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='useDBDirect', full_name='OCA.Cloud_Py_API.Proto.TaskInitReply.cfgOptions.useDBDirect', index=5,
      number=6, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='maxChunkSize', full_name='OCA.Cloud_Py_API.Proto.TaskInitReply.cfgOptions.maxChunkSize', index=6,
      number=7, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='maxCreateFileContent', full_name='OCA.Cloud_Py_API.Proto.TaskInitReply.cfgOptions.maxCreateFileContent', index=7,
      number=8, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=553,
  serialized_end=772,
)

_TASKINITREPLY = _descriptor.Descriptor(
  name='TaskInitReply',
  full_name='OCA.Cloud_Py_API.Proto.TaskInitReply',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='appName', full_name='OCA.Cloud_Py_API.Proto.TaskInitReply.appName', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='modName', full_name='OCA.Cloud_Py_API.Proto.TaskInitReply.modName', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='modPath', full_name='OCA.Cloud_Py_API.Proto.TaskInitReply.modPath', index=2,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='funcName', full_name='OCA.Cloud_Py_API.Proto.TaskInitReply.funcName', index=3,
      number=4, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='args', full_name='OCA.Cloud_Py_API.Proto.TaskInitReply.args', index=4,
      number=5, type=9, cpp_type=9, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='config', full_name='OCA.Cloud_Py_API.Proto.TaskInitReply.config', index=5,
      number=6, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='dbCfg', full_name='OCA.Cloud_Py_API.Proto.TaskInitReply.dbCfg', index=6,
      number=7, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='handler', full_name='OCA.Cloud_Py_API.Proto.TaskInitReply.handler', index=7,
      number=8, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[_TASKINITREPLY_CFGOPTIONS, ],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=320,
  serialized_end=772,
)


_TASKSETSTATUSREQUEST = _descriptor.Descriptor(
  name='TaskSetStatusRequest',
  full_name='OCA.Cloud_Py_API.Proto.TaskSetStatusRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='st_code', full_name='OCA.Cloud_Py_API.Proto.TaskSetStatusRequest.st_code', index=0,
      number=1, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='error', full_name='OCA.Cloud_Py_API.Proto.TaskSetStatusRequest.error', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=774,
  serialized_end=864,
)


_TASKEXITREQUEST = _descriptor.Descriptor(
  name='TaskExitRequest',
  full_name='OCA.Cloud_Py_API.Proto.TaskExitRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='result', full_name='OCA.Cloud_Py_API.Proto.TaskExitRequest.result', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=866,
  serialized_end=899,
)


_TASKLOGREQUEST = _descriptor.Descriptor(
  name='TaskLogRequest',
  full_name='OCA.Cloud_Py_API.Proto.TaskLogRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='log_lvl', full_name='OCA.Cloud_Py_API.Proto.TaskLogRequest.log_lvl', index=0,
      number=1, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='module', full_name='OCA.Cloud_Py_API.Proto.TaskLogRequest.module', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='content', full_name='OCA.Cloud_Py_API.Proto.TaskLogRequest.content', index=2,
      number=3, type=9, cpp_type=9, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=901,
  serialized_end=999,
)

_TASKINITREPLY_CFGOPTIONS.fields_by_name['log_lvl'].enum_type = _LOGLVL
_TASKINITREPLY_CFGOPTIONS.containing_type = _TASKINITREPLY
_TASKINITREPLY.fields_by_name['config'].message_type = _TASKINITREPLY_CFGOPTIONS
_TASKINITREPLY.fields_by_name['dbCfg'].message_type = _DBCONFIG
_TASKSETSTATUSREQUEST.fields_by_name['st_code'].enum_type = _TASKSTATUS
_TASKLOGREQUEST.fields_by_name['log_lvl'].enum_type = _LOGLVL
DESCRIPTOR.message_types_by_name['Empty'] = _EMPTY
DESCRIPTOR.message_types_by_name['dbConfig'] = _DBCONFIG
DESCRIPTOR.message_types_by_name['TaskInitReply'] = _TASKINITREPLY
DESCRIPTOR.message_types_by_name['TaskSetStatusRequest'] = _TASKSETSTATUSREQUEST
DESCRIPTOR.message_types_by_name['TaskExitRequest'] = _TASKEXITREQUEST
DESCRIPTOR.message_types_by_name['TaskLogRequest'] = _TASKLOGREQUEST
DESCRIPTOR.enum_types_by_name['logLvl'] = _LOGLVL
DESCRIPTOR.enum_types_by_name['taskStatus'] = _TASKSTATUS
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

Empty = _reflection.GeneratedProtocolMessageType('Empty', (_message.Message,), {
  'DESCRIPTOR' : _EMPTY,
  '__module__' : 'core_pb2'
  # @@protoc_insertion_point(class_scope:OCA.Cloud_Py_API.Proto.Empty)
  })
_sym_db.RegisterMessage(Empty)

dbConfig = _reflection.GeneratedProtocolMessageType('dbConfig', (_message.Message,), {
  'DESCRIPTOR' : _DBCONFIG,
  '__module__' : 'core_pb2'
  # @@protoc_insertion_point(class_scope:OCA.Cloud_Py_API.Proto.dbConfig)
  })
_sym_db.RegisterMessage(dbConfig)

TaskInitReply = _reflection.GeneratedProtocolMessageType('TaskInitReply', (_message.Message,), {

  'cfgOptions' : _reflection.GeneratedProtocolMessageType('cfgOptions', (_message.Message,), {
    'DESCRIPTOR' : _TASKINITREPLY_CFGOPTIONS,
    '__module__' : 'core_pb2'
    # @@protoc_insertion_point(class_scope:OCA.Cloud_Py_API.Proto.TaskInitReply.cfgOptions)
    })
  ,
  'DESCRIPTOR' : _TASKINITREPLY,
  '__module__' : 'core_pb2'
  # @@protoc_insertion_point(class_scope:OCA.Cloud_Py_API.Proto.TaskInitReply)
  })
_sym_db.RegisterMessage(TaskInitReply)
_sym_db.RegisterMessage(TaskInitReply.cfgOptions)

TaskSetStatusRequest = _reflection.GeneratedProtocolMessageType('TaskSetStatusRequest', (_message.Message,), {
  'DESCRIPTOR' : _TASKSETSTATUSREQUEST,
  '__module__' : 'core_pb2'
  # @@protoc_insertion_point(class_scope:OCA.Cloud_Py_API.Proto.TaskSetStatusRequest)
  })
_sym_db.RegisterMessage(TaskSetStatusRequest)

TaskExitRequest = _reflection.GeneratedProtocolMessageType('TaskExitRequest', (_message.Message,), {
  'DESCRIPTOR' : _TASKEXITREQUEST,
  '__module__' : 'core_pb2'
  # @@protoc_insertion_point(class_scope:OCA.Cloud_Py_API.Proto.TaskExitRequest)
  })
_sym_db.RegisterMessage(TaskExitRequest)

TaskLogRequest = _reflection.GeneratedProtocolMessageType('TaskLogRequest', (_message.Message,), {
  'DESCRIPTOR' : _TASKLOGREQUEST,
  '__module__' : 'core_pb2'
  # @@protoc_insertion_point(class_scope:OCA.Cloud_Py_API.Proto.TaskLogRequest)
  })
_sym_db.RegisterMessage(TaskLogRequest)


# @@protoc_insertion_point(module_scope)
