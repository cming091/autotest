# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: containerExceptionTypeEnum.proto

from google.protobuf.internal import enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor.FileDescriptor(
  name='containerExceptionTypeEnum.proto',
  package='common',
  syntax='proto3',
  serialized_options=b'\n\036com.megvii.lbg.wes.grpc.commonZDgit-pd.megvii-inc.com/slg-service/frworkstation/internal/grpc/common',
  create_key=_descriptor._internal_create_key,
  serialized_pb=b'\n containerExceptionTypeEnum.proto\x12\x06\x63ommon*\xcb\x01\n\x1a\x43ontainerExceptionTypeEnum\x12\x0b\n\x07UNKNOWN\x10\x00\x12\x15\n\x11NewSkuWithoutCode\x10\x01\x12\x15\n\x11NewSkuContainCode\x10\x02\x12\x17\n\x13SkuQuantityMismatch\x10\x03\x12\x0c\n\x08MixedSku\x10\x65\x12\x18\n\x14LessNumberOrBlocking\x10\x66\x12\x0e\n\nOverNumber\x10g\x12\x0e\n\nOverweight\x10h\x12\x11\n\rRFReadFailure\x10iBf\n\x1e\x63om.megvii.lbg.wes.grpc.commonZDgit-pd.megvii-inc.com/slg-service/frworkstation/internal/grpc/commonb\x06proto3'
)

_CONTAINEREXCEPTIONTYPEENUM = _descriptor.EnumDescriptor(
  name='ContainerExceptionTypeEnum',
  full_name='common.ContainerExceptionTypeEnum',
  filename=None,
  file=DESCRIPTOR,
  create_key=_descriptor._internal_create_key,
  values=[
    _descriptor.EnumValueDescriptor(
      name='UNKNOWN', index=0, number=0,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='NewSkuWithoutCode', index=1, number=1,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='NewSkuContainCode', index=2, number=2,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='SkuQuantityMismatch', index=3, number=3,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='MixedSku', index=4, number=101,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='LessNumberOrBlocking', index=5, number=102,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='OverNumber', index=6, number=103,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='Overweight', index=7, number=104,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='RFReadFailure', index=8, number=105,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
  ],
  containing_type=None,
  serialized_options=None,
  serialized_start=45,
  serialized_end=248,
)
_sym_db.RegisterEnumDescriptor(_CONTAINEREXCEPTIONTYPEENUM)

ContainerExceptionTypeEnum = enum_type_wrapper.EnumTypeWrapper(_CONTAINEREXCEPTIONTYPEENUM)
UNKNOWN = 0
NewSkuWithoutCode = 1
NewSkuContainCode = 2
SkuQuantityMismatch = 3
MixedSku = 101
LessNumberOrBlocking = 102
OverNumber = 103
Overweight = 104
RFReadFailure = 105


DESCRIPTOR.enum_types_by_name['ContainerExceptionTypeEnum'] = _CONTAINEREXCEPTIONTYPEENUM
_sym_db.RegisterFileDescriptor(DESCRIPTOR)


DESCRIPTOR._options = None
# @@protoc_insertion_point(module_scope)