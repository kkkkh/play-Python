# 列表

# 列表长度
len([])
# 0
len([0])
# 1
len([[1,2,3,3],7])


# 索引
# 1、正向索引
x = ["first", "second", "third", "fourth"]
print(x[1:-1])
# ['second', 'third']
print(x[0:3])
# ['first', 'second', 'third']
print(x[-2:-1])
# ['third']

# 2、反向索引
print(x[-1:2])
# []

# 3、省略索引
print(x[:3])
# ['first', 'second', 'third']
print(x[2:])
# ['third', 'fourth']
y = x[:]
y[0] = '1 st'
print(y)
# ['1 st', 'second', 'third', 'fourth']
print(x)
# ['first', 'second', 'third', 'fourth']


# 编辑列表
# 1、替换
# 单个元素替换
x = [1, 2, 3, 4]
x[1] = "two"
print(x)
# [1, 'two', 3, 4]

# 多个元素替换
x = [1, 2, 3, 4]
x[1:3] = ["two", "three"]
print(x)
# [1, 'two', 'three', 4]
x[1:3] = ["two"]
print(x)
# [1, 'two', 4]

# 字符串替换
x = [1, 2, 3, 4]
x[1:3] = "123"
print(x)
# [1, '1', '2', '3', 4]

# 2、添加
# 在列表末尾添加元素
x = [1, 2, 3, 4]
x[len(x):] = [5, 6, 7]
print(x)
# [1, 2, 3, 4, 5, 6, 7]

# 在列表头部添加元素
x = [1, 2, 3, 4]
x[:0] = [-1,0]
print(x)
# [-1, 0, 1, 2, 3, 4]

# append
x = [1, 2, 3]
x.append("four")
print(x)
# [1, 2, 3, 'four']
x = [1, 2, 3, 4]
y = [5, 6, 7]
x.append(y)
print(x)
# [1, 2, 3, 4, [5, 6, 7]]

# extend
x = [1, 2, 3, 4]
y = [5, 6, 7]
x.extend(y)
print(x)
# [1, 2, 3, 4, 5, 6, 7]

# insert
# list.insert(n, elem)与list[n:n] = [elem]的效果是一样的。
x = [1, 2, 3]
x.insert(2, "hello")
print(x)
# [1, 2, 'hello', 3]
x.insert(0, "start")
print(x)
# ['start', 1, 2, 'hello', 3]
x = [1, 2, 3]
x.insert(-1, "hello")
print(x)
# [1, 2, 'hello', 3]


# 3、删除
# 删除多个元素
x = [1, 2, 3, 4]
x[1:3] = []
print(x)
# [1, 4]

# 删除列表
x = [1, 2, 3, 4]
x[:] = []
print(x)
# []

# del
# del list[n]的功能与list[n:n+1] = [​]是一样的
# 而del list[m:n]的功能则与list[m:n] = [​]相同

x = ['a', 2, 'c', 7, 9, 11]
del x[1]
print(x)
# ['a', 'c', 7, 9, 11]
del x[:2]
print(x)
# [7, 9, 11]

# remove 删除的是列表中的元素
x = [1, 2, 3, 4, 3, 5]
x.remove(3)
print(x)
# [1, 2, 4, 3, 5]
x.remove(3)
print(x)
# [1, 2, 4, 5]
# x.remove(3)
# Traceback (innermost last):
#   File "<stdin>", line 1, in ?
# ValueError: list.remove(x): x not in list

# 4、反转列表

x = [1, 3, 5, 6, 7]
x.reverse()
print(x)
# [7, 6, 5, 3, 1]

# 列表移动至表头
# 切片插入
data_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
last_three = data_list[-3:]  # 获取最后 3 个数据项
del data_list[-3:]           # 从原列表中删除最后 3 个数据项
data_list[0:0] = last_three  # 将最后 3 个数据项插入到列表开头
print(data_list)
# 循环插入 pop 和 insert
data_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
for _ in range(3):
    item = data_list.pop()      # 移除列表末尾的元素
    data_list.insert(0, item)   # 将元素插入到列表开头
print(data_list)

