# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: wareshuttle.proto

from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from  ..common import common_pb2 as common__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='wareshuttle.proto',
  package='wareshuttle',
  syntax='proto3',
  serialized_options=b'ZIgit-pd.megvii-inc.com/slg-service/frworkstation/internal/grpc/wareshuttle',
  create_key=_descriptor._internal_create_key,
  serialized_pb=b'\n\x11wareshuttle.proto\x12\x0bwareshuttle\x1a\x0c\x63ommon.proto\"z\n\x12\x41ssignFloorRequest\x12\x0f\n\x07traceID\x18\x01 \x01(\t\x12\x13\n\x0bwarehouseID\x18\x02 \x01(\t\x12\x15\n\rwarehouseCode\x18\x03 \x01(\t\x12\x12\n\nregionCode\x18\x04 \x01(\t\x12\x13\n\x0b\x66rameIDList\x18\x05 \x03(\t\"\xba\x01\n\x13\x41ssignFloorResponse\x12\x12\n\nreturnCode\x18\x01 \x01(\x03\x12\x11\n\treturnMsg\x18\x02 \x01(\t\x12\x15\n\rreturnUserMsg\x18\x03 \x01(\t\x12\x38\n\x04\x64\x61ta\x18\x04 \x03(\x0b\x32*.wareshuttle.AssignFloorResponse.DataEntry\x1a+\n\tDataEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12\r\n\x05value\x18\x02 \x01(\t:\x02\x38\x01\"\x95\x01\n\x13PreemptFloorRequest\x12\x0f\n\x07traceID\x18\x01 \x01(\t\x12\x13\n\x0bwarehouseID\x18\x02 \x01(\t\x12\x15\n\rwarehouseCode\x18\x03 \x01(\t\x12\x12\n\nregionCode\x18\x04 \x01(\t\x12\x11\n\tsessionID\x18\x05 \x01(\x03\x12\r\n\x05mapID\x18\x06 \x01(\t\x12\x0b\n\x03qty\x18\x07 \x01(\x03\"\x88\x01\n\x13ReleaseFloorRequest\x12\x0f\n\x07traceID\x18\x01 \x01(\t\x12\x13\n\x0bwarehouseID\x18\x02 \x01(\t\x12\x15\n\rwarehouseCode\x18\x03 \x01(\t\x12\x12\n\nregionCode\x18\x04 \x01(\t\x12\x11\n\tsessionID\x18\x05 \x01(\x03\x12\r\n\x05mapID\x18\x06 \x01(\t\"\x86\x01\n\x12ReportFloorRequest\x12\x0f\n\x07traceID\x18\x01 \x01(\t\x12\x13\n\x0bwarehouseID\x18\x02 \x01(\t\x12\x15\n\rwarehouseCode\x18\x03 \x01(\t\x12\x12\n\nregionCode\x18\x04 \x01(\t\x12\x10\n\x08\x61\x63tAggID\x18\x06 \x01(\x03\x12\r\n\x05mapID\x18\x07 \x01(\t\"\x9b\x01\n\x14TriggerTakeInRequest\x12\x0f\n\x07traceID\x18\x01 \x01(\t\x12\x13\n\x0bwarehouseID\x18\x02 \x01(\t\x12\x15\n\rwarehouseCode\x18\x03 \x01(\t\x12\x12\n\nregionCode\x18\x04 \x01(\t\x12\x11\n\tsessionID\x18\x05 \x01(\x03\x12\x10\n\x08\x61\x63tAggID\x18\x06 \x01(\x03\x12\r\n\x05mapID\x18\x07 \x01(\t\"\x8c\x01\n\x14ReportDoneOutRequest\x12\x0f\n\x07traceID\x18\x01 \x01(\t\x12\x13\n\x0bwarehouseID\x18\x02 \x01(\t\x12\x15\n\rwarehouseCode\x18\x03 \x01(\t\x12\x12\n\nregionCode\x18\x04 \x01(\t\x12\x11\n\tsessionID\x18\x05 \x01(\x03\x12\x10\n\x08\x61\x63tAggID\x18\x06 \x01(\x03\"\x8b\x01\n\x13ReportDoneInRequest\x12\x0f\n\x07traceID\x18\x01 \x01(\t\x12\x13\n\x0bwarehouseID\x18\x02 \x01(\t\x12\x15\n\rwarehouseCode\x18\x03 \x01(\t\x12\x12\n\nregionCode\x18\x04 \x01(\t\x12\x11\n\tsessionID\x18\x05 \x01(\x03\x12\x10\n\x08\x61\x63tAggID\x18\x06 \x01(\x03\x32\xab\x04\n\x0bWareShuttle\x12R\n\x0b\x41ssignFloor\x12\x1f.wareshuttle.AssignFloorRequest\x1a .wareshuttle.AssignFloorResponse\"\x00\x12J\n\x0cPreemptFloor\x12 .wareshuttle.PreemptFloorRequest\x1a\x16.common.CommonResponse\"\x00\x12J\n\x0cReleaseFloor\x12 .wareshuttle.ReleaseFloorRequest\x1a\x16.common.CommonResponse\"\x00\x12H\n\x0bReportFloor\x12\x1f.wareshuttle.ReportFloorRequest\x1a\x16.common.CommonResponse\"\x00\x12L\n\rTriggerTakeIn\x12!.wareshuttle.TriggerTakeInRequest\x1a\x16.common.CommonResponse\"\x00\x12L\n\rReportDoneOut\x12!.wareshuttle.ReportDoneOutRequest\x1a\x16.common.CommonResponse\"\x00\x12J\n\x0cReportDoneIn\x12 .wareshuttle.ReportDoneInRequest\x1a\x16.common.CommonResponse\"\x00\x42KZIgit-pd.megvii-inc.com/slg-service/frworkstation/internal/grpc/wareshuttleb\x06proto3'
  ,
  dependencies=[common__pb2.DESCRIPTOR,])




_ASSIGNFLOORREQUEST = _descriptor.Descriptor(
  name='AssignFloorRequest',
  full_name='wareshuttle.AssignFloorRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='traceID', full_name='wareshuttle.AssignFloorRequest.traceID', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='warehouseID', full_name='wareshuttle.AssignFloorRequest.warehouseID', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='warehouseCode', full_name='wareshuttle.AssignFloorRequest.warehouseCode', index=2,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='regionCode', full_name='wareshuttle.AssignFloorRequest.regionCode', index=3,
      number=4, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='frameIDList', full_name='wareshuttle.AssignFloorRequest.frameIDList', index=4,
      number=5, type=9, cpp_type=9, label=3,
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
  serialized_start=48,
  serialized_end=170,
)


_ASSIGNFLOORRESPONSE_DATAENTRY = _descriptor.Descriptor(
  name='DataEntry',
  full_name='wareshuttle.AssignFloorResponse.DataEntry',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='key', full_name='wareshuttle.AssignFloorResponse.DataEntry.key', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='value', full_name='wareshuttle.AssignFloorResponse.DataEntry.value', index=1,
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
  serialized_options=b'8\001',
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=316,
  serialized_end=359,
)

_ASSIGNFLOORRESPONSE = _descriptor.Descriptor(
  name='AssignFloorResponse',
  full_name='wareshuttle.AssignFloorResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='returnCode', full_name='wareshuttle.AssignFloorResponse.returnCode', index=0,
      number=1, type=3, cpp_type=2, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='returnMsg', full_name='wareshuttle.AssignFloorResponse.returnMsg', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='returnUserMsg', full_name='wareshuttle.AssignFloorResponse.returnUserMsg', index=2,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='data', full_name='wareshuttle.AssignFloorResponse.data', index=3,
      number=4, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[_ASSIGNFLOORRESPONSE_DATAENTRY, ],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=173,
  serialized_end=359,
)


_PREEMPTFLOORREQUEST = _descriptor.Descriptor(
  name='PreemptFloorRequest',
  full_name='wareshuttle.PreemptFloorRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='traceID', full_name='wareshuttle.PreemptFloorRequest.traceID', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='warehouseID', full_name='wareshuttle.PreemptFloorRequest.warehouseID', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='warehouseCode', full_name='wareshuttle.PreemptFloorRequest.warehouseCode', index=2,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='regionCode', full_name='wareshuttle.PreemptFloorRequest.regionCode', index=3,
      number=4, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='sessionID', full_name='wareshuttle.PreemptFloorRequest.sessionID', index=4,
      number=5, type=3, cpp_type=2, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='mapID', full_name='wareshuttle.PreemptFloorRequest.mapID', index=5,
      number=6, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='qty', full_name='wareshuttle.PreemptFloorRequest.qty', index=6,
      number=7, type=3, cpp_type=2, label=1,
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
  serialized_start=362,
  serialized_end=511,
)


_RELEASEFLOORREQUEST = _descriptor.Descriptor(
  name='ReleaseFloorRequest',
  full_name='wareshuttle.ReleaseFloorRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='traceID', full_name='wareshuttle.ReleaseFloorRequest.traceID', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='warehouseID', full_name='wareshuttle.ReleaseFloorRequest.warehouseID', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='warehouseCode', full_name='wareshuttle.ReleaseFloorRequest.warehouseCode', index=2,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='regionCode', full_name='wareshuttle.ReleaseFloorRequest.regionCode', index=3,
      number=4, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='sessionID', full_name='wareshuttle.ReleaseFloorRequest.sessionID', index=4,
      number=5, type=3, cpp_type=2, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='mapID', full_name='wareshuttle.ReleaseFloorRequest.mapID', index=5,
      number=6, type=9, cpp_type=9, label=1,
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
  serialized_start=514,
  serialized_end=650,
)


_REPORTFLOORREQUEST = _descriptor.Descriptor(
  name='ReportFloorRequest',
  full_name='wareshuttle.ReportFloorRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='traceID', full_name='wareshuttle.ReportFloorRequest.traceID', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='warehouseID', full_name='wareshuttle.ReportFloorRequest.warehouseID', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='warehouseCode', full_name='wareshuttle.ReportFloorRequest.warehouseCode', index=2,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='regionCode', full_name='wareshuttle.ReportFloorRequest.regionCode', index=3,
      number=4, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='actAggID', full_name='wareshuttle.ReportFloorRequest.actAggID', index=4,
      number=6, type=3, cpp_type=2, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='mapID', full_name='wareshuttle.ReportFloorRequest.mapID', index=5,
      number=7, type=9, cpp_type=9, label=1,
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
  serialized_start=653,
  serialized_end=787,
)


_TRIGGERTAKEINREQUEST = _descriptor.Descriptor(
  name='TriggerTakeInRequest',
  full_name='wareshuttle.TriggerTakeInRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='traceID', full_name='wareshuttle.TriggerTakeInRequest.traceID', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='warehouseID', full_name='wareshuttle.TriggerTakeInRequest.warehouseID', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='warehouseCode', full_name='wareshuttle.TriggerTakeInRequest.warehouseCode', index=2,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='regionCode', full_name='wareshuttle.TriggerTakeInRequest.regionCode', index=3,
      number=4, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='sessionID', full_name='wareshuttle.TriggerTakeInRequest.sessionID', index=4,
      number=5, type=3, cpp_type=2, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='actAggID', full_name='wareshuttle.TriggerTakeInRequest.actAggID', index=5,
      number=6, type=3, cpp_type=2, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='mapID', full_name='wareshuttle.TriggerTakeInRequest.mapID', index=6,
      number=7, type=9, cpp_type=9, label=1,
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
  serialized_start=790,
  serialized_end=945,
)


_REPORTDONEOUTREQUEST = _descriptor.Descriptor(
  name='ReportDoneOutRequest',
  full_name='wareshuttle.ReportDoneOutRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='traceID', full_name='wareshuttle.ReportDoneOutRequest.traceID', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='warehouseID', full_name='wareshuttle.ReportDoneOutRequest.warehouseID', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='warehouseCode', full_name='wareshuttle.ReportDoneOutRequest.warehouseCode', index=2,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='regionCode', full_name='wareshuttle.ReportDoneOutRequest.regionCode', index=3,
      number=4, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='sessionID', full_name='wareshuttle.ReportDoneOutRequest.sessionID', index=4,
      number=5, type=3, cpp_type=2, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='actAggID', full_name='wareshuttle.ReportDoneOutRequest.actAggID', index=5,
      number=6, type=3, cpp_type=2, label=1,
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
  serialized_start=948,
  serialized_end=1088,
)


_REPORTDONEINREQUEST = _descriptor.Descriptor(
  name='ReportDoneInRequest',
  full_name='wareshuttle.ReportDoneInRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='traceID', full_name='wareshuttle.ReportDoneInRequest.traceID', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='warehouseID', full_name='wareshuttle.ReportDoneInRequest.warehouseID', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='warehouseCode', full_name='wareshuttle.ReportDoneInRequest.warehouseCode', index=2,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='regionCode', full_name='wareshuttle.ReportDoneInRequest.regionCode', index=3,
      number=4, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='sessionID', full_name='wareshuttle.ReportDoneInRequest.sessionID', index=4,
      number=5, type=3, cpp_type=2, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='actAggID', full_name='wareshuttle.ReportDoneInRequest.actAggID', index=5,
      number=6, type=3, cpp_type=2, label=1,
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
  serialized_start=1091,
  serialized_end=1230,
)

_ASSIGNFLOORRESPONSE_DATAENTRY.containing_type = _ASSIGNFLOORRESPONSE
_ASSIGNFLOORRESPONSE.fields_by_name['data'].message_type = _ASSIGNFLOORRESPONSE_DATAENTRY
DESCRIPTOR.message_types_by_name['AssignFloorRequest'] = _ASSIGNFLOORREQUEST
DESCRIPTOR.message_types_by_name['AssignFloorResponse'] = _ASSIGNFLOORRESPONSE
DESCRIPTOR.message_types_by_name['PreemptFloorRequest'] = _PREEMPTFLOORREQUEST
DESCRIPTOR.message_types_by_name['ReleaseFloorRequest'] = _RELEASEFLOORREQUEST
DESCRIPTOR.message_types_by_name['ReportFloorRequest'] = _REPORTFLOORREQUEST
DESCRIPTOR.message_types_by_name['TriggerTakeInRequest'] = _TRIGGERTAKEINREQUEST
DESCRIPTOR.message_types_by_name['ReportDoneOutRequest'] = _REPORTDONEOUTREQUEST
DESCRIPTOR.message_types_by_name['ReportDoneInRequest'] = _REPORTDONEINREQUEST
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

AssignFloorRequest = _reflection.GeneratedProtocolMessageType('AssignFloorRequest', (_message.Message,), {
  'DESCRIPTOR' : _ASSIGNFLOORREQUEST,
  '__module__' : 'wareshuttle_pb2'
  # @@protoc_insertion_point(class_scope:wareshuttle.AssignFloorRequest)
  })
_sym_db.RegisterMessage(AssignFloorRequest)

AssignFloorResponse = _reflection.GeneratedProtocolMessageType('AssignFloorResponse', (_message.Message,), {

  'DataEntry' : _reflection.GeneratedProtocolMessageType('DataEntry', (_message.Message,), {
    'DESCRIPTOR' : _ASSIGNFLOORRESPONSE_DATAENTRY,
    '__module__' : 'wareshuttle_pb2'
    # @@protoc_insertion_point(class_scope:wareshuttle.AssignFloorResponse.DataEntry)
    })
  ,
  'DESCRIPTOR' : _ASSIGNFLOORRESPONSE,
  '__module__' : 'wareshuttle_pb2'
  # @@protoc_insertion_point(class_scope:wareshuttle.AssignFloorResponse)
  })
_sym_db.RegisterMessage(AssignFloorResponse)
_sym_db.RegisterMessage(AssignFloorResponse.DataEntry)

PreemptFloorRequest = _reflection.GeneratedProtocolMessageType('PreemptFloorRequest', (_message.Message,), {
  'DESCRIPTOR' : _PREEMPTFLOORREQUEST,
  '__module__' : 'wareshuttle_pb2'
  # @@protoc_insertion_point(class_scope:wareshuttle.PreemptFloorRequest)
  })
_sym_db.RegisterMessage(PreemptFloorRequest)

ReleaseFloorRequest = _reflection.GeneratedProtocolMessageType('ReleaseFloorRequest', (_message.Message,), {
  'DESCRIPTOR' : _RELEASEFLOORREQUEST,
  '__module__' : 'wareshuttle_pb2'
  # @@protoc_insertion_point(class_scope:wareshuttle.ReleaseFloorRequest)
  })
_sym_db.RegisterMessage(ReleaseFloorRequest)

ReportFloorRequest = _reflection.GeneratedProtocolMessageType('ReportFloorRequest', (_message.Message,), {
  'DESCRIPTOR' : _REPORTFLOORREQUEST,
  '__module__' : 'wareshuttle_pb2'
  # @@protoc_insertion_point(class_scope:wareshuttle.ReportFloorRequest)
  })
_sym_db.RegisterMessage(ReportFloorRequest)

TriggerTakeInRequest = _reflection.GeneratedProtocolMessageType('TriggerTakeInRequest', (_message.Message,), {
  'DESCRIPTOR' : _TRIGGERTAKEINREQUEST,
  '__module__' : 'wareshuttle_pb2'
  # @@protoc_insertion_point(class_scope:wareshuttle.TriggerTakeInRequest)
  })
_sym_db.RegisterMessage(TriggerTakeInRequest)

ReportDoneOutRequest = _reflection.GeneratedProtocolMessageType('ReportDoneOutRequest', (_message.Message,), {
  'DESCRIPTOR' : _REPORTDONEOUTREQUEST,
  '__module__' : 'wareshuttle_pb2'
  # @@protoc_insertion_point(class_scope:wareshuttle.ReportDoneOutRequest)
  })
_sym_db.RegisterMessage(ReportDoneOutRequest)

ReportDoneInRequest = _reflection.GeneratedProtocolMessageType('ReportDoneInRequest', (_message.Message,), {
  'DESCRIPTOR' : _REPORTDONEINREQUEST,
  '__module__' : 'wareshuttle_pb2'
  # @@protoc_insertion_point(class_scope:wareshuttle.ReportDoneInRequest)
  })
_sym_db.RegisterMessage(ReportDoneInRequest)


DESCRIPTOR._options = None
_ASSIGNFLOORRESPONSE_DATAENTRY._options = None

_WARESHUTTLE = _descriptor.ServiceDescriptor(
  name='WareShuttle',
  full_name='wareshuttle.WareShuttle',
  file=DESCRIPTOR,
  index=0,
  serialized_options=None,
  create_key=_descriptor._internal_create_key,
  serialized_start=1233,
  serialized_end=1788,
  methods=[
  _descriptor.MethodDescriptor(
    name='AssignFloor',
    full_name='wareshuttle.WareShuttle.AssignFloor',
    index=0,
    containing_service=None,
    input_type=_ASSIGNFLOORREQUEST,
    output_type=_ASSIGNFLOORRESPONSE,
    serialized_options=None,
    create_key=_descriptor._internal_create_key,
  ),
  _descriptor.MethodDescriptor(
    name='PreemptFloor',
    full_name='wareshuttle.WareShuttle.PreemptFloor',
    index=1,
    containing_service=None,
    input_type=_PREEMPTFLOORREQUEST,
    output_type=common__pb2._COMMONRESPONSE,
    serialized_options=None,
    create_key=_descriptor._internal_create_key,
  ),
  _descriptor.MethodDescriptor(
    name='ReleaseFloor',
    full_name='wareshuttle.WareShuttle.ReleaseFloor',
    index=2,
    containing_service=None,
    input_type=_RELEASEFLOORREQUEST,
    output_type=common__pb2._COMMONRESPONSE,
    serialized_options=None,
    create_key=_descriptor._internal_create_key,
  ),
  _descriptor.MethodDescriptor(
    name='ReportFloor',
    full_name='wareshuttle.WareShuttle.ReportFloor',
    index=3,
    containing_service=None,
    input_type=_REPORTFLOORREQUEST,
    output_type=common__pb2._COMMONRESPONSE,
    serialized_options=None,
    create_key=_descriptor._internal_create_key,
  ),
  _descriptor.MethodDescriptor(
    name='TriggerTakeIn',
    full_name='wareshuttle.WareShuttle.TriggerTakeIn',
    index=4,
    containing_service=None,
    input_type=_TRIGGERTAKEINREQUEST,
    output_type=common__pb2._COMMONRESPONSE,
    serialized_options=None,
    create_key=_descriptor._internal_create_key,
  ),
  _descriptor.MethodDescriptor(
    name='ReportDoneOut',
    full_name='wareshuttle.WareShuttle.ReportDoneOut',
    index=5,
    containing_service=None,
    input_type=_REPORTDONEOUTREQUEST,
    output_type=common__pb2._COMMONRESPONSE,
    serialized_options=None,
    create_key=_descriptor._internal_create_key,
  ),
  _descriptor.MethodDescriptor(
    name='ReportDoneIn',
    full_name='wareshuttle.WareShuttle.ReportDoneIn',
    index=6,
    containing_service=None,
    input_type=_REPORTDONEINREQUEST,
    output_type=common__pb2._COMMONRESPONSE,
    serialized_options=None,
    create_key=_descriptor._internal_create_key,
  ),
])
_sym_db.RegisterServiceDescriptor(_WARESHUTTLE)

DESCRIPTOR.services_by_name['WareShuttle'] = _WARESHUTTLE

# @@protoc_insertion_point(module_scope)
