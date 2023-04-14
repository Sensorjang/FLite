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
    "client": {
        "encryption": {"key": "ABCDEGFHABCDEGFH", "type": "CAST"},
    }
}
FLite.init(conf, init_all=False)
# 启动远程服务,需要提前指定用户持有的数据类型以初始化数据集
FLite.start_client("femnist")