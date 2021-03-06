# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
"""Client and server classes corresponding to protobuf-defined services."""
import grpc

from ..common import common_pb2 as common__pb2
from ..common import sku_pb2 as sku__pb2


class SkuServiceStub(object):
    """Missing associated documentation comment in .proto file."""

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.AddSku = channel.unary_unary(
                '/warebasic.SkuService/AddSku',
                request_serializer=sku__pb2.AddSkuRequest.SerializeToString,
                response_deserializer=common__pb2.CommonResponse.FromString,
                )
        self.QuerySkuList = channel.unary_unary(
                '/warebasic.SkuService/QuerySkuList',
                request_serializer=sku__pb2.QuerySkuListRequest.SerializeToString,
                response_deserializer=sku__pb2.QuerySkuListResponse.FromString,
                )
        self.QuerySkuDetail = channel.unary_unary(
                '/warebasic.SkuService/QuerySkuDetail',
                request_serializer=sku__pb2.QuerySkuDetailRequest.SerializeToString,
                response_deserializer=sku__pb2.QuerySkuDetailResponse.FromString,
                )
        self.UpdateSku = channel.unary_unary(
                '/warebasic.SkuService/UpdateSku',
                request_serializer=sku__pb2.UpdateSkuRequest.SerializeToString,
                response_deserializer=common__pb2.CommonResponse.FromString,
                )
        self.CheckSkuPackage = channel.unary_unary(
                '/warebasic.SkuService/CheckSkuPackage',
                request_serializer=sku__pb2.CheckSkuPackageRequest.SerializeToString,
                response_deserializer=sku__pb2.CheckSkuPackageResponse.FromString,
                )
        self.UpdateSkuPackage = channel.unary_unary(
                '/warebasic.SkuService/UpdateSkuPackage',
                request_serializer=sku__pb2.UpdateSkuPackageRequest.SerializeToString,
                response_deserializer=common__pb2.CommonResponse.FromString,
                )
        self.DeleteSku = channel.unary_unary(
                '/warebasic.SkuService/DeleteSku',
                request_serializer=sku__pb2.DeleteSkuRequest.SerializeToString,
                response_deserializer=common__pb2.CommonResponse.FromString,
                )


class SkuServiceServicer(object):
    """Missing associated documentation comment in .proto file."""

    def AddSku(self, request, context):
        """??????SKU
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def QuerySkuList(self, request, context):
        """??????SKU??????
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def QuerySkuDetail(self, request, context):
        """??????SKU??????
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def UpdateSku(self, request, context):
        """??????SKU??????
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def CheckSkuPackage(self, request, context):
        """??????SKU????????????
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def UpdateSkuPackage(self, request, context):
        """??????SKU????????????
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def DeleteSku(self, request, context):
        """??????SKU
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')


def add_SkuServiceServicer_to_server(servicer, server):
    rpc_method_handlers = {
            'AddSku': grpc.unary_unary_rpc_method_handler(
                    servicer.AddSku,
                    request_deserializer=sku__pb2.AddSkuRequest.FromString,
                    response_serializer=common__pb2.CommonResponse.SerializeToString,
            ),
            'QuerySkuList': grpc.unary_unary_rpc_method_handler(
                    servicer.QuerySkuList,
                    request_deserializer=sku__pb2.QuerySkuListRequest.FromString,
                    response_serializer=sku__pb2.QuerySkuListResponse.SerializeToString,
            ),
            'QuerySkuDetail': grpc.unary_unary_rpc_method_handler(
                    servicer.QuerySkuDetail,
                    request_deserializer=sku__pb2.QuerySkuDetailRequest.FromString,
                    response_serializer=sku__pb2.QuerySkuDetailResponse.SerializeToString,
            ),
            'UpdateSku': grpc.unary_unary_rpc_method_handler(
                    servicer.UpdateSku,
                    request_deserializer=sku__pb2.UpdateSkuRequest.FromString,
                    response_serializer=common__pb2.CommonResponse.SerializeToString,
            ),
            'CheckSkuPackage': grpc.unary_unary_rpc_method_handler(
                    servicer.CheckSkuPackage,
                    request_deserializer=sku__pb2.CheckSkuPackageRequest.FromString,
                    response_serializer=sku__pb2.CheckSkuPackageResponse.SerializeToString,
            ),
            'UpdateSkuPackage': grpc.unary_unary_rpc_method_handler(
                    servicer.UpdateSkuPackage,
                    request_deserializer=sku__pb2.UpdateSkuPackageRequest.FromString,
                    response_serializer=common__pb2.CommonResponse.SerializeToString,
            ),
            'DeleteSku': grpc.unary_unary_rpc_method_handler(
                    servicer.DeleteSku,
                    request_deserializer=sku__pb2.DeleteSkuRequest.FromString,
                    response_serializer=common__pb2.CommonResponse.SerializeToString,
            ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
            'warebasic.SkuService', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))


 # This class is part of an EXPERIMENTAL API.
class SkuService(object):
    """Missing associated documentation comment in .proto file."""

    @staticmethod
    def AddSku(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/warebasic.SkuService/AddSku',
            sku__pb2.AddSkuRequest.SerializeToString,
            common__pb2.CommonResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def QuerySkuList(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/warebasic.SkuService/QuerySkuList',
            sku__pb2.QuerySkuListRequest.SerializeToString,
            sku__pb2.QuerySkuListResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def QuerySkuDetail(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/warebasic.SkuService/QuerySkuDetail',
            sku__pb2.QuerySkuDetailRequest.SerializeToString,
            sku__pb2.QuerySkuDetailResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def UpdateSku(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/warebasic.SkuService/UpdateSku',
            sku__pb2.UpdateSkuRequest.SerializeToString,
            common__pb2.CommonResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def CheckSkuPackage(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/warebasic.SkuService/CheckSkuPackage',
            sku__pb2.CheckSkuPackageRequest.SerializeToString,
            sku__pb2.CheckSkuPackageResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def UpdateSkuPackage(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/warebasic.SkuService/UpdateSkuPackage',
            sku__pb2.UpdateSkuPackageRequest.SerializeToString,
            common__pb2.CommonResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def DeleteSku(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/warebasic.SkuService/DeleteSku',
            sku__pb2.DeleteSkuRequest.SerializeToString,
            common__pb2.CommonResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)
