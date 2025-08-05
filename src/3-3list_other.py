# 成员运算符
print(3 in [1, 3, 4, 5])
# True
print(3 not in [1, 3, 4, 5])
# False
print(3 in ["one", "two", "three"])
# False
print(3 not in ["one", "two", "three"])
# True

# 列表推导式
z = [1, 2, 3] + [4, 5]
print(z)
# [1, 2, 3, 4, 5]

z = [1, 2, 3] * 3
print(z)
# [1, 2, 3, 1, 2, 3, 1, 2, 3]
z = [None] * 4
print(z)
# [None, None, None, None]

# min 最小值 max 最大值
print(min([3, 7, 0, -2, 11]))
# -2
# print(max([4, "Hello", [1, 2]]))
# Traceback (most recent call last):
#   File "<pyshell#58>", line 1, in <module>
#     max([4, "Hello",[1, 2]])
# TypeError: '>' not supported between instances of 'str' and 'int'

# index 值的索引 找不到会报错
x = [1, 3, "five", 7, -2]
print(x.index(7))
# 3
# print(x.index(5))
# Traceback (innermost last):
#   File "<stdin>", line 1, in ?
# ValueError: 5 is not in list

# count 计数
x = [1, 2, 2, 3, 5, 2, 5]
print(x.count(2))
# 3
print(x.count(5))
# 2
print(x.count(4))
# 0
