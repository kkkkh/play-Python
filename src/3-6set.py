# 1、集合
x = set([1,2,3,1,3,5])
print(x)
# {1, 2, 3, 5}
x.add(6)
print(x)
# {1, 2, 3, 5, 6}
x.remove(5)
print(x)
# {1, 2, 3, 6}
test = 1 in x
print(test)
# True
test = 4 in x
print(test)
# False

v = set([1,7,8,9])
test = x | v # 并集
print(test)
# {1, 2, 3, 6, 7, 8, 9}
test = x & v # 交集
print(test)
# {1}
test = x - v # x有，v没有
print(test)
# {2, 3, 6}
test = x ^ v # 对称差（symmetric difference）​。
# 对称差是指，属于其中一个但不同时属于两个集合的元素。
print(test)
# {2, 3, 6, 7, 8, 9}


# 2、不可变集合

x = set([1, 2, 3, 1, 3, 5])
z = frozenset(x)
print(z)
# frozenset({1, 2, 3, 5})
# z.add(6)
# Traceback (most recent call last):
#   File "<pyshell#79>", line 1, in <module>
#     z.add(6)
# AttributeError: 'frozenset' object has no attribute 'add'
x.add(z)
print(x)
# {1, 2, 3, 5, frozenset({1, 2, 3, 5})}

# 测试题1
test = set([1, 2, 5, 1, 0, 2, 3, 1, 1, (1, 2, 3)])
print(test)
# {0, 1, 2, 3, 5, (1, 2, 3)}
print(len(test))
# 6

# 测试题2
temperatures = []
with open('./src/lab_05.txt') as infile:
    for row in infile:
      # row.strip() 去除字符串首尾的空白字符
      # float(row.strip()) 将字符串转换为浮点数
      # int(...)：将字符串转换为整数
      temperatures.append(float(row.strip()))
print(temperatures)

min_temp = min(temperatures)
print("min_temp",min_temp)
max_temp = max(temperatures)
print("max_temp",max_temp)

len_temperatures = len(temperatures)
print("len_temperatures",len_temperatures)
# 平均温度和中位数温度
average_temp = sum(temperatures) / len_temperatures
print("average_temp",average_temp)

# 中位数温度
median_temp = sorted(temperatures)[len_temperatures // 2]
print("median_temp",median_temp)

# 列表中有多少个温度值是唯一的
# 第一种思路
# temperatures = [1,2,3,4,5,6,7,8,9,10,1]
unique_temperatures = len(temperatures) - (len(temperatures) - len(set(temperatures)) )* 2 # 原始公式
# unique_temperatures = len(temperatures) - (len(temperatures)*2 - len(set(temperatures)) * 2)
# unique_temperatures = len(temperatures) - len(temperatures)*2 + len(set(temperatures)) * 2
# unique_temperatures = - len(temperatures) + len(set(temperatures)) * 2
# unique_temperatures = len(set(temperatures)) * 2 - len(temperatures) # 最终简化公式
# print(len(set(temperatures)))
# print(len(temperatures))
unique_temperatures = len(set(temperatures)) * 2 - len(temperatures)

print("unique_temperatures",unique_temperatures)
# 当temtemperatures的重复的1不知道出现多了多少次时候，这种方法就行不通了
# temperatures = [1,2,3,4,5,6,7,8,9,10,1，1,1,1,1,1,1,1,1,1,1,1]
# 原始公式 (len(temperatures) - len(set(temperatures)) )* 2 是认为1出现了2次，现在1重复了多次，就不行了
# 另外一种思路就是：可以用总长度减所有重复元素的重复次数，再加上set的长度，就是唯一值的个数

# 第二种思路
# 遍历列表，用一个字典统计每个元素出现的次数。
# 再遍历统计字典，数出现次数为1的元素个数。
def count_unique_once(lst):
    counts = {}
    for item in lst:
        if item in counts:
            counts[item] += 1
        else:
            counts[item] = 1
    # 实现1
    # unique_once_count = 0
    # for _key, val in counts.items():
    #     if val == 1:
    #         unique_once_count += 1

    # return unique_once_count
    # 实现2
    # return sum(1 for val in counts.values() if val == 1)
    # 实现3
    return len(list(filter(lambda x: x == 1, counts.values())))

# 测试
lst = [1, 2, 2, 2,2,2,2,2,2,2,2,3, 4, 4, 5,10,89,4,4,4,4]
print(count_unique_once(lst))  # 输出 3，唯一值为 1,3,5
print(count_unique_once(temperatures))  # 输出 3，唯一值为 1,3,5


