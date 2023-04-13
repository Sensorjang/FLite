import FLite
from FLite.datasets import FederatedImageDataset

import os
from torchvision import transforms


TRANSFORM_TRAIN_LIST = transforms.Compose([
    transforms.Resize((256, 128), interpolation=3),
    transforms.Pad(10),
    transforms.RandomCrop((256, 128)),
    transforms.RandomHorizontalFlip(),
    transforms.ToTensor(),
    transforms.Normalize([0.485, 0.456, 0.406], [0.229, 0.224, 0.225])
])
TRANSFORM_VAL_LIST = transforms.Compose([
    transforms.Resize(size=(256, 128), interpolation=3),
    transforms.ToTensor(),
    transforms.Normalize([0.485, 0.456, 0.406], [0.229, 0.224, 0.225])
])

DATASETS = ["MSMT17", "Duke", "Market", "cuhk03", "prid", "cuhk01", "viper", "3dpes", "ilids"]

# Prepare customized training data
def prepare_train_data(data_dir):
    client_ids = []
    roots = []
    for db in DATASETS:
        client_ids.append(db)
        data_path = os.path.join(data_dir, db, "pytorch")
        roots.append(os.path.join(data_path, "train_all"))
    data = FederatedImageDataset(root=roots,
                                 simulated=True,
                                 do_simulate=False,
                                 transform=TRANSFORM_TRAIN_LIST,
                                 client_ids=client_ids)
    return data


# Prepare customized testing data
def prepare_test_data(data_dir):
    roots = []
    client_ids = []
    for db in DATASETS:
        test_gallery = os.path.join(data_dir, db, 'pytorch', 'gallery')
        test_query = os.path.join(data_dir, db, 'pytorch', 'query')
        roots.extend([test_gallery, test_query])
        client_ids.extend([f"{db}_gallery", f"{db}_query"])
    data = FederatedImageDataset(root=roots,
                                 simulated=True,
                                 do_simulate=False,
                                 transform=TRANSFORM_VAL_LIST,
                                 client_ids=client_ids)
    return data


if __name__ == '__main__':

    config = {...}
    data_dir = "datasets/"
    train_data, test_data = prepare_train_data(data_dir), prepare_test_data(data_dir)
    FLite.register_dataset(train_data, test_data)

    FLite.init(config)
    FLite.run()