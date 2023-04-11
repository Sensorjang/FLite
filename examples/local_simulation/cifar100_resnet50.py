import FLite


config = {
    "data": {"dataset": "cifar100"},
    "model": "resnet50_cifar100",
    "test_mode": "test_in_server",
}

FLite.init(config)
FLite.run()
