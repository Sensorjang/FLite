# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: tracking_service.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database

# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


import FLite.protobuf.common_pb2 as common__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(
    b'\n\x16tracking_service.proto\x12\x0e\x46Lite.protobuf\x1a\x0c\x63ommon.proto"I\n\x16TrackTaskMetricRequest\x12/\n\x0btask_metric\x18\x01 \x01(\x0b\x32\x1a.FLite.protobuf.TaskMetric"A\n\x17TrackTaskMetricResponse\x12&\n\x06status\x18\x01 \x01(\x0b\x32\x16.FLite.protobuf.Status"L\n\x17TrackRoundMetricRequest\x12\x31\n\x0cround_metric\x18\x01 \x01(\x0b\x32\x1b.FLite.protobuf.RoundMetric"B\n\x18TrackRoundMetricResponse\x12&\n\x06status\x18\x01 \x01(\x0b\x32\x16.FLite.protobuf.Status"P\n\x18TrackClientMetricRequest\x12\x34\n\x0e\x63lient_metrics\x18\x01 \x03(\x0b\x32\x1c.FLite.protobuf.ClientMetric"C\n\x19TrackClientMetricResponse\x12&\n\x06status\x18\x01 \x01(\x0b\x32\x16.FLite.protobuf.Status"\xd0\x01\n\x1dTrackClientTrainMetricRequest\x12\x0f\n\x07task_id\x18\x01 \x01(\t\x12\x10\n\x08round_id\x18\x02 \x01(\x05\x12\x11\n\tclient_id\x18\x03 \x01(\t\x12\x12\n\ntrain_loss\x18\x04 \x03(\x02\x12\x12\n\ntrain_time\x18\x05 \x01(\x02\x12\x19\n\x11train_upload_time\x18\x06 \x01(\x02\x12\x1b\n\x13train_download_size\x18\x07 \x01(\x02\x12\x19\n\x11train_upload_size\x18\x08 \x01(\x02"H\n\x1eTrackClientTrainMetricResponse\x12&\n\x06status\x18\x01 \x01(\x0b\x32\x16.FLite.protobuf.Status"\xc7\x01\n\x1cTrackClientTestMetricRequest\x12\x0f\n\x07task_id\x18\x01 \x01(\t\x12\x10\n\x08round_id\x18\x02 \x01(\x05\x12\x11\n\tclient_id\x18\x03 \x01(\t\x12\x15\n\rtest_accuracy\x18\x04 \x01(\x02\x12\x11\n\ttest_loss\x18\x05 \x01(\x02\x12\x11\n\ttest_time\x18\x06 \x01(\x02\x12\x18\n\x10test_upload_time\x18\x07 \x01(\x02\x12\x1a\n\x12test_download_size\x18\x08 \x01(\x02"G\n\x1dTrackClientTestMetricResponse\x12&\n\x06status\x18\x01 \x01(\x0b\x32\x16.FLite.protobuf.Status"Q\n\x1cGetRoundTrainTestTimeRequest\x12\x0f\n\x07task_id\x18\x01 \x01(\t\x12\x0e\n\x06rounds\x18\x02 \x01(\x05\x12\x10\n\x08interval\x18\x03 \x01(\x05"/\n\rTrainTestTime\x12\x10\n\x08round_id\x18\x01 \x01(\x05\x12\x0c\n\x04time\x18\x02 \x01(\x02"\x80\x01\n\x1dGetRoundTrainTestTimeResponse\x12\x37\n\x10train_test_times\x18\x01 \x03(\x0b\x32\x1d.FLite.protobuf.TrainTestTime\x12&\n\x06status\x18\x02 \x01(\x0b\x32\x16.FLite.protobuf.Status"9\n\x16GetRoundMetricsRequest\x12\x0f\n\x07task_id\x18\x01 \x01(\t\x12\x0e\n\x06rounds\x18\x02 \x03(\x05"\x92\x01\n\x17GetRoundMetricsResponse\x12\x0f\n\x07task_id\x18\x01 \x01(\t\x12\x10\n\x08round_id\x18\x02 \x01(\x05\x12,\n\x07metrics\x18\x03 \x03(\x0b\x32\x1b.FLite.protobuf.RoundMetric\x12&\n\x06status\x18\x04 \x01(\x0b\x32\x16.FLite.protobuf.Status"P\n\x17GetClientMetricsRequest\x12\x0f\n\x07task_id\x18\x01 \x01(\t\x12\x10\n\x08round_id\x18\x02 \x01(\x05\x12\x12\n\nclient_ids\x18\x03 \x03(\t"\x94\x01\n\x18GetClientMetricsResponse\x12\x0f\n\x07task_id\x18\x01 \x01(\t\x12\x10\n\x08round_id\x18\x02 \x01(\x05\x12-\n\x07metrics\x18\x03 \x03(\x0b\x32\x1c.FLite.protobuf.ClientMetric\x12&\n\x06status\x18\x04 \x01(\x0b\x32\x16.FLite.protobuf.Status2\x86\x07\n\x0fTrackingService\x12\x64\n\x0fTrackTaskMetric\x12&.FLite.protobuf.TrackTaskMetricRequest\x1a\'.FLite.protobuf.TrackTaskMetricResponse"\x00\x12g\n\x10TrackRoundMetric\x12\'.FLite.protobuf.TrackRoundMetricRequest\x1a(.FLite.protobuf.TrackRoundMetricResponse"\x00\x12j\n\x11TrackClientMetric\x12(.FLite.protobuf.TrackClientMetricRequest\x1a).FLite.protobuf.TrackClientMetricResponse"\x00\x12y\n\x16TrackClientTrainMetric\x12-.FLite.protobuf.TrackClientTrainMetricRequest\x1a..FLite.protobuf.TrackClientTrainMetricResponse"\x00\x12v\n\x15TrackClientTestMetric\x12,.FLite.protobuf.TrackClientTestMetricRequest\x1a-.FLite.protobuf.TrackClientTestMetricResponse"\x00\x12\x64\n\x0fGetRoundMetrics\x12&.FLite.protobuf.GetRoundMetricsRequest\x1a\'.FLite.protobuf.GetRoundMetricsResponse"\x00\x12g\n\x10GetClientMetrics\x12\'.FLite.protobuf.GetClientMetricsRequest\x1a(.FLite.protobuf.GetClientMetricsResponse"\x00\x12v\n\x15GetRoundTrainTestTime\x12,.FLite.protobuf.GetRoundTrainTestTimeRequest\x1a-.FLite.protobuf.GetRoundTrainTestTimeResponse"\x00\x62\x06proto3'
)


_TRACKTASKMETRICREQUEST = DESCRIPTOR.message_types_by_name["TrackTaskMetricRequest"]
_TRACKTASKMETRICRESPONSE = DESCRIPTOR.message_types_by_name["TrackTaskMetricResponse"]
_TRACKROUNDMETRICREQUEST = DESCRIPTOR.message_types_by_name["TrackRoundMetricRequest"]
_TRACKROUNDMETRICRESPONSE = DESCRIPTOR.message_types_by_name["TrackRoundMetricResponse"]
_TRACKCLIENTMETRICREQUEST = DESCRIPTOR.message_types_by_name["TrackClientMetricRequest"]
_TRACKCLIENTMETRICRESPONSE = DESCRIPTOR.message_types_by_name[
    "TrackClientMetricResponse"
]
_TRACKCLIENTTRAINMETRICREQUEST = DESCRIPTOR.message_types_by_name[
    "TrackClientTrainMetricRequest"
]
_TRACKCLIENTTRAINMETRICRESPONSE = DESCRIPTOR.message_types_by_name[
    "TrackClientTrainMetricResponse"
]
_TRACKCLIENTTESTMETRICREQUEST = DESCRIPTOR.message_types_by_name[
    "TrackClientTestMetricRequest"
]
_TRACKCLIENTTESTMETRICRESPONSE = DESCRIPTOR.message_types_by_name[
    "TrackClientTestMetricResponse"
]
_GETROUNDTRAINTESTTIMEREQUEST = DESCRIPTOR.message_types_by_name[
    "GetRoundTrainTestTimeRequest"
]
_TRAINTESTTIME = DESCRIPTOR.message_types_by_name["TrainTestTime"]
_GETROUNDTRAINTESTTIMERESPONSE = DESCRIPTOR.message_types_by_name[
    "GetRoundTrainTestTimeResponse"
]
_GETROUNDMETRICSREQUEST = DESCRIPTOR.message_types_by_name["GetRoundMetricsRequest"]
_GETROUNDMETRICSRESPONSE = DESCRIPTOR.message_types_by_name["GetRoundMetricsResponse"]
_GETCLIENTMETRICSREQUEST = DESCRIPTOR.message_types_by_name["GetClientMetricsRequest"]
_GETCLIENTMETRICSRESPONSE = DESCRIPTOR.message_types_by_name["GetClientMetricsResponse"]
TrackTaskMetricRequest = _reflection.GeneratedProtocolMessageType(
    "TrackTaskMetricRequest",
    (_message.Message,),
    {
        "DESCRIPTOR": _TRACKTASKMETRICREQUEST,
        "__module__": "FLite.protobuf.tracking_service_pb2"
        # @@protoc_insertion_point(class_scope:FLite.protobuf.TrackTaskMetricRequest)
    },
)
_sym_db.RegisterMessage(TrackTaskMetricRequest)

TrackTaskMetricResponse = _reflection.GeneratedProtocolMessageType(
    "TrackTaskMetricResponse",
    (_message.Message,),
    {
        "DESCRIPTOR": _TRACKTASKMETRICRESPONSE,
        "__module__": "FLite.protobuf.tracking_service_pb2"
        # @@protoc_insertion_point(class_scope:FLite.protobuf.TrackTaskMetricResponse)
    },
)
_sym_db.RegisterMessage(TrackTaskMetricResponse)

TrackRoundMetricRequest = _reflection.GeneratedProtocolMessageType(
    "TrackRoundMetricRequest",
    (_message.Message,),
    {
        "DESCRIPTOR": _TRACKROUNDMETRICREQUEST,
        "__module__": "FLite.protobuf.tracking_service_pb2"
        # @@protoc_insertion_point(class_scope:FLite.protobuf.TrackRoundMetricRequest)
    },
)
_sym_db.RegisterMessage(TrackRoundMetricRequest)

TrackRoundMetricResponse = _reflection.GeneratedProtocolMessageType(
    "TrackRoundMetricResponse",
    (_message.Message,),
    {
        "DESCRIPTOR": _TRACKROUNDMETRICRESPONSE,
        "__module__": "FLite.protobuf.tracking_service_pb2"
        # @@protoc_insertion_point(class_scope:FLite.protobuf.TrackRoundMetricResponse)
    },
)
_sym_db.RegisterMessage(TrackRoundMetricResponse)

TrackClientMetricRequest = _reflection.GeneratedProtocolMessageType(
    "TrackClientMetricRequest",
    (_message.Message,),
    {
        "DESCRIPTOR": _TRACKCLIENTMETRICREQUEST,
        "__module__": "FLite.protobuf.tracking_service_pb2"
        # @@protoc_insertion_point(class_scope:FLite.protobuf.TrackClientMetricRequest)
    },
)
_sym_db.RegisterMessage(TrackClientMetricRequest)

TrackClientMetricResponse = _reflection.GeneratedProtocolMessageType(
    "TrackClientMetricResponse",
    (_message.Message,),
    {
        "DESCRIPTOR": _TRACKCLIENTMETRICRESPONSE,
        "__module__": "FLite.protobuf.tracking_service_pb2"
        # @@protoc_insertion_point(class_scope:FLite.protobuf.TrackClientMetricResponse)
    },
)
_sym_db.RegisterMessage(TrackClientMetricResponse)

TrackClientTrainMetricRequest = _reflection.GeneratedProtocolMessageType(
    "TrackClientTrainMetricRequest",
    (_message.Message,),
    {
        "DESCRIPTOR": _TRACKCLIENTTRAINMETRICREQUEST,
        "__module__": "FLite.protobuf.tracking_service_pb2"
        # @@protoc_insertion_point(class_scope:FLite.protobuf.TrackClientTrainMetricRequest)
    },
)
_sym_db.RegisterMessage(TrackClientTrainMetricRequest)

TrackClientTrainMetricResponse = _reflection.GeneratedProtocolMessageType(
    "TrackClientTrainMetricResponse",
    (_message.Message,),
    {
        "DESCRIPTOR": _TRACKCLIENTTRAINMETRICRESPONSE,
        "__module__": "FLite.protobuf.tracking_service_pb2"
        # @@protoc_insertion_point(class_scope:FLite.protobuf.TrackClientTrainMetricResponse)
    },
)
_sym_db.RegisterMessage(TrackClientTrainMetricResponse)

TrackClientTestMetricRequest = _reflection.GeneratedProtocolMessageType(
    "TrackClientTestMetricRequest",
    (_message.Message,),
    {
        "DESCRIPTOR": _TRACKCLIENTTESTMETRICREQUEST,
        "__module__": "FLite.protobuf.tracking_service_pb2"
        # @@protoc_insertion_point(class_scope:FLite.protobuf.TrackClientTestMetricRequest)
    },
)
_sym_db.RegisterMessage(TrackClientTestMetricRequest)

TrackClientTestMetricResponse = _reflection.GeneratedProtocolMessageType(
    "TrackClientTestMetricResponse",
    (_message.Message,),
    {
        "DESCRIPTOR": _TRACKCLIENTTESTMETRICRESPONSE,
        "__module__": "FLite.protobuf.tracking_service_pb2"
        # @@protoc_insertion_point(class_scope:FLite.protobuf.TrackClientTestMetricResponse)
    },
)
_sym_db.RegisterMessage(TrackClientTestMetricResponse)

GetRoundTrainTestTimeRequest = _reflection.GeneratedProtocolMessageType(
    "GetRoundTrainTestTimeRequest",
    (_message.Message,),
    {
        "DESCRIPTOR": _GETROUNDTRAINTESTTIMEREQUEST,
        "__module__": "FLite.protobuf.tracking_service_pb2"
        # @@protoc_insertion_point(class_scope:FLite.protobuf.GetRoundTrainTestTimeRequest)
    },
)
_sym_db.RegisterMessage(GetRoundTrainTestTimeRequest)

TrainTestTime = _reflection.GeneratedProtocolMessageType(
    "TrainTestTime",
    (_message.Message,),
    {
        "DESCRIPTOR": _TRAINTESTTIME,
        "__module__": "FLite.protobuf.tracking_service_pb2"
        # @@protoc_insertion_point(class_scope:FLite.protobuf.TrainTestTime)
    },
)
_sym_db.RegisterMessage(TrainTestTime)

GetRoundTrainTestTimeResponse = _reflection.GeneratedProtocolMessageType(
    "GetRoundTrainTestTimeResponse",
    (_message.Message,),
    {
        "DESCRIPTOR": _GETROUNDTRAINTESTTIMERESPONSE,
        "__module__": "FLite.protobuf.tracking_service_pb2"
        # @@protoc_insertion_point(class_scope:FLite.protobuf.GetRoundTrainTestTimeResponse)
    },
)
_sym_db.RegisterMessage(GetRoundTrainTestTimeResponse)

GetRoundMetricsRequest = _reflection.GeneratedProtocolMessageType(
    "GetRoundMetricsRequest",
    (_message.Message,),
    {
        "DESCRIPTOR": _GETROUNDMETRICSREQUEST,
        "__module__": "FLite.protobuf.tracking_service_pb2"
        # @@protoc_insertion_point(class_scope:FLite.protobuf.GetRoundMetricsRequest)
    },
)
_sym_db.RegisterMessage(GetRoundMetricsRequest)

GetRoundMetricsResponse = _reflection.GeneratedProtocolMessageType(
    "GetRoundMetricsResponse",
    (_message.Message,),
    {
        "DESCRIPTOR": _GETROUNDMETRICSRESPONSE,
        "__module__": "FLite.protobuf.tracking_service_pb2"
        # @@protoc_insertion_point(class_scope:FLite.protobuf.GetRoundMetricsResponse)
    },
)
_sym_db.RegisterMessage(GetRoundMetricsResponse)

GetClientMetricsRequest = _reflection.GeneratedProtocolMessageType(
    "GetClientMetricsRequest",
    (_message.Message,),
    {
        "DESCRIPTOR": _GETCLIENTMETRICSREQUEST,
        "__module__": "FLite.protobuf.tracking_service_pb2"
        # @@protoc_insertion_point(class_scope:FLite.protobuf.GetClientMetricsRequest)
    },
)
_sym_db.RegisterMessage(GetClientMetricsRequest)

GetClientMetricsResponse = _reflection.GeneratedProtocolMessageType(
    "GetClientMetricsResponse",
    (_message.Message,),
    {
        "DESCRIPTOR": _GETCLIENTMETRICSRESPONSE,
        "__module__": "FLite.protobuf.tracking_service_pb2"
        # @@protoc_insertion_point(class_scope:FLite.protobuf.GetClientMetricsResponse)
    },
)
_sym_db.RegisterMessage(GetClientMetricsResponse)

_TRACKINGSERVICE = DESCRIPTOR.services_by_name["TrackingService"]
if _descriptor._USE_C_DESCRIPTORS == False:

    DESCRIPTOR._options = None
    _TRACKTASKMETRICREQUEST._serialized_start = 71
    _TRACKTASKMETRICREQUEST._serialized_end = 139
    _TRACKTASKMETRICRESPONSE._serialized_start = 141
    _TRACKTASKMETRICRESPONSE._serialized_end = 201
    _TRACKROUNDMETRICREQUEST._serialized_start = 203
    _TRACKROUNDMETRICREQUEST._serialized_end = 274
    _TRACKROUNDMETRICRESPONSE._serialized_start = 276
    _TRACKROUNDMETRICRESPONSE._serialized_end = 337
    _TRACKCLIENTMETRICREQUEST._serialized_start = 339
    _TRACKCLIENTMETRICREQUEST._serialized_end = 414
    _TRACKCLIENTMETRICRESPONSE._serialized_start = 416
    _TRACKCLIENTMETRICRESPONSE._serialized_end = 478
    _TRACKCLIENTTRAINMETRICREQUEST._serialized_start = 481
    _TRACKCLIENTTRAINMETRICREQUEST._serialized_end = 689
    _TRACKCLIENTTRAINMETRICRESPONSE._serialized_start = 691
    _TRACKCLIENTTRAINMETRICRESPONSE._serialized_end = 758
    _TRACKCLIENTTESTMETRICREQUEST._serialized_start = 761
    _TRACKCLIENTTESTMETRICREQUEST._serialized_end = 960
    _TRACKCLIENTTESTMETRICRESPONSE._serialized_start = 962
    _TRACKCLIENTTESTMETRICRESPONSE._serialized_end = 1028
    _GETROUNDTRAINTESTTIMEREQUEST._serialized_start = 1030
    _GETROUNDTRAINTESTTIMEREQUEST._serialized_end = 1111
    _TRAINTESTTIME._serialized_start = 1113
    _TRAINTESTTIME._serialized_end = 1160
    _GETROUNDTRAINTESTTIMERESPONSE._serialized_start = 1162
    _GETROUNDTRAINTESTTIMERESPONSE._serialized_end = 1280
    _GETROUNDMETRICSREQUEST._serialized_start = 1282
    _GETROUNDMETRICSREQUEST._serialized_end = 1339
    _GETROUNDMETRICSRESPONSE._serialized_start = 1342
    _GETROUNDMETRICSRESPONSE._serialized_end = 1478
    _GETCLIENTMETRICSREQUEST._serialized_start = 1480
    _GETCLIENTMETRICSREQUEST._serialized_end = 1560
    _GETCLIENTMETRICSRESPONSE._serialized_start = 1563
    _GETCLIENTMETRICSRESPONSE._serialized_end = 1701
    _TRACKINGSERVICE._serialized_start = 1704
    _TRACKINGSERVICE._serialized_end = 2526
# @@protoc_insertion_point(module_scope)
