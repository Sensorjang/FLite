import FLite


config = {
    "task_id": "femnist",
    "data": {"dataset": "femnist", "split_type": "iid"},
    "server": {"rounds": 5, "clients_per_round": 2, "test_all": True},
    "client": {"local_epoch": 5},
    "model": "simple_cnn_femnist",
    "test_mode": "test_in_client",
}

FLite.init(config)
FLite.run()
