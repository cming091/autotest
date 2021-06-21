# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
"""Client and server classes corresponding to protobuf-defined services."""
import grpc

from  ..common import common_pb2 as common__pb2
from  . import wareshuttle_pb2 as wareshuttle__pb2


class WareShuttleStub(object):
    """ProcessFlowEngine engine message channel
    """

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.AssignFloor = channel.unary_unary(
                '/wareshuttle.WareShuttle/AssignFloor',
                request_serializer=wareshuttle__pb2.AssignFloorRequest.SerializeToString,
                response_deserializer=wareshuttle__pb2.AssignFloorResponse.FromString,
                )
        self.PreemptFloor = channel.unary_unary(
                '/wareshuttle.WareShuttle/PreemptFloor',
                request_serializer=wareshuttle__pb2.PreemptFloorRequest.SerializeToString,
                response_deserializer=common__pb2.CommonResponse.FromString,
                )
        self.ReleaseFloor = channel.unary_unary(
                '/wareshuttle.WareShuttle/ReleaseFloor',
                request_serializer=wareshuttle__pb2.ReleaseFloorRequest.SerializeToString,
                response_deserializer=common__pb2.CommonResponse.FromString,
                )
        self.ReportFloor = channel.unary_unary(
                '/wareshuttle.WareShuttle/ReportFloor',
                request_serializer=wareshuttle__pb2.ReportFloorRequest.SerializeToString,
                response_deserializer=common__pb2.CommonResponse.FromString,
                )
        self.TriggerTakeIn = channel.unary_unary(
                '/wareshuttle.WareShuttle/TriggerTakeIn',
                request_serializer=wareshuttle__pb2.TriggerTakeInRequest.SerializeToString,
                response_deserializer=common__pb2.CommonResponse.FromString,
                )
        self.ReportDoneOut = channel.unary_unary(
                '/wareshuttle.WareShuttle/ReportDoneOut',
                request_serializer=wareshuttle__pb2.ReportDoneOutRequest.SerializeToString,
                response_deserializer=common__pb2.CommonResponse.FromString,
                )
        self.ReportDoneIn = channel.unary_unary(
                '/wareshuttle.WareShuttle/ReportDoneIn',
                request_serializer=wareshuttle__pb2.ReportDoneInRequest.SerializeToString,
                response_deserializer=common__pb2.CommonResponse.FromString,
                )


class WareShuttleServicer(object):
    """ProcessFlowEngine engine message channel
    """

    def AssignFloor(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def PreemptFloor(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def ReleaseFloor(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def ReportFloor(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def TriggerTakeIn(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def ReportDoneOut(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def ReportDoneIn(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')


def add_WareShuttleServicer_to_server(servicer, server):
    rpc_method_handlers = {
            'AssignFloor': grpc.unary_unary_rpc_method_handler(
                    servicer.AssignFloor,
                    request_deserializer=wareshuttle__pb2.AssignFloorRequest.FromString,
                    response_serializer=wareshuttle__pb2.AssignFloorResponse.SerializeToString,
            ),
            'PreemptFloor': grpc.unary_unary_rpc_method_handler(
                    servicer.PreemptFloor,
                    request_deserializer=wareshuttle__pb2.PreemptFloorRequest.FromString,
                    response_serializer=common__pb2.CommonResponse.SerializeToString,
            ),
            'ReleaseFloor': grpc.unary_unary_rpc_method_handler(
                    servicer.ReleaseFloor,
                    request_deserializer=wareshuttle__pb2.ReleaseFloorRequest.FromString,
                    response_serializer=common__pb2.CommonResponse.SerializeToString,
            ),
            'ReportFloor': grpc.unary_unary_rpc_method_handler(
                    servicer.ReportFloor,
                    request_deserializer=wareshuttle__pb2.ReportFloorRequest.FromString,
                    response_serializer=common__pb2.CommonResponse.SerializeToString,
            ),
            'TriggerTakeIn': grpc.unary_unary_rpc_method_handler(
                    servicer.TriggerTakeIn,
                    request_deserializer=wareshuttle__pb2.TriggerTakeInRequest.FromString,
                    response_serializer=common__pb2.CommonResponse.SerializeToString,
            ),
            'ReportDoneOut': grpc.unary_unary_rpc_method_handler(
                    servicer.ReportDoneOut,
                    request_deserializer=wareshuttle__pb2.ReportDoneOutRequest.FromString,
                    response_serializer=common__pb2.CommonResponse.SerializeToString,
            ),
            'ReportDoneIn': grpc.unary_unary_rpc_method_handler(
                    servicer.ReportDoneIn,
                    request_deserializer=wareshuttle__pb2.ReportDoneInRequest.FromString,
                    response_serializer=common__pb2.CommonResponse.SerializeToString,
            ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
            'wareshuttle.WareShuttle', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))


 # This class is part of an EXPERIMENTAL API.
class WareShuttle(object):
    """ProcessFlowEngine engine message channel
    """

    @staticmethod
    def AssignFloor(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/wareshuttle.WareShuttle/AssignFloor',
            wareshuttle__pb2.AssignFloorRequest.SerializeToString,
            wareshuttle__pb2.AssignFloorResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def PreemptFloor(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/wareshuttle.WareShuttle/PreemptFloor',
            wareshuttle__pb2.PreemptFloorRequest.SerializeToString,
            common__pb2.CommonResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def ReleaseFloor(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/wareshuttle.WareShuttle/ReleaseFloor',
            wareshuttle__pb2.ReleaseFloorRequest.SerializeToString,
            common__pb2.CommonResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def ReportFloor(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/wareshuttle.WareShuttle/ReportFloor',
            wareshuttle__pb2.ReportFloorRequest.SerializeToString,
            common__pb2.CommonResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def TriggerTakeIn(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/wareshuttle.WareShuttle/TriggerTakeIn',
            wareshuttle__pb2.TriggerTakeInRequest.SerializeToString,
            common__pb2.CommonResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def ReportDoneOut(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/wareshuttle.WareShuttle/ReportDoneOut',
            wareshuttle__pb2.ReportDoneOutRequest.SerializeToString,
            common__pb2.CommonResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def ReportDoneIn(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/wareshuttle.WareShuttle/ReportDoneIn',
            wareshuttle__pb2.ReportDoneInRequest.SerializeToString,
            common__pb2.CommonResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)