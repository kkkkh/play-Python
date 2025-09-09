# 1 打开文件
with open("myfile", "r") as file_object:
    line = file_object.readline()
    print(line)
    line = file_object.readline()
    print(line)

# import os
# file_name = os.path.join("c:", "My Documents", "test", "myfile")
# file_object = open(file_name, 'r')

# 2 关闭文件
file_object = open("myfile", "r")
line = file_object.readline()
print(line)
# . . . any further reading on the file_object . . .
file_object.close()

with open("myfile", "r") as file_object:
    line = file_object.readline()
# . . . any further reading on the file_object . .

# 3、写入文件
file_object = open("myfile", "w")
file_object.write("Hello, World\n")
file_object.close()

# 4 二进制
## readline
file_object = open("myfile", "r")
count = 0
while file_object.readline() != "":
    count = count + 1
print(count)
file_object.close()
## readlines
file_object = open("myfile", "r")
print(len(file_object.readlines()))
file_object.close()
## for in
file_object = open("myfile", "r")
count = 0
for line in file_object:
    count = count + 1
print(count)
file_object.close()
## rb read
input_file = open("myfile", "rb")
header = input_file.read(4)
print(header)
# b'Hell'
data = input_file.read()
print(data)
# b'o, World\r\n'
input_file.close()
# readlines -> writelines
input_file = open("myfile", "r")
lines = input_file.readlines()
input_file.close()
output = open("myfile2.txt", "w")
output.writelines(lines)
output.close()

# 5、pathlib
from pathlib import Path

p_text = Path("my_text_file")
p_text.write_text("Text file contents")
# 18
x = p_text.read_text()
print(x)
# 'Text file contents'
p_binary = Path("my_binary_file")
p_binary.write_bytes(b"Binary file contents")
x = p_binary.read_bytes()
print(x)
# b'Binary file contents'

# 6 input/output
# x = input("enter file name to use: ")
# # enter file name to use: myfile
# print(x)
# # 'myfile'

# x = int(input("enter your number: "))
# # enter your number: 39
# print(x)
# # 39

# 7、标准输入、输出重定向
# python 11file.py > myfile < myfile
# python 11file.py < myfile
# python 11file.py

# import sys
# print("Write to the standard output.")
# # Write to the standard output.
# sys.stdout.write("Write to the standard output.\n")
# # Write to the standard output.
# # 30 # 在IDLE会显示                                             #A
# s = sys.stdin.readline()  # 输入内容 + \n
# # An input line
# print("222" + "1")
# print(s + "1")
# # 'An input line\n'

## 重置sys.stdout
# import sys
# f = open("outfile.txt", "w")
# sys.stdout = f
# sys.stdout.writelines(["A first line.\n", "A second line.\n"])  # A
# print("A line from the print function")
# 3 + 4  # B
# sys.stdout = sys.__stdout__
# f.close()
# 3 + 4
# # 7

## print传参file
# import sys
# f = open("outfile.txt", "w")
# print("A first line.\n", "A second line.\n", file=f)  # A
# 3 + 4
# 7
# f.close()
# 3 + 4
# 7

print("--------------------------------")
# 7 struct
# import struct

# record_format = "hd4s"
# record_size = struct.calcsize(record_format)
# print("record_size", record_size)
# # 20
# result_list = []
# i = 0
# with open("index.exe", "rb") as f:
#     while i < 20:
#         i += 1
#         record = f.read(record_size)
#         print(record)
#         # b'MZ\x90\x00\x03\x00\x00\x00\x04\x00\x00\x00\xff\xff\x00\x00\xb8\x00\x00\x00'
#         # b'\x00\x00\x00\x00@\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'
#         if len(record) < record_size:  # 防止最后不足一条记录
#             break
#         result_list.append(struct.unpack(record_format, record))
# print(result_list)
# # [(23117, 1.39064994160911e-309, b'\xb8\x00\x00\x00'), (0, 0.0, b'\x00\x00\x00\x00'), (0, 0.0, b'\x00\x00\x00\x00'),...]

# import struct

# record_format = "hd4s"
# x = struct.pack(record_format, 7, 3.14, b"gbye")
# print(x)
# # b"\x07\x00\x00\x00\x00\x00\x00\x00\x1f\x85\xebQ\xb8\x1e\t@gbye"


# 8 Pickle

# import pickle
# .
# .
# .
# file = open("state", 'wb')
# pickle.dump(a, file)
# pickle.dump(b, file)
# pickle.dump(c, file)
# file.close()

# import pickle
# file = open("state", 'rb')
# a = pickle.load(file)
# b = pickle.load(file)
# c = pickle.load(file)
# file.close()


# import pickle
# .
# .
# .
# def save_data():
#     global a, b, c
#     file = open("state", 'w')
#     data = {'a': a, 'b': b, 'c': c}
#     pickle.dump(data, file)
#     file.close()

# def restore_data():
#     global a, b, c
#     file = open("state", 'r')
#     data = pickle.load(file)
#     file.close()
#     a = data['a']
#     b = data['b']
#     c = data['c']
#     .
#     .

# 初始化文件，方便sole.py启用
# import pickle
# file = open("solecache",'wb')
# pickle.dump({}, file)
# file.close()

# 9 Shelve

import shelve

book = shelve.open("addresses")

book["flintstone"] = ("fred", "555-1234", "1233 Bedrock Place")
book["rubble"] = ("barney", "555-4321", "1235 Bedrock Place")


book.close()


book = shelve.open("addresses")

print(book["flintstone"])
# ('fred', '555-1234', '1233 Bedrock Place')
