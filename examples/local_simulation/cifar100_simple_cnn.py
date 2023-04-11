import FLite


config = {
    "data": {"dataset": "cifar100"},
    "model": "simple_cnn_cifar100",
    "test_mode": "test_in_server",
}

FLite.init(config)
FLite.run()
