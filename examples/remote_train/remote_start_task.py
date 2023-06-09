import FLite
from FLite.protobuf import common_pb2 as common_pb
from FLite.protobuf import server_service_pb2 as server_pb
from FLite.protocol import codec
from FLite.communication.grpc import grpc_wrapper
from FLite.registry.vclient import VirtualClient

config = {
    # "data": {"dataset": "femnist"}, # 注意：选择的数据集名称应当与远程客户端启动时配置的的数据集一致，使用自定义数据集时本项忽略不配置
    "model": "lenet",
    "test_mode": "test_in_client",
    "server": {"rounds": 5, "clients_per_round": 2},
    "client": {"track": True},
}
# 初始化配置
FLite.init(config, init_all=False)

# Initialize the model, using the configured 'lenet'
model = FLite.init_model()

"""
修改服务端信息
"""
server_addr = "localhost:22999"
# 组建gRPC请求
stub = grpc_wrapper.init_stub(grpc_wrapper.TYPE_SERVER, server_addr)
request = server_pb.RunRequest(model=codec.marshal(model))


"""
修改客户端信息
"""
# 请求包含客户端地址用于和服务器建立通信
# clients = [VirtualClient("1", "localhost:23000", 0), VirtualClient("2", "localhost:23001", 1)]
clients = [VirtualClient("1", "localhost:23000", 0)]
for c in clients:
    request.clients.append(server_pb.Client(client_id=c.id, index=c.index, address=c.address))


# 发送请求以触发训练
print("waiting ...")
response = stub.Run(request)
result = "Success" if response.status.code == common_pb.SC_OK else response
print("[OK!]\ntask_start_msg sent SUCCESSFULLY!\n\nconfig: {}\nresult: {}".format(config, result))