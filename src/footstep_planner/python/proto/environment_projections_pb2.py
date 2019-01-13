# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: environment_projections.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
from google.protobuf import descriptor_pb2
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor.FileDescriptor(
  name='environment_projections.proto',
  package='footstep_planner.environment.proto',
  syntax='proto2',
  serialized_pb=_b('\n\x1d\x65nvironment_projections.proto\x12\"footstep_planner.environment.proto\"L\n\x10WorkspaceIndices\x12\x1b\n\x13lower_workspace_idx\x18\x01 \x01(\r\x12\x1b\n\x13upper_workspace_idx\x18\x02 \x01(\r\"\x8e\x02\n\x15\x45nvironmentProjection\x12T\n\x04\x64\x61ta\x18\x01 \x03(\x0e\x32\x42.footstep_planner.environment.proto.EnvironmentProjection.CellTypeB\x02\x10\x01\x12&\n\x1aworkspace_2d_to_surface_3d\x18\x02 \x03(\rB\x02\x10\x01\"w\n\x08\x43\x65llType\x12\x1d\n\x19OUTER_WORKSPACE_AREA_CELL\x10\x01\x12\r\n\tFREE_CELL\x10\x02\x12\r\n\tGATE_CELL\x10\x03\x12\x11\n\rOBSTACLE_CELL\x10\x04\x12\x1b\n\x17WORKSPACE_BOUNDARY_CELL\x10\x05\"\xa3\x02\n\x16\x45nvironmentProjections\x12\x0c\n\x04rows\x18\x01 \x02(\r\x12\x0c\n\x04\x63ols\x18\x02 \x02(\r\x12N\n\x0bprojections\x18\x03 \x03(\x0b\x32\x39.footstep_planner.environment.proto.EnvironmentProjection\x12S\n\x15surface_3d_to_indices\x18\x04 \x03(\x0b\x32\x34.footstep_planner.environment.proto.WorkspaceIndices\x12\x1e\n\x12workspace_3d_to_2d\x18\x05 \x03(\rB\x02\x10\x01\x12(\n\x1csurface_3d_to_stepping_cells\x18\x06 \x03(\rB\x02\x10\x01\"/\n\x12ValidSteppingCells\x12\x19\n\rstepping_cell\x18\x01 \x03(\x08\x42\x02\x10\x01')
)



_ENVIRONMENTPROJECTION_CELLTYPE = _descriptor.EnumDescriptor(
  name='CellType',
  full_name='footstep_planner.environment.proto.EnvironmentProjection.CellType',
  filename=None,
  file=DESCRIPTOR,
  values=[
    _descriptor.EnumValueDescriptor(
      name='OUTER_WORKSPACE_AREA_CELL', index=0, number=1,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='FREE_CELL', index=1, number=2,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='GATE_CELL', index=2, number=3,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='OBSTACLE_CELL', index=3, number=4,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='WORKSPACE_BOUNDARY_CELL', index=4, number=5,
      options=None,
      type=None),
  ],
  containing_type=None,
  options=None,
  serialized_start=299,
  serialized_end=418,
)
_sym_db.RegisterEnumDescriptor(_ENVIRONMENTPROJECTION_CELLTYPE)


_WORKSPACEINDICES = _descriptor.Descriptor(
  name='WorkspaceIndices',
  full_name='footstep_planner.environment.proto.WorkspaceIndices',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='lower_workspace_idx', full_name='footstep_planner.environment.proto.WorkspaceIndices.lower_workspace_idx', index=0,
      number=1, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='upper_workspace_idx', full_name='footstep_planner.environment.proto.WorkspaceIndices.upper_workspace_idx', index=1,
      number=2, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
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
  syntax='proto2',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=69,
  serialized_end=145,
)


_ENVIRONMENTPROJECTION = _descriptor.Descriptor(
  name='EnvironmentProjection',
  full_name='footstep_planner.environment.proto.EnvironmentProjection',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='data', full_name='footstep_planner.environment.proto.EnvironmentProjection.data', index=0,
      number=1, type=14, cpp_type=8, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=_descriptor._ParseOptions(descriptor_pb2.FieldOptions(), _b('\020\001')), file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='workspace_2d_to_surface_3d', full_name='footstep_planner.environment.proto.EnvironmentProjection.workspace_2d_to_surface_3d', index=1,
      number=2, type=13, cpp_type=3, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=_descriptor._ParseOptions(descriptor_pb2.FieldOptions(), _b('\020\001')), file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
    _ENVIRONMENTPROJECTION_CELLTYPE,
  ],
  options=None,
  is_extendable=False,
  syntax='proto2',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=148,
  serialized_end=418,
)


_ENVIRONMENTPROJECTIONS = _descriptor.Descriptor(
  name='EnvironmentProjections',
  full_name='footstep_planner.environment.proto.EnvironmentProjections',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='rows', full_name='footstep_planner.environment.proto.EnvironmentProjections.rows', index=0,
      number=1, type=13, cpp_type=3, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='cols', full_name='footstep_planner.environment.proto.EnvironmentProjections.cols', index=1,
      number=2, type=13, cpp_type=3, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='projections', full_name='footstep_planner.environment.proto.EnvironmentProjections.projections', index=2,
      number=3, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='surface_3d_to_indices', full_name='footstep_planner.environment.proto.EnvironmentProjections.surface_3d_to_indices', index=3,
      number=4, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='workspace_3d_to_2d', full_name='footstep_planner.environment.proto.EnvironmentProjections.workspace_3d_to_2d', index=4,
      number=5, type=13, cpp_type=3, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=_descriptor._ParseOptions(descriptor_pb2.FieldOptions(), _b('\020\001')), file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='surface_3d_to_stepping_cells', full_name='footstep_planner.environment.proto.EnvironmentProjections.surface_3d_to_stepping_cells', index=5,
      number=6, type=13, cpp_type=3, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=_descriptor._ParseOptions(descriptor_pb2.FieldOptions(), _b('\020\001')), file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  syntax='proto2',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=421,
  serialized_end=712,
)


_VALIDSTEPPINGCELLS = _descriptor.Descriptor(
  name='ValidSteppingCells',
  full_name='footstep_planner.environment.proto.ValidSteppingCells',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='stepping_cell', full_name='footstep_planner.environment.proto.ValidSteppingCells.stepping_cell', index=0,
      number=1, type=8, cpp_type=7, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=_descriptor._ParseOptions(descriptor_pb2.FieldOptions(), _b('\020\001')), file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  syntax='proto2',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=714,
  serialized_end=761,
)

_ENVIRONMENTPROJECTION.fields_by_name['data'].enum_type = _ENVIRONMENTPROJECTION_CELLTYPE
_ENVIRONMENTPROJECTION_CELLTYPE.containing_type = _ENVIRONMENTPROJECTION
_ENVIRONMENTPROJECTIONS.fields_by_name['projections'].message_type = _ENVIRONMENTPROJECTION
_ENVIRONMENTPROJECTIONS.fields_by_name['surface_3d_to_indices'].message_type = _WORKSPACEINDICES
DESCRIPTOR.message_types_by_name['WorkspaceIndices'] = _WORKSPACEINDICES
DESCRIPTOR.message_types_by_name['EnvironmentProjection'] = _ENVIRONMENTPROJECTION
DESCRIPTOR.message_types_by_name['EnvironmentProjections'] = _ENVIRONMENTPROJECTIONS
DESCRIPTOR.message_types_by_name['ValidSteppingCells'] = _VALIDSTEPPINGCELLS
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

WorkspaceIndices = _reflection.GeneratedProtocolMessageType('WorkspaceIndices', (_message.Message,), dict(
  DESCRIPTOR = _WORKSPACEINDICES,
  __module__ = 'environment_projections_pb2'
  # @@protoc_insertion_point(class_scope:footstep_planner.environment.proto.WorkspaceIndices)
  ))
_sym_db.RegisterMessage(WorkspaceIndices)

EnvironmentProjection = _reflection.GeneratedProtocolMessageType('EnvironmentProjection', (_message.Message,), dict(
  DESCRIPTOR = _ENVIRONMENTPROJECTION,
  __module__ = 'environment_projections_pb2'
  # @@protoc_insertion_point(class_scope:footstep_planner.environment.proto.EnvironmentProjection)
  ))
_sym_db.RegisterMessage(EnvironmentProjection)

EnvironmentProjections = _reflection.GeneratedProtocolMessageType('EnvironmentProjections', (_message.Message,), dict(
  DESCRIPTOR = _ENVIRONMENTPROJECTIONS,
  __module__ = 'environment_projections_pb2'
  # @@protoc_insertion_point(class_scope:footstep_planner.environment.proto.EnvironmentProjections)
  ))
_sym_db.RegisterMessage(EnvironmentProjections)

ValidSteppingCells = _reflection.GeneratedProtocolMessageType('ValidSteppingCells', (_message.Message,), dict(
  DESCRIPTOR = _VALIDSTEPPINGCELLS,
  __module__ = 'environment_projections_pb2'
  # @@protoc_insertion_point(class_scope:footstep_planner.environment.proto.ValidSteppingCells)
  ))
_sym_db.RegisterMessage(ValidSteppingCells)


_ENVIRONMENTPROJECTION.fields_by_name['data'].has_options = True
_ENVIRONMENTPROJECTION.fields_by_name['data']._options = _descriptor._ParseOptions(descriptor_pb2.FieldOptions(), _b('\020\001'))
_ENVIRONMENTPROJECTION.fields_by_name['workspace_2d_to_surface_3d'].has_options = True
_ENVIRONMENTPROJECTION.fields_by_name['workspace_2d_to_surface_3d']._options = _descriptor._ParseOptions(descriptor_pb2.FieldOptions(), _b('\020\001'))
_ENVIRONMENTPROJECTIONS.fields_by_name['workspace_3d_to_2d'].has_options = True
_ENVIRONMENTPROJECTIONS.fields_by_name['workspace_3d_to_2d']._options = _descriptor._ParseOptions(descriptor_pb2.FieldOptions(), _b('\020\001'))
_ENVIRONMENTPROJECTIONS.fields_by_name['surface_3d_to_stepping_cells'].has_options = True
_ENVIRONMENTPROJECTIONS.fields_by_name['surface_3d_to_stepping_cells']._options = _descriptor._ParseOptions(descriptor_pb2.FieldOptions(), _b('\020\001'))
_VALIDSTEPPINGCELLS.fields_by_name['stepping_cell'].has_options = True
_VALIDSTEPPINGCELLS.fields_by_name['stepping_cell']._options = _descriptor._ParseOptions(descriptor_pb2.FieldOptions(), _b('\020\001'))
# @@protoc_insertion_point(module_scope)
