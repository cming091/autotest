# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: common.proto

from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor.FileDescriptor(
  name='common.proto',
  package='common',
  syntax='proto3',
  serialized_options=b'\n\036com.megvii.lbg.wes.grpc.commonZDgit-pd.megvii-inc.com/slg-service/frworkstation/internal/grpc/common',
  create_key=_descriptor._internal_create_key,
  serialized_pb=b'\n\x0c\x63ommon.proto\x12\x06\x63ommon\"N\n\x0e\x43ommonResponse\x12\x12\n\nreturnCode\x18\x01 \x01(\x03\x12\x11\n\treturnMsg\x18\x02 \x01(\t\x12\x15\n\rreturnUserMsg\x18\x03 \x01(\tBf\n\x1e\x63om.megvii.lbg.wes.grpc.commonZDgit-pd.megvii-inc.com/slg-service/frworkstation/internal/grpc/commonb\x06proto3'
)




_COMMONRESPONSE = _descriptor.Descriptor(
  name='CommonResponse',
  full_name='common.CommonResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='returnCode', full_name='common.CommonResponse.returnCode', index=0,
      number=1, type=3, cpp_type=2, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='returnMsg', full_name='common.CommonResponse.returnMsg', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='returnUserMsg', full_name='common.CommonResponse.returnUserMsg', index=2,
      number=3, type=9, cpp_type=9, label=1,
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
  serialized_start=24,
  serialized_end=102,
)

DESCRIPTOR.message_types_by_name['CommonResponse'] = _COMMONRESPONSE
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

CommonResponse = _reflection.GeneratedProtocolMessageType('CommonResponse', (_message.Message,), {
  'DESCRIPTOR' : _COMMONRESPONSE,
  '__module__' : 'common_pb2'
  # @@protoc_insertion_point(class_scope:common.CommonResponse)
  })
_sym_db.RegisterMessage(CommonResponse)


DESCRIPTOR._options = None
# @@protoc_insertion_point(module_scope)