import FLite


config = {
    "data": {"dataset": "cifar10"},
    "model": "vgg9",
    "test_mode": "test_in_server",
}

FLite.init(config)
FLite.run()
