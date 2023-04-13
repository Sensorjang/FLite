import FLite
from FLite.client.BaseClient import BaseClient


# Inherit BaseClient to implement customized client operations.
class CustomizedClient(BaseClient):
    def __init__(self, cid, conf, train_data, test_data, device, **kwargs):
        super(CustomizedClient, self).__init__(cid, conf, train_data, test_data, device, **kwargs)
        pass  # more initialization of attributes.

    def decompression(self):
        pass  # implement decompression method.

    def pre_train(self):
        pass  # inject operations before training.

    def train(self, conf, device):
        pass  # implement customized training method.

    def post_train(self):
        pass  # inject operations after training.

    def load_loss_fn(self, conf):
        pass  # load a customized loss function.
        return loss

    def load_optimizer(self, conf):
        pass  # load a customized optimizer
        return optimizer

    def load_loader(self, conf):
        pass  # load a customized data loader.
        return train_loader

    def test_local(self):
        pass  # implement testing of the trained model before uploading to the server.

    def pre_test(self):
        pass  # inject operations before testing.

    def test(self, conf, device):
        pass  # implement customized testing.

    def post_test(self):
        pass  # inject operations after testing.

    def encryption(self):
        pass  # implement customized encryption method.

    def compression(self):
        pass  # implement customized compression method.

    def upload(self):
        pass  # implement customized upload method.

    def post_upload(self):
        pass  # implement customized post upload method.