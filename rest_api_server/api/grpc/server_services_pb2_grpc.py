# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
"""Client and server classes corresponding to protobuf-defined services."""
import grpc
import warnings

import api.grpc.server_services_pb2 as server__services__pb2

GRPC_GENERATED_VERSION = '1.68.0'
GRPC_VERSION = grpc.__version__
_version_not_supported = False

try:
    from grpc._utilities import first_version_is_lower
    _version_not_supported = first_version_is_lower(GRPC_VERSION, GRPC_GENERATED_VERSION)
except ImportError:
    _version_not_supported = True

if _version_not_supported:
    raise RuntimeError(
        f'The grpc package installed is at version {GRPC_VERSION},'
        + f' but the generated code in server_services_pb2_grpc.py depends on'
        + f' grpcio>={GRPC_GENERATED_VERSION}.'
        + f' Please upgrade your grpc module to grpcio>={GRPC_GENERATED_VERSION}'
        + f' or downgrade your generated code using grpcio-tools<={GRPC_VERSION}.'
    )


class SendFileServiceStub(object):
    """Service definition
    """

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.SendFile = channel.unary_unary(
                '/server_services.SendFileService/SendFile',
                request_serializer=server__services__pb2.SendFileRequestBody.SerializeToString,
                response_deserializer=server__services__pb2.SendFileResponseBody.FromString,
                _registered_method=True)


class SendFileServiceServicer(object):
    """Service definition
    """

    def SendFile(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')


def add_SendFileServiceServicer_to_server(servicer, server):
    rpc_method_handlers = {
            'SendFile': grpc.unary_unary_rpc_method_handler(
                    servicer.SendFile,
                    request_deserializer=server__services__pb2.SendFileRequestBody.FromString,
                    response_serializer=server__services__pb2.SendFileResponseBody.SerializeToString,
            ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
            'server_services.SendFileService', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))
    server.add_registered_method_handlers('server_services.SendFileService', rpc_method_handlers)


 # This class is part of an EXPERIMENTAL API.
class SendFileService(object):
    """Service definition
    """

    @staticmethod
    def SendFile(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(
            request,
            target,
            '/server_services.SendFileService/SendFile',
            server__services__pb2.SendFileRequestBody.SerializeToString,
            server__services__pb2.SendFileResponseBody.FromString,
            options,
            channel_credentials,
            insecure,
            call_credentials,
            compression,
            wait_for_ready,
            timeout,
            metadata,
            _registered_method=True)
