# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
"""Client and server classes corresponding to protobuf-defined services."""
import grpc

from chirpstack_api.fuota import fuota_pb2 as chirpstack__api_dot_fuota_dot_fuota__pb2


class FUOTAServerServiceStub(object):
    """FUOTAServerService provides the fuota-server API methods.
    Note: this API considered experimental.
    """

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.CreateDeployment = channel.unary_unary(
                '/fuota.FUOTAServerService/CreateDeployment',
                request_serializer=chirpstack__api_dot_fuota_dot_fuota__pb2.CreateDeploymentRequest.SerializeToString,
                response_deserializer=chirpstack__api_dot_fuota_dot_fuota__pb2.CreateDeploymentResponse.FromString,
                )
        self.GetDeploymentStatus = channel.unary_unary(
                '/fuota.FUOTAServerService/GetDeploymentStatus',
                request_serializer=chirpstack__api_dot_fuota_dot_fuota__pb2.GetDeploymentStatusRequest.SerializeToString,
                response_deserializer=chirpstack__api_dot_fuota_dot_fuota__pb2.GetDeploymentStatusResponse.FromString,
                )
        self.GetDeploymentDeviceLogs = channel.unary_unary(
                '/fuota.FUOTAServerService/GetDeploymentDeviceLogs',
                request_serializer=chirpstack__api_dot_fuota_dot_fuota__pb2.GetDeploymentDeviceLogsRequest.SerializeToString,
                response_deserializer=chirpstack__api_dot_fuota_dot_fuota__pb2.GetDeploymentDeviceLogsResponse.FromString,
                )


class FUOTAServerServiceServicer(object):
    """FUOTAServerService provides the fuota-server API methods.
    Note: this API considered experimental.
    """

    def CreateDeployment(self, request, context):
        """CreateDeployment creates the given FUOTA deployment.
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def GetDeploymentStatus(self, request, context):
        """GetDeploymentStatus returns the FUOTA deployment status given an ID.
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def GetDeploymentDeviceLogs(self, request, context):
        """GetDeploymentDeviceLogs returns the FUOTA logs given a deployment ID and DevEUI.
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')


def add_FUOTAServerServiceServicer_to_server(servicer, server):
    rpc_method_handlers = {
            'CreateDeployment': grpc.unary_unary_rpc_method_handler(
                    servicer.CreateDeployment,
                    request_deserializer=chirpstack__api_dot_fuota_dot_fuota__pb2.CreateDeploymentRequest.FromString,
                    response_serializer=chirpstack__api_dot_fuota_dot_fuota__pb2.CreateDeploymentResponse.SerializeToString,
            ),
            'GetDeploymentStatus': grpc.unary_unary_rpc_method_handler(
                    servicer.GetDeploymentStatus,
                    request_deserializer=chirpstack__api_dot_fuota_dot_fuota__pb2.GetDeploymentStatusRequest.FromString,
                    response_serializer=chirpstack__api_dot_fuota_dot_fuota__pb2.GetDeploymentStatusResponse.SerializeToString,
            ),
            'GetDeploymentDeviceLogs': grpc.unary_unary_rpc_method_handler(
                    servicer.GetDeploymentDeviceLogs,
                    request_deserializer=chirpstack__api_dot_fuota_dot_fuota__pb2.GetDeploymentDeviceLogsRequest.FromString,
                    response_serializer=chirpstack__api_dot_fuota_dot_fuota__pb2.GetDeploymentDeviceLogsResponse.SerializeToString,
            ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
            'fuota.FUOTAServerService', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))


 # This class is part of an EXPERIMENTAL API.
class FUOTAServerService(object):
    """FUOTAServerService provides the fuota-server API methods.
    Note: this API considered experimental.
    """

    @staticmethod
    def CreateDeployment(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/fuota.FUOTAServerService/CreateDeployment',
            chirpstack__api_dot_fuota_dot_fuota__pb2.CreateDeploymentRequest.SerializeToString,
            chirpstack__api_dot_fuota_dot_fuota__pb2.CreateDeploymentResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def GetDeploymentStatus(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/fuota.FUOTAServerService/GetDeploymentStatus',
            chirpstack__api_dot_fuota_dot_fuota__pb2.GetDeploymentStatusRequest.SerializeToString,
            chirpstack__api_dot_fuota_dot_fuota__pb2.GetDeploymentStatusResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def GetDeploymentDeviceLogs(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/fuota.FUOTAServerService/GetDeploymentDeviceLogs',
            chirpstack__api_dot_fuota_dot_fuota__pb2.GetDeploymentDeviceLogsRequest.SerializeToString,
            chirpstack__api_dot_fuota_dot_fuota__pb2.GetDeploymentDeviceLogsResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)
