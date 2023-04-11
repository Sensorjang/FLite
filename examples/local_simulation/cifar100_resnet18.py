import FLite


config = {
    "data": {"dataset": "cifar100"},
    "model": "resnet18_cifar100",
    "test_mode": "test_in_server",
}

FLite.init(config)
FLite.run()
