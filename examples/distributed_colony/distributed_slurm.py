import FLite

from FLite.data_distribution import slurm
# Slurm 集群环境运行

rank, local_rank, world_size, host_addr = slurm.setup()

configs = {
    "gpu": 4,
    "distributed": {
        "rank": rank,
        "local_rank": local_rank,
        "world_size": world_size,
        "init_method": host_addr,
    },
    "server": {
        "clients_per_round": 20,
    }
}

FLite.init(configs)
FLite.run()
