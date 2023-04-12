import FLite

# Configurations for the remote server.
"""
修改服务端信息
"""
conf = {"is_remote": True, "local_port": 22999}
# Initialize only the configuration.
FLite.init(conf, init_all=False)
# Start remote server service.
# The remote server waits to be connected with the remote client.
FLite.start_server()