import time
import FLite
from torch import nn
import torch.optim as optim
from FLite.client.BaseClient import BaseClient
from FLite.models.lenet import Model

# Inherit BaseClient to implement customized client operations.
class CustomizedClient(BaseClient):
    def __init__(self, cid, conf, train_data, test_data, device, **kwargs):
        super(CustomizedClient, self).__init__(cid, conf, train_data, test_data, device, **kwargs)
        # Initialize a classifier for each client.
        self.classifier = nn.Sequential(*[nn.Linear(512, 100)])

        from FLite.models.lenet import Model
        self.model = Model()
        from FLite.utils.obvious_notice_logger import noticelogger
        noticelogger.get_instance().red("CustomizedClient init")

    def train(self, conf, device):
        start_time = time.time()
        self.model.classifier.classifier = self.classifier.to(device)
        loss_fn, optimizer = self.pretrain_setup(conf, device)
        self.train_loss = []
        for i in range(conf.local_epoch):
            batch_loss = []
            for batched_x, batched_y in self.train_loader:
                x, y = batched_x.to(device), batched_y.to(device)
                optimizer.zero_grad()
                out = self.model(x)
                loss = loss_fn(out, y)
                loss.backward()
                optimizer.step()
                batch_loss.append(loss.item())
            current_epoch_loss = sum(batch_loss) / len(batch_loss)
            self.train_loss.append(float(current_epoch_loss))
        self.train_time = time.time() - start_time
        # Keep the classifier in clients and upload only the backbone of model.
        self.classifier = self.model.classifier.classifier
        self.model.classifier.classifier = nn.Sequential()

    # A customized optimizer that sets different learning rates for different model parts.
    def load_optimizer(self, conf):
        ignored_params = list(map(id, self.model.classifier.parameters()))
        base_params = filter(lambda p: id(p) not in ignored_params, self.model.parameters())
        optimizer = optim.SGD([
            {'params': base_params, 'lr': 0.1 * conf.optimizer.lr},
            {'params': self.model.classifier.parameters(), 'lr': conf.optimizer.lr}
        ], weight_decay=5e-4, momentum=conf.optimizer.momentum, nesterov=True)
        return optimizer

# Register customized client.
FLite.register_client(CustomizedClient)


"""
1 remote start
"""
conf = {
    "is_remote": True,
    "local_port": 23000,
    "server_addr": "localhost:22999",
    "index": 0,
}
FLite.init(conf, init_all=False)
# 需要提前指定用户持有的数据类型以初始化数据集
FLite.start_client("cifar10")


# """
# 2 simulation start
# """
# config = {
#         "data": {
#             "dataset": "cifar10",
#             "num_of_clients": 1000
#         },
#         "server": {
#             "rounds": 5,
#             "clients_per_round": 2
#         },
#         "client": {"local_epoch": 5},
#         "model": "resnet18",
#         "test_mode": "test_in_server",
#     }
# # Initialize FLite with the new config.
# FLite.init(config)
# FLite.run()