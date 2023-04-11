import FLite


config = {
    "data": {"dataset": "cifar10"},
    "model": "lenet_cifar10",
    "test_mode": "test_in_server",
}

FLite.init(config)
FLite.run()
