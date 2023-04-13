import FLite
from FLite.server.BaseServer import BaseServer
from FLite.server.BaseServer import MODEL


class CustomizedServer(BaseServer):
    def __init__(self, conf, **kwargs):
        super(CustomizedServer, self).__init__(conf, **kwargs)
        from FLite.utils.obvious_notice_logger import noticelogger
        noticelogger.get_instance().red("CustomizedServer init")
        pass  # more initialization of attributes.

    def aggregation(self):
        uploaded_content = self.get_client_uploads()
        models = list(uploaded_content[MODEL].values())
        # Original implementation of aggregation weights
        # weights = list(uploaded_content[DATA_SIZE].values())
        # We can assign the manipulated customized weights in aggregation.
        customized_weights = list(range(len(models)))
        model = self.aggregate(models, customized_weights)
        self.set_model(model, load_dict=True)


# Register customized server.
FLite.register_server(CustomizedServer)


"""
1 remote start
"""
conf = {"is_remote": True, "local_port": 22999}
FLite.init(conf, init_all=False)
FLite.start_server()


# """
# 2 simulation start
# """
# FLite.init()
# FLite.run()