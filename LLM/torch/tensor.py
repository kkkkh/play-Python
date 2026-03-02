import torch
#region pre
# torch 版本
print(torch.__version__)
# 检查安装是否识别了内置的NVIDIA GPU
print(torch.cuda.is_available())
# 以检查你的Mac是否支持使用Apple Silicon芯片加速PyTorch
print(torch.backends.mps.is_available())
#endregion pre

#region tensor
tensor0d = torch.tensor(1)
tensor1d = torch.tensor([1,2,3])
tensor2d = torch.tensor([[1,2],[3,4]])
tensor3d = torch.tensor([[[1,2],[3,4]],[[5,6],[7,8]]])
#endregion tensor

#region shape
tensor2d = torch.tensor([[1, 2, 3], [4, 5, 6]])
print(tensor2d.shape)
# torch.Size([2, 3])
#endregion shape

#region reshape
# 改变的是行与列的数量
print(tensor2d.reshape(3, 2))
# tensor([[1, 2],
#         [3, 4],
#         [5, 6]])
print(tensor2d.view(3, 2))
# tensor([[1, 2],
#         [3, 4],
#         [5, 6]])
#endregion reshape

#region T
# 是每一个值的想 x,y坐标进行调换
tensor2d = torch.tensor([[1, 2, 3], [4, 5, 6]])
# 1（0，0） 2 （1，0） 3（2，0）
# 4（0，1） 5（1，1） 6（2，1）
print(tensor2d.T)
# tensor([[1, 4],
#         [2, 5],
#         [3, 6]])
# 1（0，0） 2 （0，1） 3（0，2）
# 4（1，0） 5（1，1） 6（1，2）
#endregion T

# region matmul
# 矩阵相乘
print(tensor2d.matmul(tensor2d.T))
# tensor([[14, 32],
#         [32, 77]])
print(tensor2d @ tensor2d.T)
# tensor([[14, 32],
#         [32, 77]])
#endregion matmul



X = torch.rand((1, 50))
print(X)
# tensor([[0.4293, 0.8310, 0.5309, 0.9465, 0.1308, 0.5832, 0.0374, 0.4018, 0.2917,
#          0.9049, 0.0435, 0.7375, 0.3036, 0.9863, 0.5724, 0.1524, 0.7737, 0.8297,
#          0.7989, 0.2393, 0.0254, 0.7968, 0.9454, 0.3183, 0.6662, 0.2899, 0.3774,
#          0.6075, 0.1887, 0.4808, 0.9087, 0.5328, 0.9162, 0.9087, 0.9654, 0.0024,
#          0.0821, 0.4569, 0.0952, 0.2308, 0.8048, 0.1978, 0.7330, 0.3982, 0.8850,
#          0.6174, 0.8036, 0.2316, 0.6516, 0.7724]])
