from torch import nn
import torch.nn.functional as F
import FLite
from FLite.models.BaseModel import BaseModel

"""
1 使用模型类传递模型配置
"""
def method_1():
    # Define a customized model class.
    class CustomizedModel(BaseModel):
        def __init__(self):
            super(CustomizedModel, self).__init__()
            self.conv1 = nn.Conv2d(3, 32, 224, padding=(2, 2))
            self.conv2 = nn.Conv2d(32, 64, 5, padding=(2, 2))
            self.fc1 = nn.Linear(64, 128)
            self.fc2 = nn.Linear(128, 42)

        def forward(self, x):
            x = F.relu(self.conv1(x))
            x = F.max_pool2d(x, 2, 2)
            x = F.relu(self.conv2(x))
            x = F.max_pool2d(x, 2, 2)
            x = x.view(-1, 64)
            x = F.relu(self.fc1(x))
            x = self.fc2(x)

            return x

    # Register the customized model class.
    FLite.register_model(CustomizedModel)


"""
2 使用模型实例递模型配置
"""
def method_2():
    # Define a customized model class.
    class CustomizedModel(BaseModel):
        def __init__(self, num_class):
            super(CustomizedModel, self).__init__()
            self.conv1 = nn.Conv2d(3, 32, 224, padding=(2, 2))
            self.conv2 = nn.Conv2d(32, 64, 5, padding=(2, 2))
            self.fc1 = nn.Linear(64, 128)
            self.fc2 = nn.Linear(128, num_class)

        def forward(self, x):
            x = F.relu(self.conv1(x))
            x = F.max_pool2d(x, 2, 2)
            x = F.relu(self.conv2(x))
            x = F.max_pool2d(x, 2, 2)
            x = x.view(-1, 64)
            x = F.relu(self.fc1(x))
            x = self.fc2(x)
            return x

    # Register the customized model instance.
    FLite.register_model(CustomizedModel(num_class=10))


if __name__ == '__main__':

    method_1()
    # method_2()

    FLite.init(FLite.load_config("../customize_config/myconfig.yaml"))
    FLite.run()

