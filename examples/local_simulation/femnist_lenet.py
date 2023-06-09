import FLite


config = {
    "task_id": "femnist",
    "data": {"dataset": "femnist", "split_type": "iid"},
    "server": {"rounds": 10, "clients_per_round": 10, "test_all": True, "aggregation_strategy": "FedProx", "prox_mu": 0.01},
    "client": {"local_epoch": 30},
    "model": "lenet",
    "test_mode": "test_in_client",
}


FLite.init(config)
FLite.run()
