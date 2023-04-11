import FLite


config = {
    "data": {"dataset": "cifar10"},
    "model": "simple_cnn",
    "test_mode": "test_in_server",
}

FLite.init(config)
FLite.run()
