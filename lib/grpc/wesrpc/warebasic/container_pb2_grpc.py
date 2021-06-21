# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
"""Client and server classes corresponding to protobuf-defined services."""
import grpc

from ..common import common_pb2 as common__pb2
from ..common import container_pb2 as container__pb2


class ContainerServiceStub(object):
    """Missing associated documentation comment in .proto file."""

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.AddContainer = channel.unary_unary(
                '/warebasic.ContainerService/AddContainer',
                request_serializer=container__pb2.AddContainerRequest.SerializeToString,
                response_deserializer=common__pb2.CommonResponse.FromString,
                )
        self.QueryContainerList = channel.unary_unary(
                '/warebasic.ContainerService/QueryContainerList',
                request_serializer=container__pb2.QueryContainerListRequest.SerializeToString,
                response_deserializer=container__pb2.QueryContainerListResponse.FromString,
                )
        self.QueryContainerDetail = channel.unary_unary(
                '/warebasic.ContainerService/QueryContainerDetail',
                request_serializer=container__pb2.QueryContainerDetailRequest.SerializeToString,
                response_deserializer=container__pb2.QueryContainerDetailResponse.FromString,
                )
        self.DeleteContainer = channel.unary_unary(
                '/warebasic.ContainerService/DeleteContainer',
                request_serializer=container__pb2.DeleteContainerRequest.SerializeToString,
                response_deserializer=common__pb2.CommonResponse.FromString,
                )


class ContainerServiceServicer(object):
    """Missing associated documentation comment in .proto file."""

    def AddContainer(self, request, context):
        """新增容器
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def QueryContainerList(self, request, context):
        """查询容器列表
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def QueryContainerDetail(self, request, context):
        """查询容器详情
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def DeleteContainer(self, request, context):
        """删除容器
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')


def add_ContainerServiceServicer_to_server(servicer, server):
    rpc_method_handlers = {
            'AddContainer': grpc.unary_unary_rpc_method_handler(
                    servicer.AddContainer,
                    request_deserializer=container__pb2.AddContainerRequest.FromString,
                    response_serializer=common__pb2.CommonResponse.SerializeToString,
            ),
            'QueryContainerList': grpc.unary_unary_rpc_method_handler(
                    servicer.QueryContainerList,
                    request_deserializer=container__pb2.QueryContainerListRequest.FromString,
                    response_serializer=container__pb2.QueryContainerListResponse.SerializeToString,
            ),
            'QueryContainerDetail': grpc.unary_unary_rpc_method_handler(
                    servicer.QueryContainerDetail,
                    request_deserializer=container__pb2.QueryContainerDetailRequest.FromString,
                    response_serializer=container__pb2.QueryContainerDetailResponse.SerializeToString,
            ),
            'DeleteContainer': grpc.unary_unary_rpc_method_handler(
                    servicer.DeleteContainer,
                    request_deserializer=container__pb2.DeleteContainerRequest.FromString,
                    response_serializer=common__pb2.CommonResponse.SerializeToString,
            ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
            'warebasic.ContainerService', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))


 # This class is part of an EXPERIMENTAL API.
class ContainerService(object):
    """Missing associated documentation comment in .proto file."""

    @staticmethod
    def AddContainer(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/warebasic.ContainerService/AddContainer',
            container__pb2.AddContainerRequest.SerializeToString,
            common__pb2.CommonResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def QueryContainerList(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/warebasic.ContainerService/QueryContainerList',
            container__pb2.QueryContainerListRequest.SerializeToString,
            container__pb2.QueryContainerListResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def QueryContainerDetail(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/warebasic.ContainerService/QueryContainerDetail',
            container__pb2.QueryContainerDetailRequest.SerializeToString,
            container__pb2.QueryContainerDetailResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def DeleteContainer(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/warebasic.ContainerService/DeleteContainer',
            container__pb2.DeleteContainerRequest.SerializeToString,
            common__pb2.CommonResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)