# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: qrldebug.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
from google.protobuf import descriptor_pb2
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


import qrl.generated.qrl_pb2 as qrl__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='qrldebug.proto',
  package='qrl',
  syntax='proto3',
  serialized_pb=_b('\n\x0eqrldebug.proto\x12\x03qrl\x1a\tqrl.proto\"\x11\n\x0fGetFullStateReq\"i\n\x10GetFullStateResp\x12)\n\x0e\x63oinbase_state\x18\x01 \x01(\x0b\x32\x11.qrl.AddressState\x12*\n\x0f\x61\x64\x64resses_state\x18\x02 \x03(\x0b\x32\x11.qrl.AddressState2G\n\x08\x44\x65\x62ugAPI\x12;\n\x0cGetFullState\x12\x14.qrl.GetFullStateReq\x1a\x15.qrl.GetFullStateRespb\x06proto3')
  ,
  dependencies=[qrl__pb2.DESCRIPTOR,])




_GETFULLSTATEREQ = _descriptor.Descriptor(
  name='GetFullStateReq',
  full_name='qrl.GetFullStateReq',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=34,
  serialized_end=51,
)


_GETFULLSTATERESP = _descriptor.Descriptor(
  name='GetFullStateResp',
  full_name='qrl.GetFullStateResp',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='coinbase_state', full_name='qrl.GetFullStateResp.coinbase_state', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='addresses_state', full_name='qrl.GetFullStateResp.addresses_state', index=1,
      number=2, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=53,
  serialized_end=158,
)

_GETFULLSTATERESP.fields_by_name['coinbase_state'].message_type = qrl__pb2._ADDRESSSTATE
_GETFULLSTATERESP.fields_by_name['addresses_state'].message_type = qrl__pb2._ADDRESSSTATE
DESCRIPTOR.message_types_by_name['GetFullStateReq'] = _GETFULLSTATEREQ
DESCRIPTOR.message_types_by_name['GetFullStateResp'] = _GETFULLSTATERESP
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

GetFullStateReq = _reflection.GeneratedProtocolMessageType('GetFullStateReq', (_message.Message,), dict(
  DESCRIPTOR = _GETFULLSTATEREQ,
  __module__ = 'qrldebug_pb2'
  # @@protoc_insertion_point(class_scope:qrl.GetFullStateReq)
  ))
_sym_db.RegisterMessage(GetFullStateReq)

GetFullStateResp = _reflection.GeneratedProtocolMessageType('GetFullStateResp', (_message.Message,), dict(
  DESCRIPTOR = _GETFULLSTATERESP,
  __module__ = 'qrldebug_pb2'
  # @@protoc_insertion_point(class_scope:qrl.GetFullStateResp)
  ))
_sym_db.RegisterMessage(GetFullStateResp)



_DEBUGAPI = _descriptor.ServiceDescriptor(
  name='DebugAPI',
  full_name='qrl.DebugAPI',
  file=DESCRIPTOR,
  index=0,
  options=None,
  serialized_start=160,
  serialized_end=231,
  methods=[
  _descriptor.MethodDescriptor(
    name='GetFullState',
    full_name='qrl.DebugAPI.GetFullState',
    index=0,
    containing_service=None,
    input_type=_GETFULLSTATEREQ,
    output_type=_GETFULLSTATERESP,
    options=None,
  ),
])
_sym_db.RegisterServiceDescriptor(_DEBUGAPI)

DESCRIPTOR.services_by_name['DebugAPI'] = _DEBUGAPI

# @@protoc_insertion_point(module_scope)
