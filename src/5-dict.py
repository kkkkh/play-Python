# 字典
# 1、基本操作
x = []
y = {}
y[0] = 'Hello'
y[1] = 'Goodbye'
# x[0] = 'Hello'
# Traceback (innermost last):
#   File "<stdin>", line 1, in ?
# IndexError: list assignment index out of range
print(y[0])
# Hello
print(y[1] + ", Friend.")
# 'Goodbye, Friend.'
y["two"] = 2
y["pi"] = 3.14
print(y["two"] * y["pi"])
# 6.28

english_to_french = {}                    #A
english_to_french['red'] = 'rouge'          #B
english_to_french['blue'] = 'bleu'
english_to_french['green'] = 'vert'
print("red is", english_to_french['red'])   #C
# red is rouge

# 手动题
# dicts = {}
# for idx in range(1,4):
#   name = input(f"请输入第{idx}个姓名: ")
#   age = input(f"请输入第{idx}个年龄: ")
#   dicts[name] = age
# find_name = input("请输入要查找的姓名: ")
# print(dicts[find_name])

# 2、其他操作
english_to_french = {'red': 'rouge', 'blue': 'bleu', 'green': 'vert'}
print(len(english_to_french))

x = english_to_french.keys()
print(x)
# dict_keys(['red', 'blue', 'green'])
x = list(english_to_french.keys())
print(x)

# ['green', 'blue', 'red']
x = list(english_to_french.values())
print(x)
# ['vert', 'bleu', 'rouge']

x = list(english_to_french.items())
print(x)
# [('green', 'vert'), ('blue', 'bleu'), ('red', 'rouge')]
del english_to_french['green']
x = list(english_to_french.items())
print(x)
#  [('blue', 'bleu'), ('red', 'rouge')]

print('red' in english_to_french)
# True
print('orange' in english_to_french)
# False

print(english_to_french.get('blue', 'No translation'))
# bleu
print(english_to_french.get('chartreuse', 'No translation2'))
# No translation
print(english_to_french.get('chartreuse'))
# None

print(english_to_french.setdefault('chartreuse', 'No translation'))
# No translation
print(english_to_french.setdefault('blue', 'No translation'))
# bleu

x = {0: 'zero', 1: 'one'}
y = x.copy()
print(y)
# {0: 'zero', 1: 'one'}

z = {1: 'One', 2: 'Two'}
x = {0: 'zero', 1: 'one'}
x.update(z)
print(x)
# {0: 'zero', 1: 'One', 2: 'Two'}

# 速测题
x = {'a':1, 'b':2, 'c':3, 'd':4}
y ={'a':6, 'e':5, 'f':6}
del x['d']
print(x)
# {'a': 1, 'b': 2, 'c': 3}
z = x.setdefault('g', 7)
print(x)
# {'a': 1, 'b': 2, 'c': 3, 'g': 7}
print(z)
# 7
x.update(y)
print(x)
# {'a': 6, 'b': 2, 'c': 3, 'g': 7,'e': 5, 'f': 6, }
print(x.keys())
# dict_keys(['a', 'b', 'c', 'g', 'e', 'f'])

# 3、单词计数
sample_string = "To be or not to be"
occurrences = {}
for word in sample_string.split():
     occurrences[word] = occurrences.get(word, 0) + 1   #1

for word in occurrences:
     print("The word", word, "occurs", occurrences[word], \
            "times in the string")

# The word To occurs 1 times in the string
# The word be occurs 2 times in the string
# The word or occurs 1 times in the string
# The word not occurs 1 times in the string
# The word to occurs 1 times in the string
print('--------------------------------')
from collections import Counter

sample_string = "To be or not to be"
occurrences = Counter(sample_string.split())
print(occurrences)
for word in occurrences:
     print("The word", word, "occurs", occurrences[word], \
            "times in the string")

# 4、稀疏矩阵

# matrix = [[3, 0, -2, 11], [0, 9, 0, 0], [0, 7, 0, 0], [0, 0, 0, -5]]
matrix = {(0, 0): 3, (0, 2): -2, (0, 3): 11,(1, 1): 9, (2, 1): 7, (3, 3): -5}
for (rownum, colnum) in matrix:
    print(rownum, colnum)
    print(matrix[(rownum, colnum)])
    print(matrix.get((rownum, colnum),0))
    element = matrix[(rownum, colnum)]
    # element = matrix.get((rownum, colnum),0)
else:
    element = 0

# 5、字典作为缓存
# def sole(m, n, t):
#     # . . . do some time-consuming calculations . . .
#     return(result)
import random
sole_cache = {}
def sole(m, n, t):
    if (m, n, t) in sole_cache:
        print('缓存中...')
        return sole_cache[(m, n, t)]
    else:
        print('计算中...')
        # . . . do some time-consuming calculations . . .
        result = random.randint(1, 100)
        sole_cache[(m, n, t)] = result
        return result
print(sole(1,2,3))
print(sole(1,2,3))

# 研究题：用字典来统计每个单词出现的次数，然后将最常用和最不常用的单词打印出来。
word_count = {}
with open("./src/moby_01_clean.txt") as infile:
  word_count = Counter(map(lambda x:x.strip(),infile))
  # 最常用
  print(word_count.most_common(5))
  # 最不常用：方法1
  print(word_count.most_common()[:-6:-1])
  # 最不常用：方法2
  word_count_list = list(word_count.items())
  word_count_list.sort(key=lambda sublist: sublist[1])
  print(word_count_list[:5])
