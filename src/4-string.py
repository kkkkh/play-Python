# 1、索引、切片语法
x = "Hello"
print(x[0])
# 'H'
print(x[-1])
# 'o'
print(x[1:])
# 'ello'

x = "Goodbye\n"
x = x[:-1]
print(x)
# 'Goodbye'

print(len("Goodbye"))
# 7

# 2、拼接字符串
x = "Hello" + "World"
print(x)
# 'Hello World'

print(8 * "x")
# 'xxxxxxxx'

# 3、转义字符

# 3、1
print('m')
# 'm'
print('\155')
# 'm'
print('\x6D')
# 'm'

# 3、2
print('1','\n')
# '\n'
print('2','\012')
# '\n'
print('3','\x0A')
# '\n'

# 3、3
# \N{名称} 来插入具有特定 Unicode 名称的字符
unicode_a ='\N{LATIN SMALL LETTER A}'      #A
print(unicode_a)
# 'a'                                            #1
unicode_a_with_acute = '\N{LATIN SMALL LETTER A WITH ACUTE}'
print(unicode_a_with_acute)
# 'á'
print("\u00E1")                                   #B
# 'á'

# 3、4
'a\n\tb' # 交互式环境下
'a\n\tb'
print('a\n\tb')
# a
#     b
print("abc\n")
# abc
#
print("abc\n", end="")
# abc

# 4、字符串方法
# 4、1、join、split
x = " ".join(["join", "puts", "spaces", "between", "elements"])
print(x)
# 'join puts spaces between elements'

x = "::".join(["Separated", "with", "colons"])
print(x)
# 'Separated::with::colons'

x = "".join(["Separated", "by", "nothing"])
print(x)
# 'Separatedbynothing'

# 在默认情况下，split方法将依据所有空白字符进行拆分，而不仅是一个空格符。
x = "You\t\t can have tabs\t\n \t and newlines \n\n mixed in"
y = x.split()
print(y)
# ['You', 'can', 'have', 'tabs', 'and', 'newlines', 'mixed', 'in']
x = "Mississippi"
y = x.split("ss")
print(y)
# ['Mi', 'i', 'ippi']

x = 'a b c d'
y = x.split(None, 1)
print(y)
# ['a', 'b c d']
y = x.split(' ', 1)
print(y)
# ['a', 'b c d']
y = x.split(' ', 2)
print(y)
# ['a', 'b', 'c d']
x.split(' ', 9)
['a', 'b', 'c', 'd']

x = "this is a test"
y = "-".join(x.split())
print(y)
# 'this-is-a-test'
print(x.replace(" ", "-"))
# 'this-is-a-test'

# 4、2、字符串转换为数值

print(float('123.456'))
# 123.456
# print(float('xxyy'))
# ValueError: could not convert string to float: 'xxyy'
print(int('3333'))
# 3333
# print(int('123.456'))                       #A
# ValueError: invalid literal for int() with base 10: '123.456'
#  File "<stdin>", line 1, in ?
# ValueError: invalid literal for int() with base 10: '123.456'

# int函数还可以接受第二个可选参数，用来指定转换输入的字符串时采用的数值进制
print(int('10000', 8))                   #B
# 4096
print(int('101', 2))
# 5
print(int('ff', 16))
# 255
# print(int('123456', 6))              #C
# ValueError: invalid literal for int() with base 6: '123456'

# print(int('a1'))
# invalid literal for int() with base 10: 'a1'
# print(int('12G', 16))
# invalid literal for int() with base 16: '12G'
print(float("12345678901234567890"))
# 1.2345678901234568e+23
# print(int("12＊2"))
# invalid literal for int() with base 10: '12＊2'

# 4、3、去除多余空白符

x = "  Hello,    World\t\t "
print(x.strip())
# 'Hello,    World'
print(x.lstrip())
# 'Hello,    World\t\t '
print(x.rstrip())
# '  Hello,    World'

import string
print(string.whitespace)
# print 打印不出来，再交互式环境下打印结果如下
# ' \t\n\r\x0b\x0c'
# print 打印不出来，再交互式环境下打印结果如下
print(" \t\n\r\v\f")
# ' \t\n\r\x0b\x0c'

x = "www.python.org"
print(x.strip("w")) #A
# '.python.org'
print(x.strip("gor")) #删除头尾所有的g、o、r字符
# 'www.python.'
print(x.strip(".gorw")) #删除头尾所有的.、g、o、r、w字符
# 'python'

x = "(name, date), \n"
print(x.rstrip("),"))
# (name, date), \n
print(x.strip("),\n"))
# (name, date), 
print(x.strip("\n)(,"))
# name, date), 

# 4、4、字符串搜索

x = "Mississippi"
print(x.find("ss"))
# 2
print(x.find("zz"))
# -1
print(x.find("ss", 3))
# 5
print(x.find("ss", 0, 3))
# -1

print(x.rfind("ss"))
# 5

print(x.count("ss"))
# 2

x = "Mississippi"
print(x.startswith("Miss"))
# True
print(x.startswith("Mist"))
# False
print(x.endswith("pi"))
# True
print(x.endswith("p"))
# False

print(x.endswith(("i", "u")))  # Mississippi 满足一个条件就返回True
# True

# 4、5、字符串修改

x = "Mississippi"
print(x.replace("ss", "+++"))
# 'Mi+++i+++ippi'

# 一次性把多个字符替换为对应字符
x = "~~~~~~x ^ (y % z)"
table = x.maketrans("~^()", "!&[]")
print(x.translate(table))
# '!!!!!!x & [y % z]'

x= "mississippI anDDDDDD"
print(x.capitalize())  # 首字母大写，同时会将其他字母转换为小写
# 'Mississippi anddddddd'
print(x.title())  # 每个单词首字母大写
# 'Mississippi Anddddddd'
print(x.swapcase())  # 大小写互换
# 'MISSISSIPPi ANDDDDDD'
print(x.upper())  # 全部转换为大写
# 'MISSISSIPPI ANDDDDDD'
print(x.lower())  # 全部转换为小写
# 'mississippi anddddddd'
x = '\t\n\t\t\t\t\t'
print(x.expandtabs(1))  # 将1个制表符转换为1个空格
# ' \n     '
print(x.expandtabs(2))  # 将1个制表符转换为2个空格
# '  \n          '

# 4、6、利用列表修改字符串

text = "Hello, World"
wordList = list(text)
wordList[6:] = []                    #A
wordList.reverse()
text = "".join(wordList)
print(text)                          #B
# ,olleH

# 速测题：字符串的修改要把字符串中的所有标点符号替换为空格符，比较快捷的方案是什么？
import string
# 获取所有的标点字符串
print(string.punctuation)
def replace_punctuation_with_space(text):
    """将字符串中所有标点符号替换为空格"""
    translator = str.maketrans(string.punctuation, ' ' * len(string.punctuation))
    return text.translate(translator)

# 使用示例
sample_text = "Hello, world! This is a test-string."
cleaned_text = replace_punctuation_with_space(sample_text)
print(cleaned_text)  # 输出: "Hello  world  This is a test string "

# 4、7、其他方法

x = "123"
print(x.isdigit()) # 是否包含数字
# True
x = "abc"
print(x.isalpha()) # 是否包含字母
# True
x = "M"
print(x.islower()) # 是否全为小写字母
# False
print(x.isupper()) # 是否全为大写字母
# True


print(string.whitespace) # 空格字符串
print(string.digits) # 数字字符串 0 1 2 3 4 5 6 7 8 9
print(string.hexdigits) # 十六进制字符串 0 1 2 3 4 5 6 7 8 9 a b c d e f A B C D E F
print(string.octdigits) # 八进制字符串 0 1 2 3 4 5 6 7
print(string.ascii_lowercase) # 所有小写ASCII字母字符
print(string.ascii_uppercase) # 所有大写ASCII字母字符
print(string.ascii_letters) # 所有ASCII字母字符

# 速测题：将列表中的字符串中的双引号替换为空格
x = ['"abc"', 'def', '"ghi"', '"klm"', 'nop']
print((",".join(x).replace('"','').split(",")))
print(list(map(lambda y: y.replace('"',''), x)))
# ['abc', 'def', 'ghi', 'klm', 'nop']

# 速测题2：如何查找"Mississippi"中最后一个字母p的位置？找到后又该如何只去除该字母呢？
x = "Mississippi"
index = x.rfind("p")
y = x[:index] + x[index+1:]
print(y)
# Mississipi

# 5、将对象转为字符串

print(repr([1, 2, 3]))
# '[1, 2, 3]'
x = [1]
x.append(2)
x.append([3, 4])
print('the list x is ' + repr(x))
# the list x is [1, 2, [3, 4]]
print(repr(len))
# <built-in function len>

# 6、格式化字符串 format
# 6.1
x = "{0} is the {1} of {2}".format("Ambrosia", "food", "the gods") #1
print(x)
# 'Ambrosia is the food of the gods'
x = "{{Ambrosia}} is the {0} of {1}".format("food", "the gods") #2
print(x)
# '{Ambrosia} is the food of the gods'

# 6.2
x = "{food} is the food of {user}".format(food="Ambrosia", user="the gods")
print(x)
# 'Ambrosia is the food of the gods'
x = "{0} is the food of {user[1]}".format("Ambrosia",user=["men", "the gods", "others"])
print(x)
# 'Ambrosia is the food of the gods'

# 6.3
x = "{0:10} is the food of gods".format("Ambrosia")      #1
print(x)
# 'Ambrosia   is the food of gods'
x = "{0:{1}} is the food of gods".format("Ambrosia", 10)   #2
print(x)
# 'Ambrosia   is the food of gods'
x = "{food:{width}} is the food of gods".format(food="Ambrosia", width=10)
print(x)
# 'Ambrosia   is the food of gods'
x = "{0:>10} is the food of gods".format("Ambrosia")         #3
print(x)
# '  Ambrosia is the food of gods'
x = "{0:&>10} is the food of gods".format("Ambrosia")           #4
print(x)
# '&&Ambrosia is the food of gods'

# 自测题
x = "{1:{0}}".format(3, 4)
print(x)
# '  4'
x = "{0:$>5}".format(3)
print(x)
# '$$$$3'
x = "{a:{b}}".format(a=1, b=5)
print(x)
# '    1'
x = "{a:{b}}:{0:$>5}".format(3, 4, a=1, b=5, c=10)
print(x)
# '    1:$$$$3'

# 7、用%格式化字符串

x = "%s is the %s of %s" % ("Ambrosia", "food", "the gods")
print(x)
# 'Ambrosia is the food of the gods'
x = "%s is the %s of %s" % ("Nectar", "drink", "gods")
print(x)
# 'Nectar is the drink of gods'
x = "%s is the %s of the %s" % ("Brussels Sprouts", "food", "foolish")
print(x)
# 'Brussels Sprouts is the food of the foolish'
x = [1, 2, "three"]
x = "The %s contains: %s" % ("list", x)
print(x)
# 'The list contains: [1, 2, 'three']'
# 输出宽度（字符总数）设定为6，将小数点后面的字符数设定为2，并将数字左对齐。
x = "Pi is <%-6.2f>" % 3.14159 # use of the formatting sequence: %–6.2f
print(x)
# 'Pi is <3.14  >'

num_dict = {'e': 2.718, 'pi': 3.14159}
print("%(pi).2f - %(pi).4f - %(e).2f" % num_dict)
# 3.14 - 3.1416 - 2.72

print("a", "b", "c", sep="|")
# a|b|c
print("a", "b", "c", end="\n\n")
# a b c
#
print("a", "b", "c", sep="|", end="\n\n")
# a|b|c
#
# print("a", "b", "c", file=open("testfile.txt", "w"))

# 速测题
x = "%.2f" % 1.1111
print(x)
# '1.11'
x = "%(a).2f" % {'a':1.1111}
print(x)
# '1.11'
x = "%(a).08f" % {'a':1.1111}
print(x)
# '1.11110000'

# 8 字符串内插
value = 42
message = f"The answer is {value}"
print(message)
# The answer is 42

pi = 3.1415
# 当同时指定了字段宽度和精度时，精度指的是 小数点前的位数和小数点后的位数之和，而不是单纯的小数点后的位数。
print(f"pi is {pi:{10}.{2}f}")
# pi is        3.14
print(f"pi is {pi:{10}.{2}}")
# pi is        3.1
print(f"pi is {pi:10.2f}")
# pi is        3.14
print(f"pi is {pi:10.2}")
# pi is        3.1

# 9 Bytes

unicode_a_with_acute = '\N{LATIN SMALL LETTER A WITH ACUTE}'
print(unicode_a_with_acute)
# 'á'
xb = unicode_a_with_acute.encode()    #1
print(xb)
# b'\xc3\xa1'                               #2 
# xb += 'A'                              #3
# Traceback (most recent call last):
#   File "<pyshell#35>", line 1, in <module>
#     xb += 'A'
# TypeError: can't concat str to bytes
x = xb.decode()                           #4
print(x)
# 'á'
print('你好'.encode())
# b'\xe4\xbd\xa0\xe5\xa5\xbd'

# 研究题
with open("./src/moby_01.txt") as infile, open("./src/moby_01_clean.txt", "w") as outfile:
    for line in infile:
        # 全都转成大写或小写
        line = line.upper()
        # 删除标点符号
        line = line.translate(str.maketrans(string.punctuation, ' ' * len(string.punctuation)))
        # 拆分为单词
        words = line.split()
        # 将全部单词按一行写入
        # cleaned_words = " ".join(words)
        # outfile.write(cleaned_words)
        # 将全部单词按每行一个写入
        for word in words:
            outfile.write(word + "\n")
