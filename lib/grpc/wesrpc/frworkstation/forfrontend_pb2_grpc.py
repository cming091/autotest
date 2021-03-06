# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
"""Client and server classes corresponding to protobuf-defined services."""
import grpc

from . import forfrontend_pb2 as forfrontend__pb2


class frontendStub(object):
    """Missing associated documentation comment in .proto file."""

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.CheckContainerCode = channel.unary_unary(
                '/frworkstation.frontend/CheckContainerCode',
                request_serializer=forfrontend__pb2.CheckContainerCodeRequest.SerializeToString,
                response_deserializer=forfrontend__pb2.CheckContainerCodeResponse.FromString,
                )
        self.BindContainerAndrfid = channel.unary_unary(
                '/frworkstation.frontend/BindContainerAndrfid',
                request_serializer=forfrontend__pb2.BindContainerAndrfidRequest.SerializeToString,
                response_deserializer=forfrontend__pb2.BindContainerAndrfidResponse.FromString,
                )
        self.UpdateContainerException = channel.unary_unary(
                '/frworkstation.frontend/UpdateContainerException',
                request_serializer=forfrontend__pb2.UpdateContainerExceptionRequest.SerializeToString,
                response_deserializer=forfrontend__pb2.UpdateContainerExceptionResponse.FromString,
                )
        self.ExceBindContainerAndrfid = channel.unary_unary(
                '/frworkstation.frontend/ExceBindContainerAndrfid',
                request_serializer=forfrontend__pb2.BindContainerAndrfidRequest.SerializeToString,
                response_deserializer=forfrontend__pb2.BindContainerAndrfidResponse.FromString,
                )
        self.QueryExceptionByContainerCode = channel.unary_unary(
                '/frworkstation.frontend/QueryExceptionByContainerCode',
                request_serializer=forfrontend__pb2.QueryExceptionByContainerCodeRequest.SerializeToString,
                response_deserializer=forfrontend__pb2.QueryExceptionsResponse.FromString,
                )
        self.QueryExceptionByRFidList = channel.unary_unary(
                '/frworkstation.frontend/QueryExceptionByRFidList',
                request_serializer=forfrontend__pb2.QueryExceptionByRFidListRequest.SerializeToString,
                response_deserializer=forfrontend__pb2.QueryExceptionsResponse.FromString,
                )


class frontendServicer(object):
    """Missing associated documentation comment in .proto file."""

    def CheckContainerCode(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def BindContainerAndrfid(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def UpdateContainerException(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def ExceBindContainerAndrfid(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def QueryExceptionByContainerCode(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def QueryExceptionByRFidList(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')


def add_frontendServicer_to_server(servicer, server):
    rpc_method_handlers = {
            'CheckContainerCode': grpc.unary_unary_rpc_method_handler(
                    servicer.CheckContainerCode,
                    request_deserializer=forfrontend__pb2.CheckContainerCodeRequest.FromString,
                    response_serializer=forfrontend__pb2.CheckContainerCodeResponse.SerializeToString,
            ),
            'BindContainerAndrfid': grpc.unary_unary_rpc_method_handler(
                    servicer.BindContainerAndrfid,
                    request_deserializer=forfrontend__pb2.BindContainerAndrfidRequest.FromString,
                    response_serializer=forfrontend__pb2.BindContainerAndrfidResponse.SerializeToString,
            ),
            'UpdateContainerException': grpc.unary_unary_rpc_method_handler(
                    servicer.UpdateContainerException,
                    request_deserializer=forfrontend__pb2.UpdateContainerExceptionRequest.FromString,
                    response_serializer=forfrontend__pb2.UpdateContainerExceptionResponse.SerializeToString,
            ),
            'ExceBindContainerAndrfid': grpc.unary_unary_rpc_method_handler(
                    servicer.ExceBindContainerAndrfid,
                    request_deserializer=forfrontend__pb2.BindContainerAndrfidRequest.FromString,
                    response_serializer=forfrontend__pb2.BindContainerAndrfidResponse.SerializeToString,
            ),
            'QueryExceptionByContainerCode': grpc.unary_unary_rpc_method_handler(
                    servicer.QueryExceptionByContainerCode,
                    request_deserializer=forfrontend__pb2.QueryExceptionByContainerCodeRequest.FromString,
                    response_serializer=forfrontend__pb2.QueryExceptionsResponse.SerializeToString,
            ),
            'QueryExceptionByRFidList': grpc.unary_unary_rpc_method_handler(
                    servicer.QueryExceptionByRFidList,
                    request_deserializer=forfrontend__pb2.QueryExceptionByRFidListRequest.FromString,
                    response_serializer=forfrontend__pb2.QueryExceptionsResponse.SerializeToString,
            ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
            'frworkstation.frontend', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))


 # This class is part of an EXPERIMENTAL API.
class frontend(object):
    """Missing associated documentation comment in .proto file."""

    @staticmethod
    def CheckContainerCode(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/frworkstation.frontend/CheckContainerCode',
            forfrontend__pb2.CheckContainerCodeRequest.SerializeToString,
            forfrontend__pb2.CheckContainerCodeResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def BindContainerAndrfid(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/frworkstation.frontend/BindContainerAndrfid',
            forfrontend__pb2.BindContainerAndrfidRequest.SerializeToString,
            forfrontend__pb2.BindContainerAndrfidResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def UpdateContainerException(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/frworkstation.frontend/UpdateContainerException',
            forfrontend__pb2.UpdateContainerExceptionRequest.SerializeToString,
            forfrontend__pb2.UpdateContainerExceptionResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def ExceBindContainerAndrfid(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/frworkstation.frontend/ExceBindContainerAndrfid',
            forfrontend__pb2.BindContainerAndrfidRequest.SerializeToString,
            forfrontend__pb2.BindContainerAndrfidResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def QueryExceptionByContainerCode(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/frworkstation.frontend/QueryExceptionByContainerCode',
            forfrontend__pb2.QueryExceptionByContainerCodeRequest.SerializeToString,
            forfrontend__pb2.QueryExceptionsResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def QueryExceptionByRFidList(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/frworkstation.frontend/QueryExceptionByRFidList',
            forfrontend__pb2.QueryExceptionByRFidListRequest.SerializeToString,
            forfrontend__pb2.QueryExceptionsResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)
