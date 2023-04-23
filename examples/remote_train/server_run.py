import FLite

# 远程服务器的配置
"""
修改服务端信息
"""
conf = {
    "is_remote": True,
    "local_port": 22999,
    "server": {
        "encryption": {"key": "ABCDEGFHABCDEGFH", "type": "Blowfish"},
    }
}
# 初始化配置
FLite.init(conf, init_all=False)
# 启动远程服务器服务
# 远程服务器等待与远程客户端建立连接
FLite.start_server()