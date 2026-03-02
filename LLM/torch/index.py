import torch
from torch.utils.data import Dataset, DataLoader
import torch.nn.functional as F

#region NeuralNetwork
# 多层感知机(multilayer perceptron)，即全连接神经网络
class NeuralNetwork(torch.nn.Module):
    def __init__(self, num_inputs, num_outputs):
        super().__init__()

        self.layers = torch.nn.Sequential(
            # 1st hidden layer
            torch.nn.Linear(num_inputs, 30),
            torch.nn.ReLU(),

            # 2nd hidden layer
            torch.nn.Linear(30, 20),
            torch.nn.ReLU(),

            # output layer
            torch.nn.Linear(20, num_outputs),
        )

    def forward(self, x):
        # print("x",x)
        # 与 print(X) 一致
        # tensor([[0.2391, 0.3194, 0.8111, 0.7507, 0.3306, 0.5374, 0.2845, 0.8459, 0.2232,
        #          0.2083, 0.8169, 0.1084, 0.3285, 0.7185, 0.3624, 0.3084, 0.8893, 0.4179,
        #          0.9741, 0.3697, 0.2397, 0.8936, 0.1443, 0.1365, 0.7625, 0.1632, 0.6641,
        #          0.1525, 0.9830, 0.5936, 0.9120, 0.0146, 0.6323, 0.4743, 0.7467, 0.3545,
        #          0.9994, 0.9815, 0.7399, 0.2057, 0.8742, 0.0138, 0.7676, 0.7481, 0.7570,
        #          0.6432, 0.9111, 0.2246, 0.8668, 0.6961]])
        logits = self.layers(x)
        return logits

torch.manual_seed(123)
#endregion NeuralNetwork
#region NeuralNetworkTest
# NeuralNetwork 测试
def NeuralNetworkTest():
  model = NeuralNetwork(50, 3)
  X = torch.rand((1, 50))
  print(X)
  # tensor([[0.2391, 0.3194, 0.8111, 0.7507, 0.3306, 0.5374, 0.2845, 0.8459, 0.2232,
  #          0.2083, 0.8169, 0.1084, 0.3285, 0.7185, 0.3624, 0.3084, 0.8893, 0.4179,
  #          0.9741, 0.3697, 0.2397, 0.8936, 0.1443, 0.1365, 0.7625, 0.1632, 0.6641,
  #          0.1525, 0.9830, 0.5936, 0.9120, 0.0146, 0.6323, 0.4743, 0.7467, 0.3545,
  #          0.9994, 0.9815, 0.7399, 0.2057, 0.8742, 0.0138, 0.7676, 0.7481, 0.7570,
  #          0.6432, 0.9111, 0.2246, 0.8668, 0.6961]])
  out = model(X)
  print(out)
  # tensor([[-0.1670,  0.1001, -0.1219]], grad_fn=<AddmmBackward0>)

  with torch.no_grad():
      # model(X)返回的是logits
      # 不会返回 经过 激活函数softmax 或 sigmoid 处理的值
      # 因为损失函数会将 激活 与 负对数似然损失 结合在一起
      # 手动调用,获得 预测结果计算类别成员概率
      out = torch.softmax(model(X), dim=1)
  print(out)
  # tensor([[0.2983, 0.3896, 0.3121]])
#endregion NeuralNetworkTest
#region data
# 创建训练数据集和测试数据集
class ToyDataset(Dataset):
    def __init__(self, X, y):
        self.features = X
        self.labels = y

    def __getitem__(self, index):
        one_x = self.features[index]
        one_y = self.labels[index]
        return one_x, one_y

    def __len__(self):
        return self.labels.shape[0]


X_train = torch.tensor([
        [-1.2, 3.1],
        [-0.9, 2.9],
        [-0.5, 2.6],
        [2.3, -1.1],
        [2.7, -1.5]
    ])
y_train = torch.tensor([0, 0, 0, 1, 1])

# 准备数据集
def prepare_dataset():
    X_test = torch.tensor([
        [-0.8, 2.8],
        [2.6, -1.6],
    ])
    y_test = torch.tensor([0, 1])

    train_ds = ToyDataset(X_train, y_train)
    test_ds = ToyDataset(X_test, y_test)

    # 创建数据加载器
    train_loader = DataLoader(
        dataset=train_ds,
        batch_size=2, # 每批次两条数据
        shuffle=True,  # 打乱顺序
        num_workers=0, # 当num_workers设置为大于0的数值时，会启动多个工作进程并行加载数据
        drop_last=True
    )
    test_loader = DataLoader(
        dataset=test_ds,
        batch_size=2,
        shuffle=True,
        num_workers=0
    )

    # for idx, (x, y) in enumerate(train_loader):
    #   print(f"Batch {idx+1}:", x, y)
    # Batch 1: tensor([[ 2.7000, -1.5000],
    #         [ 2.3000, -1.1000]]) tensor([1, 1])
    # Batch 2: tensor([[-0.9000,  2.9000],
    #         [-1.2000,  3.1000]]) tensor([0, 0])
    # Batch 3: tensor([[-0.5000,  2.6000]]) tensor([0])

    return train_loader, test_loader

#endregion data
#region epoch
num_epochs = 3
train_loader,test_loader = prepare_dataset()
model = NeuralNetwork(2, 2) # 该数据集有两个特征，两个标签
optimizer = torch.optim.SGD(model.parameters(), lr=0.5)

# 进行三轮训练
for epoch in range(num_epochs):
    # 训练模式
    model.train()
    for batch_idx, (features, labels) in enumerate(train_loader):
        print("features",features)
        logits = model(features)
        # cross_entropy损失函数，后者会在内部应用softmax函数，以提高效率并增强数值稳定性
        loss = F.cross_entropy(logits, labels)  # Loss function

        optimizer.zero_grad() # 将上一轮的梯度 置为0
        loss.backward() # 计算梯度
        optimizer.step() # 优化器使用梯度更新模型参数

        # LOGGING
        print(f"Epoch: {epoch+1:03d}/{num_epochs:03d}"
              f" | Batchsize {labels.shape[0]:03d}"
              f" | Train/Val Loss: {loss:.2f}")
#endregion epoch
#region eval
# 评估模式
model.eval()
with torch.no_grad():
    outputs = model(X_train)
    print(outputs)
    torch.set_printoptions(sci_mode=False)
    # 获得类别成员概率
    probas = torch.softmax(outputs, dim=1)
    print(probas)
    # argmax函数将这些概率值转换为类别标签预测
    predictions = torch.argmax(probas, dim=1)
    print(predictions)
    predictions = torch.argmax(outputs, dim=1)
    print(predictions)
    print(predictions == y_train)
    # tensor([True, True, True, True, True])

def compute_accuracy(model, dataloader):
    # 预测准确率
    model = model.eval()
    correct = 0.0
    total_examples = 0

    for idx, (features, labels) in enumerate(dataloader):

        with torch.no_grad():
            logits = model(features)
        predictions = torch.argmax(logits, dim=1)
        compare = labels == predictions
        correct += torch.sum(compare)
        total_examples += len(compare)
    return (correct / total_examples).item()

print(compute_accuracy(model, train_loader))
#endregion eval
#region save-load
# 保存
# state_dict是一个Python字典对象，
# 它可以将模型中的每一层映射到其可训练参数（权重和偏置）
torch.save(model.state_dict(), "./torch/model.pth")
# 加载
# model = NeuralNetwork(2, 2)这一行并不是严格必需的。
# 然而，这里包含它是为了说明我们需要在内存中拥有一个模型的实例，这样才能应用保存的参数。
# 此外，NeuralNetwork(2, 2)的架构必须与最初保存的模型完全匹配。
model = NeuralNetwork(2, 2)
# model.load_state_dict()则将这些参数应用到模型中，有效地恢复了我们保存模型时模型的学习状态
model.load_state_dict(torch.load("./torch/model.pth",weights_only=True))
#endregion save-load
