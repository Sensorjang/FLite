import FLite

# Configurations for the remote client.
"""
修改客户端信息
"""
conf = {
    "is_remote": True,
    "local_port": 23000,
    "server_addr": "localhost:22999",
    "index": 0,
}
# Initialize only the configuration.
FLite.init(conf, init_all=False)
# Start remote client service.
# The remote client waits to be connected with the remote server.
FLite.start_client()