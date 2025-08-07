# 浅拷贝
x = [[0],[1]]
y = x[:] # 切片 浅拷贝
print(y)
# [[0], [1]]

x[0][0] = 100
print(y)
# [[100], [1]]


import copy
x = [[0],[1]]
y = copy.deepcopy(x) # 浅拷贝
print(y)
# [[0], [1]]

x[0][0] = 100
print(y)
# [[0], [1]]

