import FLite
"""
1 python代码中导入配置
"""
def method_1():
    # Define customized configurations.
    config = {
        "data": {
            "root": "../../local_simulation/data/",
            "dataset": "cifar10",
            "num_of_clients": 1000
        },
        "server": {
            "rounds": 5,
            "clients_per_round": 2
        },
        "client": {"local_epoch": 5},
        "model": "resnet18",
        "test_mode": "test_in_server",
    }
    # Initialize FLite with the new config.
    FLite.init(config)


"""
2 外部yaml文件入配置
"""
def method_2():
    config_file = "myconfig.yaml"
    # Load the yaml file as config.
    config = FLite.load_config(config_file)
    # Initialize FLite with the new config.
    FLite.init(config)


"""
3 混合导入配置(一般使用python导入需要经常修改的内容,使用yaml导入不需要经常改动的内容,两份配置将被merge,其中python导入的配置优先级更高)
"""
def method_3():
    # Define part of customized configs.
    config = {
        "data": {
            "root": "../../local_simulation/data/",
            "dataset": "cifar10",
            "num_of_clients": 10
        },
        "server": {
            "rounds": 5,
            "clients_per_round": 2
        },
        "client": {"local_epoch": 5},
        "model": "resnet18",
        "test_mode": "test_in_server",
    }
    config_file = "myconfig.yaml"
    # Define part of configs in a yaml file.
    config = FLite.load_config(config,config_file)
    # Initialize FLite with the new config.
    FLite.init(config)


"""
4 使用指令参数传递配置
"""
def method_4():
    import argparse
    # Define command line arguments.
    parser = argparse.ArgumentParser(description='Example')
    parser.add_argument("--batch_size", type=int, default=32)
    parser.add_argument("--local_epoch", type=int, default=5)
    args = parser.parse_args()
    print("args", args)

    # Define customized configurations using the arguments.
    config = {
        "client": {
            "batch_size": args.batch_size,
            "local_epoch": args.local_epoch,
        }
    }
    # Initialize FLite with the new config.
    FLite.init(config)


if __name__ == '__main__':

    method_1()
    # method_2()
    # method_3()
    # method_4()

    FLite.run()