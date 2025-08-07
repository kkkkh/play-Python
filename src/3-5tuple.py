x = ('a', 'b', 'c')

# 1、基本操作
# 元组创建完成后，就能像列表一样使用了。
print(x[2])
# 'c'
print(x[1:])
# ('b', 'c')
print(len(x))
# 3
print(max(x))
# 'c'
print(min(x))
# 'a'
print(5 in x)
# False
print(5 not in x)
# True

# 2、元组是不可变的，不能修改元素
# x[2] = 'd'
# Traceback (most recent call last):
#   File "<stdin>", line 1, in <module>
# TypeError: 'tuple' object does not support item assignment

# 3、元组操作符
print(x + x)
# ('a', 'b', 'c', 'a', 'b', 'c')
print(2 * x)
# ('a', 'b', 'c', 'a', 'b', 'c')

print(x[:])
# ('a', 'b', 'c')
print(x * 1)
# ('a', 'b', 'c')
print(x + ())
# ('a', 'b', 'c')

# 4、元组推导式
x = 3
y = 4
print((x + y))    # 此行代码将把x和y相加
# 7
print((x + y,))  # 跟了逗号就意味着，圆括号是用来标识元组的
# (7,)
print(())          # 用成对的空的圆括号创建一个空元组
# ()

# 5、元组 拆包、打包
(one, two, three, four) =  (1, 2, 3, 4)
print("one",one)
one, two, three, four = 1, 2, 3, 4
print("one",one)
# 1
one, two = two, one
print("one",one)
# 2
print("two",two)
# 1

# 注意，带星号的元素会把多余的所有数据项接收为列表。
x = (1, 2, 3, 4)
a, b, *c = x
test = a, b, c
print("a, b, c",test)
# (1, 2, [3, 4])
a, *b, c = x
test = a, b, c
print("a, b, c",test)
# (1, [2, 3], 4)
*a, b, c = x
test = a, b, c
print("a, b, c",test)
# ([1, 2], 3, 4)
a, b, c, d, *e = x
test = a, b, c, d, *e
print("a, b, c, d, e",test)
# (1, 2, 3, 4, [])

# 当遇到列表分隔符时，也会执行打包和拆包操作：
[a, b] = [1, 2]
[c, d] = 3, 4
[e, f] = (5, 6)
(g, h) = 7, 8
i, j = [9, 10]
k, l = (11, 12)
print("a",a)
# 1
print("[b, c, d]",[b, c, d])
# [2, 3, 4]
print("(e, f, g)",(e, f, g))
# (5, 6, 7)
test = h, i, j, k, l
print("test",test)
# (8, 9, 10, 11, 12)

# 6、元组和列表的转换
print(list((1, 2, 3, 4)))
# [1, 2, 3, 4]
print(tuple([1, 2, 3, 4]))
# (1, 2, 3, 4)

print(list("Hello"))
# ['H', 'e', 'l', 'l', 'o']
print(tuple("Hello"))
# ('H', 'e', 'l', 'l', 'o')

# 测试题1 - 增删改元祖
# x = (1, 2, 3, 4)
# 以下操作都会报错
# x.append(1)
# x[1] = "hello"
# del x[2]

# 测试题2 - 元祖排序
x = (3, 1, 4, 2)
x.sort() # 不能直接排序
sorted_x = sorted(x)  # 返回一个排好序的列表 [1, 2, 3, 4]
sorted_x_tuple = tuple(sorted_x)
print(sorted_x_tuple)  # 输出 (1, 2, 3, 4)
