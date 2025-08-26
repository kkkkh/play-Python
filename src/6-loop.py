# 流程控制

# 1、if elseif else
x = 10
if x < 5:
    pass
    print("x < 5")
else:
    x = 5
    print(x)
# 2、for 循环
x = [1.0, 2.0, 3.0]
for n in x:
    print(1 / n)

# 2-1、range函数

x = [1, 3, -7, 4, 9, -5, 4]
for i in range(len(x)):
    if x[i] < 0:
        print("Found a negative number at index ", i)

print(range(3, 7))
x = list(range(3, 7))  # 1
print(x)
# [3, 4, 5, 6]
x = list(range(2, 10))  # 1
print(x)
# [2, 3, 4, 5, 6, 7, 8, 9]
x = list(range(5, 3))
print(x)
# []
x = list(range(0, 10, 2))
print(x)
# [0, 2, 4, 6, 8]
x = list(range(5, 0, -1))
print(x)
# [5, 4, 3, 2, 1]

# 2-2、元组拆包

somelist = [(1, 2), (3, 7), (9, 5)]
result = 0
for t in somelist:
    result = result + (t[0] * t[1])
print(result)
somelist = [(1, 2), (3, 7), (9, 5)]
result = 0

for x, y in somelist:
    result = result + (x * y)
print(result)

# 2-3、enumerate

x = [1, 3, -7, 4, 9, -5, 4]
for i, n in enumerate(x):  # 1
    if n < 0:  # 2
        print("Found a negative number at index ", i)  # 3

# 2-4、zip

x = [1, 2, 3, 4]
y = ["a", "b", "c"]  # 最短的列表长度决定结果长度
z = zip(x, y)
print(list(z))
# [(1, 'a'), (2, 'b'), (3, 'c')]    #B

# 动手题
x = [1, 3, 5, 0, -1, 3, -2]
y = filter(lambda x: x > 0, x)
print(y)
# <filter object at 0x000001D57B2FBEE0>
print(list(y))
# [1, 3, 5, 3]
print(tuple(y))
# ()

# 3、列表推导式、字典推导式、生成器表达式
x = [1, 2, 3, 4]
x_squared = []
for item in x:
    x_squared.append(item * item)
print(x_squared)
# [1, 4, 9, 16]

x = [1, 2, 3, 4]
x_squared = [item * item for item in x]
print(x_squared)
# [1, 4, 9, 16]

x = [1, 2, 3, 4]
x_squared = [item * item for item in x if item > 2]
print(x_squared)
# [9, 16]

x = [1, 2, 3, 4]
x_squared_dict = {item: item * item for item in x}
print(x_squared_dict)
# {1: 1, 2: 4, 3: 9, 4: 16}

x = [1, 2, 3, 4]
x_squared = (item * item for item in x)
print(x_squared)
# <generator object <genexpr> at 0x102176708>
for square in x_squared:
    print(square)
# 1 4 9 16

# 动手题
x = [1, 2, 3, 4, -1, 3, -2]
y = [item for item in x if item > 0]
print(y)
# [1, 2, 3, 4, 3]
x = range(1, 100)
y = (item for item in x if (item % 2) != 0)
print(y)
# <generator object <genexpr> at 0x000002986A8F2B50>
print(list(y))
# [1, 3, 5, 7, 9, ..., 99]
x = range(11, 15)
y = [item * item * item for item in x]
print(y)
# [1331, 1728, 2197, 2744]

# 4、语句、块和缩进

x = 1
y = 0
z = 0
if x > 0:
    y = 1
    z = 10
else:
    y = -1
print(x, y, z)
# 1 1 10

# x = 1
# File "<stdin>", line 1
#     x = 1
#     ^
#    IndentationError: unexpected indent

v = 1
x = 1
z = 0
y = 0
if x == 1:
    y = 2
    if v > 0:
        z = 2
        v = 0

x = 1
if x == 1:
    y = 2
# z = 2
# File "<stdin>", line 3
#        z = 2
#        ^
#     IndentationError: unindent does not match any outer indentation level

print("string1", "string2", "string3", "string4", "string5")
# string1 string2 string3 string4 string5
x = 100 + 200 + 300 + 400 + 500
print(x)
# 1500
v = [100, 300, 500, 700, 900, 1100, 1300]
print(v)
# [100, 300, 500, 700, 900, 1100, 1300]
print(max(1000, 300, 500, 800, 1200))
# 1200
x = 100 + 200 + 300 + 400 + 500
print(x)
# 1500

x = "strings separated by whitespace " """are automatically""" " concatenated"
print(x)
# 'strings separated by whitespace are automatically concatenated'
x = 1
if x > 0:
    string1 = "this string broken by a backslash will end up \
                with the indentation tabs in it"
print(string1)
# this string broken by a backslash will end up                 with the indentation tabs in it
if x > 0:
    string1 = "this can be easily avoided by splitting the " "string in this way"
print(string1)
# 'this can be easily avoided by splitting the string in this way'

# 6、布尔值

# 看为true或者false的最终的落脚点
x = [2] and [3, 4]
print(x)
# [3, 4]
x = [] and 5
print(x)
# []
x = [] and 0
print(x)
# []
x = 5 and []
print(x)
# []

x = [2] or [3, 4]
print(x)
# [2]
x = [] or 5
print(x)
# 5
x = 5 or []
print(x)
# 5
x = [] or 0
print(x)
# 0

x = [0]
y = [x, 1]
print(x is y[0])
# True
x = [0]
print(x is y[0])
# False
print(x == y[0])
# True
if 1 > 0 and []:  # false
    print(1)
