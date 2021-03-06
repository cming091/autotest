# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: warectu.proto

from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from  ..common import common_pb2 as common__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='warectu.proto',
  package='warectu',
  syntax='proto3',
  serialized_options=b'ZFgit-pd.megvii-inc.com/slg-service/frworkstation/internal/protp/warectu',
  create_key=_descriptor._internal_create_key,
  serialized_pb=b'\n\rwarectu.proto\x12\x07warectu\x1a\x0c\x63ommon.proto\"W\n\x16TransferTriggerRequest\x12\x15\n\rwarehouseCode\x18\x01 \x01(\t\x12\x12\n\nregionCode\x18\x02 \x01(\t\x12\x12\n\nwaveNoList\x18\x03 \x03(\t\"~\n\x1c\x45xchangeChooseStationRequest\x12\x15\n\rwarehouseCode\x18\x01 \x01(\t\x12\x13\n\x0binComingBox\x18\x02 \x01(\t\x12\x32\n\x11stationBoxMapList\x18\x03 \x03(\x0b\x32\x17.warectu.StationBoxList\"2\n\x0eStationBoxList\x12\x0f\n\x07station\x18\x01 \x01(\t\x12\x0f\n\x07\x42oxCode\x18\x02 \x01(\t\"\x89\x01\n\x1d\x45xchangeChooseStationResponse\x12\x12\n\nreturnCode\x18\x01 \x01(\x03\x12\x11\n\treturnMsg\x18\x02 \x01(\t\x12\x15\n\rreturnUserMsg\x18\x03 \x01(\t\x12*\n\x04\x64\x61ta\x18\x04 \x01(\x0b\x32\x1c.warectu.ChooseStationDetail\"*\n\x13\x43hooseStationDetail\x12\x13\n\x0bStationCode\x18\x01 \x01(\t2\xc2\x01\n\x07Warectu\x12M\n\x0fTransferTrigger\x12\x1f.warectu.TransferTriggerRequest\x1a\x17.warectu.CommonResponse\"\x00\x12h\n\x15\x45xchangeChooseStation\x12%.warectu.ExchangeChooseStationRequest\x1a&.warectu.ExchangeChooseStationResponse\"\x00\x42HZFgit-pd.megvii-inc.com/slg-service/frworkstation/internal/protp/warectub\x06proto3'
  ,
  dependencies=[common__pb2.DESCRIPTOR,])




_TRANSFERTRIGGERREQUEST = _descriptor.Descriptor(
  name='TransferTriggerRequest',
  full_name='warectu.TransferTriggerRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='warehouseCode', full_name='warectu.TransferTriggerRequest.warehouseCode', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='regionCode', full_name='warectu.TransferTriggerRequest.regionCode', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='waveNoList', full_name='warectu.TransferTriggerRequest.waveNoList', index=2,
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
  serialized_start=40,
  serialized_end=127,
)


_EXCHANGECHOOSESTATIONREQUEST = _descriptor.Descriptor(
  name='ExchangeChooseStationRequest',
  full_name='warectu.ExchangeChooseStationRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='warehouseCode', full_name='warectu.ExchangeChooseStationRequest.warehouseCode', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='inComingBox', full_name='warectu.ExchangeChooseStationRequest.inComingBox', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='stationBoxMapList', full_name='warectu.ExchangeChooseStationRequest.stationBoxMapList', index=2,
      number=3, type=11, cpp_type=10, label=3,
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
  serialized_start=129,
  serialized_end=255,
)


_STATIONBOXLIST = _descriptor.Descriptor(
  name='StationBoxList',
  full_name='warectu.StationBoxList',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='station', full_name='warectu.StationBoxList.station', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='BoxCode', full_name='warectu.StationBoxList.BoxCode', index=1,
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
  serialized_start=257,
  serialized_end=307,
)


_EXCHANGECHOOSESTATIONRESPONSE = _descriptor.Descriptor(
  name='ExchangeChooseStationResponse',
  full_name='warectu.ExchangeChooseStationResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='returnCode', full_name='warectu.ExchangeChooseStationResponse.returnCode', index=0,
      number=1, type=3, cpp_type=2, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='returnMsg', full_name='warectu.ExchangeChooseStationResponse.returnMsg', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='returnUserMsg', full_name='warectu.ExchangeChooseStationResponse.returnUserMsg', index=2,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='data', full_name='warectu.ExchangeChooseStationResponse.data', index=3,
      number=4, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
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
  serialized_start=310,
  serialized_end=447,
)


_CHOOSESTATIONDETAIL = _descriptor.Descriptor(
  name='ChooseStationDetail',
  full_name='warectu.ChooseStationDetail',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='StationCode', full_name='warectu.ChooseStationDetail.StationCode', index=0,
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
  serialized_start=449,
  serialized_end=491,
)

_EXCHANGECHOOSESTATIONREQUEST.fields_by_name['stationBoxMapList'].message_type = _STATIONBOXLIST
_EXCHANGECHOOSESTATIONRESPONSE.fields_by_name['data'].message_type = _CHOOSESTATIONDETAIL
DESCRIPTOR.message_types_by_name['TransferTriggerRequest'] = _TRANSFERTRIGGERREQUEST
DESCRIPTOR.message_types_by_name['ExchangeChooseStationRequest'] = _EXCHANGECHOOSESTATIONREQUEST
DESCRIPTOR.message_types_by_name['StationBoxList'] = _STATIONBOXLIST
DESCRIPTOR.message_types_by_name['ExchangeChooseStationResponse'] = _EXCHANGECHOOSESTATIONRESPONSE
DESCRIPTOR.message_types_by_name['ChooseStationDetail'] = _CHOOSESTATIONDETAIL
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

TransferTriggerRequest = _reflection.GeneratedProtocolMessageType('TransferTriggerRequest', (_message.Message,), {
  'DESCRIPTOR' : _TRANSFERTRIGGERREQUEST,
  '__module__' : 'warectu_pb2'
  # @@protoc_insertion_point(class_scope:warectu.TransferTriggerRequest)
  })
_sym_db.RegisterMessage(TransferTriggerRequest)

ExchangeChooseStationRequest = _reflection.GeneratedProtocolMessageType('ExchangeChooseStationRequest', (_message.Message,), {
  'DESCRIPTOR' : _EXCHANGECHOOSESTATIONREQUEST,
  '__module__' : 'warectu_pb2'
  # @@protoc_insertion_point(class_scope:warectu.ExchangeChooseStationRequest)
  })
_sym_db.RegisterMessage(ExchangeChooseStationRequest)

StationBoxList = _reflection.GeneratedProtocolMessageType('StationBoxList', (_message.Message,), {
  'DESCRIPTOR' : _STATIONBOXLIST,
  '__module__' : 'warectu_pb2'
  # @@protoc_insertion_point(class_scope:warectu.StationBoxList)
  })
_sym_db.RegisterMessage(StationBoxList)

ExchangeChooseStationResponse = _reflection.GeneratedProtocolMessageType('ExchangeChooseStationResponse', (_message.Message,), {
  'DESCRIPTOR' : _EXCHANGECHOOSESTATIONRESPONSE,
  '__module__' : 'warectu_pb2'
  # @@protoc_insertion_point(class_scope:warectu.ExchangeChooseStationResponse)
  })
_sym_db.RegisterMessage(ExchangeChooseStationResponse)

ChooseStationDetail = _reflection.GeneratedProtocolMessageType('ChooseStationDetail', (_message.Message,), {
  'DESCRIPTOR' : _CHOOSESTATIONDETAIL,
  '__module__' : 'warectu_pb2'
  # @@protoc_insertion_point(class_scope:warectu.ChooseStationDetail)
  })
_sym_db.RegisterMessage(ChooseStationDetail)


DESCRIPTOR._options = None

_WARECTU = _descriptor.ServiceDescriptor(
  name='Warectu',
  full_name='warectu.Warectu',
  file=DESCRIPTOR,
  index=0,
  serialized_options=None,
  create_key=_descriptor._internal_create_key,
  serialized_start=494,
  serialized_end=688,
  methods=[
  _descriptor.MethodDescriptor(
    name='TransferTrigger',
    full_name='warectu.Warectu.TransferTrigger',
    index=0,
    containing_service=None,
    input_type=_TRANSFERTRIGGERREQUEST,
    output_type=common__pb2._COMMONRESPONSE,
    serialized_options=None,
    create_key=_descriptor._internal_create_key,
  ),
  _descriptor.MethodDescriptor(
    name='ExchangeChooseStation',
    full_name='warectu.Warectu.ExchangeChooseStation',
    index=1,
    containing_service=None,
    input_type=_EXCHANGECHOOSESTATIONREQUEST,
    output_type=_EXCHANGECHOOSESTATIONRESPONSE,
    serialized_options=None,
    create_key=_descriptor._internal_create_key,
  ),
])
_sym_db.RegisterServiceDescriptor(_WARECTU)

DESCRIPTOR.services_by_name['Warectu'] = _WARECTU

# @@protoc_insertion_point(module_scope)
