# 排序

# x = [1, 2, 'hello', 3]
# x.sort()
# Traceback (most recent call last):
#   File "<stdin>", line 1, in <module>
# TypeError: '<' not supported between instances of 'str' and 'int'

# 列表的列表
x = [[3, 5], [2, 9], [2, 3], [4, 1], [3, 2]]
x.sort()
print(x)
# [[2, 3], [2, 9], [3, 2], [3, 5], [4, 1]]


# 自定义排序
def compare_num_of_chars(string1):
        return len(string1)
word_list = ['Python', 'is', 'better', 'than', 'C']
word_list.sort()
print(word_list)
# ['C', 'Python', 'better', 'is', 'than']
word_list = ['Python', 'is', 'better', 'than', 'C']
word_list.sort(key=compare_num_of_chars)
print(word_list)
# ['C', 'is', 'than', 'Python', 'better']


# sorted 函数
x = (4, 3, 1, 2)
y = sorted(x)
print(y)
# [1, 2, 3, 4]
z = sorted(x, reverse=True)
print(z)
# [4, 3, 2, 1]


# ：​[​[1, 2, 3], [2, 1, 3], [4, 0, 1]​]​ 得到 ​[​[4, 0, 1], [2, 1, 3], [1, 2, 3]​]​
# lambda
def sort_by_second_element(list_of_lists):
    """
    按每个子列表的第二个元素对列表进行排序。

    参数：
    list_of_lists (list): 包含子列表的列表。

    返回值：
    list: 排序后的列表。
    """
    list_of_lists.sort(key=lambda sublist: sublist[1])
    return list_of_lists
my_list = [[1, 2, 3], [2, 1, 3], [4, 0, 1]]
sorted_list = sort_by_second_element(my_list)
print(sorted_list)
# 输出: [[4, 0, 1], [2, 1, 3], [1, 2, 3]]

# 简单自定义方法
def sort_by_second(sublist):
    return sublist[1]

my_list = [[1, 2, 3], [2, 1, 3], [4, 0, 1]]
my_list.sort(key=sort_by_second)  # 直接修改 my_list
print(my_list)
# 输出: [[4, 0, 1], [2, 1, 3], [1, 2, 3]]

# reverse 倒序
my_list = [[1, 2, 3], [2, 1, 3], [4, 0, 1]]
my_list.reverse()
print(my_list)
# 输出: [[1, 2, 3], [2, 1, 3], [4, 0, 1]]

# sort 倒序
my_list = [[1, 2, 3], [2, 1, 3], [4, 0, 1]]
my_list.sort(reverse=True)
print(my_list)
# 输出: [[1, 2, 3], [2, 1, 3], [4, 0, 1]]

# sorted 倒序
my_list = [[1, 2, 3], [2, 1, 3], [4, 0, 1]]
my_list_sorted = sorted(my_list, reverse=True)
print(my_list_sorted)
# 输出: [[4, 0, 1], [2, 1, 3], [1, 2, 3]]
