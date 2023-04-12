import FLite
from FLite.protobuf import common_pb2 as common_pb
from FLite.protobuf import server_service_pb2 as server_pb
from FLite.protocol import codec
from FLite.communication.grpc import grpc_wrapper
from FLite.registry.vclient import VirtualClient

# TODO : 更改Client的Dataset初始化时间，适配不同的数据集
config = {
    "data": {"dataset": "femnist"},
    "model": "lenet",
    "test_mode": "test_in_client",
    "server": {"rounds": 5, "clients_per_round": 2},
    "client": {"track": True},
}
# Initialize configurations.
FLite.init(config, init_all=False)

# Initialize the model, using the configured 'lenet'
model = FLite.init_model()

"""
修改服务端信息
"""
server_addr = "localhost:22999"
# Construct gRPC request
stub = grpc_wrapper.init_stub(grpc_wrapper.TYPE_SERVER, server_addr)
request = server_pb.RunRequest(model=codec.marshal(model))


"""
修改客户端信息
"""
# The request contains clients' addresses for the server to communicate with the clients.
clients = [VirtualClient("1", "localhost:23000", 0), VirtualClient("2", "localhost:23001", 1)]
for c in clients:
    request.clients.append(server_pb.Client(client_id=c.id, index=c.index, address=c.address))


# Send request to trigger training.
print("waiting ...")
response = stub.Run(request)
result = "Success" if response.status.code == common_pb.SC_OK else response
print("[OK!]\ntask_start_msg sent SUCCESSFULLY!\n\nconfig: {}\nresult: {}".format(config, result))