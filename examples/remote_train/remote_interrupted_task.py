from FLite.communication.grpc import grpc_wrapper
from FLite.protobuf import common_pb2 as common_pb
from FLite.protobuf import server_service_pb2 as server_pb

"""
修改服务端信息
"""
server_addr = "localhost:22999"
stub = grpc_wrapper.init_stub(grpc_wrapper.TYPE_SERVER, server_addr)


# 发送停止训练请求
print("waiting ...")
response = stub.Stop(server_pb.StopRequest())
result = "Success" if response.status.code == common_pb.SC_OK else response
print("[OK!]\ntask_stop_msg sent SUCCESSFULLY!\n\nresult: {}".format(result))