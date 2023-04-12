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
# 初始化服务i去配置文件
FLite.init(conf, init_all=False)
# Start remote client service.
# 远程客户端等待服务器连接
# 需要提前制定用户持有的数据类型以初始化数据集
FLite.start_client("femnist")