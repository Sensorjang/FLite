import FLite


config = {
    "data": {"dataset": "shakespeare"},
    "model": "rnn",
    "test_mode": "test_in_client",
}

FLite.init(config)
FLite.run()
