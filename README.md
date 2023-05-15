<pre>
                                                     /$$$$$$$$ /$$       /$$   /$$
     _   _  U _____ u  _       _       U  ___ u     | $$_____/| $$      |__/  | $$
    |'| |'| \| ___"|/ |"|     |"|       \/"_ \/     | $$      | $$       /$$ /$$$$$$    /$$$$$$
   /| |_| |\ |  _|" U | | u U | | u     | | | |     | $$$$$   | $$      | $$|_  $$_/   /$$__  $$
   U|  _  |u | |___  \| |/__ \| |/__.-,_| |_| |     | $$__/   | $$      | $$  | $$    | $$$$$$$$  
    |_| |_|  |_____|  |_____| |_____|\_)-\___/      | $$      | $$      | $$  | $$ /$$| $$_____/
    //   \\  <<   >>  //  \\  //  \\      \\        | $$      | $$$$$$$$| $$  |  $$$$/|  $$$$$$$
   (_") ("_)(__) (__)(_")("_)(_")("_)    (__)       |__/      |________/|__/   \___/   \_______/
                                                                                      Version 1.0.1
</pre>

<div align="center">
<h1 align="center">FLite: A Lightweight Federated Learning Framework for Real-World Deployment</h1>

![GitHub](https://img.shields.io/github/license/Sensorjang/FLite)
![Version](https://img.shields.io/badge/Version-V1.0.1-yellow)
![Language](https://img.shields.io/badge/Language-Python-blue)
![Build](https://img.shields.io/badge/Build-passing-lightgreen)
![Maintained](https://img.shields.io/badge/Maintained-Yes-red)

</div>

## Introduction
**Graduation Project: Design and Implementation of a Topology Based Distributed Training Federated Learning Experimental Framework. <br/>**
**毕业设计：一种基于拓扑结构的分布式训练联邦学习实验框架的设计与实现<br/>**
[Software Engineering, School of Computer Science and Technology, WUST, P. Qi(Sensorjang@wust.edu.cn)]<br/>

## Prerequisites
- Linux 或 macOS
- Python 3.6+
- PyTorch 1.3+
- CUDA 9.2+（如果您使用GPU运行）

## Installation
这里是使用 conda 配置FLite环境的完整命令<br/>
Here is the complete command to configure the FLite environment using conda<br/>

```bash
# create a new conda environment
# 创建一个新的conda环境
conda create -n flite python=3.7 -y
conda activate flite

# 1、CPU only
# 在仅通过CPU计算的设备上运行
conda install pytorch==1.6.0 torchvision==0.7.0 -c pytorch -y
# 2、With GPU
# 在支持GPU的设备上运行
conda install pytorch==1.6.0 torchvision==0.7.0 cudatoolkit=10.1 -c pytorch -y

# install FLite
# 1、本地编译安装FLite
git clone https://github.com/Sensorjang/FLite.git
cd FLite
pip install -v -e .
# 2、pip安装 (from https://pypi.org/project/FLite/1.0.1)
pip install FLite==1.0.1
```

## Features Overview

### 联邦学习计算范例支持
- 独立仿真训练 Independent Simulation Training
- 分布式训练（基于gRPC通信协议）Distributed Training (based on gRPC communication protocol)

### 数据集与模型支持
| - | LeNet | ResNet18 | ResNet50 | RNN | simple-CNN | VGG9 |
| :---: |:-----:|:--------:|:--------:|:---:|:----------:|:----:|
| Cifar10 |   √   |    √     |    √     |     |     √      |  √   |
| FEMNIST |   √   |          |          |     |     √      |      |
| Shakespeare |       |          |          |  √  |            |      |
| Cifar100 |   √   |    √     |    √     |     |     √      |  √   |

### 联邦聚合算法支持
- FedAvg
- FedProx
- Equal Average


#### 聚合策略：all、parameters

- all：使用statedict聚合模型，包括模型参数和持久缓冲区（如BatchNorm统计数据）
- parameters：只聚集模型参数。

### 模型加密算法支持
- Blowfish
- DES
- Salsa20

### 数据分布支持
支持：iid、niid（用于feminist和shakespeare），以及dir和class（用于cifar系列数据集）

### 联邦优化器
- SGD
- Adam

### 联邦学习配置文件
- python代码中导入配置
- 外部yaml文件入配置
- 混合导入配置
- 使用指令参数传递配置

### 联邦建模追踪服务
本地数据库配置,支持sqlite3和mysql

### 异构联邦客户端模拟
- Simulate ISO: 选定客户端具有等长睡眠时间分布
- Simulate DIR: 使用对称狄利克雷过程对睡眠时间异质性进行采样，以模拟直接异质性
- Simulate REAL: 模拟真实的异构性，即客户端的计算能力不同。使用主流智能手机的真实速度比来模拟睡眠时间的异构性

#### 处理系统异构的分组策略
支持：随机、贪婪、最慢(random, greedy, slowest)

### FLite特色
设备异构模拟服务
联邦建模追踪服务
数据集分割处理模块

## Quick Start
Flite提供了许多示例，您可以在[examples](/examples)目录下找到它们。<br/>
Flite provides many examples, which can be found in the [examples](/examples) directory.<br/>

## License
This project is released under the [MIT License](LICENSE).
