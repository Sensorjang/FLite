import FLite
from FLite.server.BaseServer import BaseServer


class CustomizedServer(BaseServer):
    def __init__(self, conf, **kwargs):
        super(CustomizedServer, self).__init__(conf, **kwargs)
        pass  # more initialization of attributes.

    def selection(self, clients, clients_per_round):
        pass  # implement customized client selection algorithm.

    def compression(self):
        pass  # implement customized compression algorithm.

    def pre_train(self):
        pass  # inject operations before distribution to train.

    def post_train(self):
        pass  # inject operations after aggregation.

    def pre_test(self):
        pass  # inject operations before distribution to test.

    def post_test(self):
        pass  # inject operations after aggregating testing results.

    def decompression(self, model):
        pass  # implement customized decompression algorithm.

    def aggregation(self):
        pass  # implement customized aggregation algorithm.