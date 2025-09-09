# 文件系统的使用
# 1、路径
# 1.1、os
import os

# 获取当前工作目录
x = os.getcwd()
print(x)

x = os.listdir(os.getcwd())
print(x)
# 表示当前目录的字符串
x = os.curdir  # 相对路径
print(x)

x = os.listdir()
print(x)

x = os.listdir(os.curdir)
print(x)

# 修改当前工作目录
# os.chdir("./src")  # A
# x = os.getcwd()
# print(x)
# x = os.listdir(os.getcwd())
# print(x)

# 不同操作系统，返回的路径格式不同
x = os.path.join("bin", "utils", "disktools")
print(x)
# bin /utils/disktools

x = os.path.join("mydir\\bin", "utils\\disktools\\chkdisk")
print(x)
# mydir\bin\utils\disktools\chkdisk

path1 = os.path.join("mydir", "bin")
path2 = os.path.join("utils", "disktools", "chkdisk")
print(os.path.join(path1, path2))
# mydir\bin\utils\disktools\chkdisk

print(os.path.split(os.path.join("some", "directory", "path")))
# ('some\\directory', 'path')

x = os.path.basename(os.path.join("some", "directory", "path.jpg"))
print(x)
# 'path.jpg'
x = os.path.dirname(os.path.join("some", "directory", "path.jpg"))
print(x)
# 'some\\directory'

x = os.path.splitext(os.path.join("some", "directory", "path.jpg"))
print(x)
# ("some/directory/path", ".jpg")
x = os.path.splitext(os.path.join("some", "directory", "path"))
print(x)
# ("some/directory/path", "")

x = os.path.commonprefix(("\\aaa\\bbb", "\\aaa\\ccc"))
print(x)
# \\aaa

x = os.path.expanduser("~")
print(x)
# C:\Users\administrator

x = os.path.expandvars("$HOME\\temp")
print(x)
# C:\Users\administrator\temp
print("--------------------------------")
# 1.2、pathlib

import pathlib

cur_path = pathlib.Path()
x = cur_path.cwd()
print(x)

from pathlib import Path

cur_path = Path()
x = cur_path.joinpath("bin", "utils", "disktools")
print(x)
# bin\utils\disktools

x = cur_path / "bin" / "utils" / "disktools"
print(x)
# WindowsPath('bin/utils/disktools')
print(x.parts)
# ('bin', 'utils', 'disktools')

a_path = Path("some", "directory", "path.jpg")
print(a_path.name)
# "path.jpg"
print(a_path.parent)
# some\directory
print(a_path.suffix)
# ".jpg"

# 是否为绝对路径
x = os.path.isabs(os.path.join(os.pardir, "path"))
print(x)
# False

x = os.name
print(x)
# nt

if os.name == "posix":
    root_dir = "/"
elif os.name == "nt":
    root_dir = "C:\\"
else:
    print("Don't understand this operating system!")
import sys

x = sys.platform
print(x)
# win32

# 获取环境变量
# x = os.environ
# print(x)


# 测试题：
# 如何利用os模块中的函数获取test.log文件的路径？
# 并在同一目录下为名为test.log.old的文件新建一个文件路径？
# 如何用pathlib模块完成同样的任务？

# 假设 test.log 文件名（可以是相对路径或绝对路径）
test_log = "test.log"
# 获取 test.log 文件的绝对路径
test_log_abs_path = os.path.abspath(test_log)
print(test_log_abs_path)
# 获取 test.log 所在目录
test_log_dir = os.path.dirname(test_log_abs_path)
# 在同一目录下创建 test.log.old 的路径
test_log_old_path = os.path.join(test_log_dir, "test.log.old")
print("test.log 绝对路径:", test_log_abs_path)
print("test.log.old 路径:", test_log_old_path)

# 假设 test.log 文件
test_log = Path("test.log")
# 获取 test.log 文件的绝对路径
test_log_abs_path = test_log.resolve()
print(test_log_abs_path)
# 获取文件所在目录
test_log_dir = test_log_abs_path.parent
# 在同一目录下创建 test.log.old 路径
test_log_old_path = test_log_dir / "test.log.old"
print("test.log 绝对路径:", test_log_abs_path)
print("test.log.old 路径:", test_log_old_path)

x = Path(os.pardir)
print(x)
# ".."

# 2、文件信息
x = os.path.exists("C:\\Users\\myuser\\My Documents")
print(x)
# False
x = os.path.exists("C:\\Users\\myuser\\My Documents\\Letter.doc")
print(x)
# False
x = os.path.isdir("C:\\Users\\myuser\\My Documents")
print(x)
# True
x = os.path.isfile("C:\\Users\\ myuser\\My Documents")
print(x)
# False
x = os.path.isdir("C:\\Users\\ myuser\\My Documents\\Letter.doc")
print(x)
# False
x = os.path.isfile("C:\\Users\\ myuser\\My Documents\\Letter.doc")
print(x)
# True

print("--------------------------------")
with os.scandir(".") as my_dir:
    for entry in my_dir:
        print(entry.name, entry.is_file())
# pip-selfcheck.json True
# pyvenv.cfg True
# include False
# test.py True
# lib False
# lib64 False
# bin False

# os.scandir不会自动递归到各级子目录
# 如果需要递归子目录，可使用os.walk方法，如：
import os
from os.path import join, getsize

for root, dirs, files in os.walk("."):
    print(root, "consumes")
    # 计算当前目录 root 下所有 非目录文件 的大小总和：
    #   join(root, name) 拼接出文件完整路径
    #   getsize(...) 计算单个文件大小，单位是字节
    #   最外层 sum(...) 把所有文件大小相加
    print(
        sum(getsize(join(root, name)) for name in files),
    )
    print("bytes in", len(files), "non-directory files")
    # 即跳过 "CVS" 目录及其内容。
    if "CVS" in dirs:
        dirs.remove("CVS")  # don't visit CVS directories


# 3、更多操作

# os.chdir(os.path.join("C:", "my documents", "tmp"))
# x = os.listdir(os.curdir)
# print(x)
# ["book1.doc.tmp", "a.tmp", "1.tmp", "7.tmp", "9.tmp", "registry.bkp"]


import glob

x = glob.glob("*")
print(x)
# ["book1.doc.tmp", "a.tmp", "1.tmp", "7.tmp", "9.tmp", "registry.bkp"]
x = glob.glob("*bkp")
print(x)
# ["registry.bkp"]
x = glob.glob("?.tmp")
print(x)
# ["a.tmp", "1.tmp", "7.tmp", "9.tmp"]
x = glob.glob("[0-9].tmp")
print(x)
# ["1.tmp", "7.tmp", "9.tmp"]

# os.rename("registry.bkp", "registry.bkp.old")
# x = os.listdir(os.curdir)
# print(x)
# ['book1.doc.tmp', 'a.tmp', '1.tmp', '7.tmp', '9.tmp', 'registry.bkp.old']

# os.remove("book1.doc.tmp")
# x = os.listdir(os.curdir)
# print(x)
# ['a.tmp', '1.tmp', '7.tmp', '9.tmp', 'registry.bkp.old']

# os.makedirs("mydir")
# x = os.listdir(os.curdir)
# print(x)
# ['mydir', 'a.tmp', '1.tmp', '7.tmp', '9.tmp', 'registry.bkp.old']
# x = os.path.isdir("mydir")
# print(x)
# True

# os.rmdir("mydir")
# x = os.listdir(os.curdir)
# print(x)
# ['a.tmp', '1.tmp', '7.tmp', '9.tmp', 'registry.bkp.old']

new_path = cur_path.joinpath("C:", "Log")
print(
    new_path.iterdir()
)  # iterdir方法类似于os.path.listdir函数，但返回的是路径迭代器而不是字符串列表：
x = list(new_path.iterdir())
print(x)
# [WindowsPath('book1.doc.tmp'), WindowsPath('a.tmp'), WindowsPath('1.tmp'), WindowsPath('7.tmp'), WindowsPath('9.tmp'), WindowsPath('registry.bkp')]

x = list(cur_path.glob("*"))
print(x)
# [WindowsPath('book1.doc.tmp'), WindowsPath('a.tmp'), WindowsPath('1.tmp'), WindowsPath('7.tmp'), WindowsPath('9.tmp'), WindowsPath('registry.bkp')]
x = list(cur_path.glob("*bkp"))
print(x)
# [WindowsPath('registry.bkp')]
x = list(cur_path.glob("?.tmp"))
print(x)
# [WindowsPath('a.tmp'), WindowsPath('1.tmp'), WindowsPath('7.tmp'), WindowsPath('9.tmp')]
x = list(cur_path.glob("[0-9].tmp"))
print(x)
# [WindowsPath('1.tmp'), WindowsPath('7.tmp'), WindowsPath('9.tmp')]

# old_path = Path("registry.bkp")
# new_path = Path("registry.bkp.old")
# old_path.rename(new_path)
x = list(cur_path.iterdir())
print(x)
# [WindowsPath('book1.doc.tmp'), WindowsPath('a.tmp'), WindowsPath('1.tmp'), WindowsPath('7.tmp'), WindowsPath('9.tmp'), WindowsPath('registry.bkp.old')]

# new_path = Path("test")
# new_path.unlink()
# list(cur_path.iterdir())
# [WindowsPath('a.tmp'), WindowsPath('1.tmp'), WindowsPath('7.tmp'), WindowsPath('9.tmp'), WindowsPath('registry.bkp.old')]

# new_path = Path("mydir")
# new_path.mkdir(parents=True)
# list(cur_path.iterdir())
# [WindowsPath('mydir'), WindowsPath('a.tmp'), WindowsPath('1.tmp'), WindowsPath('7.tmp'), WindowsPath('9.tmp'), WindowsPath('registry.bkp.old')]]
# new_path.is_dir('mydir')
# True

# new_path = Path("mydir")
# new_path.rmdir()
# list(cur_path.iterdir())
# [WindowsPath('a.tmp'), WindowsPath('1.tmp'), WindowsPath('7.tmp'), WindowsPath('9.tmp'), WindowsPath('registry.bkp.old']

# 研究题
# 如何计算所有以.txt结尾文件的总大小，符号链接文件除外？
# 如果先用了os.path，请用pathlib再试一遍，反之亦然。
print("--------------------------------")
x = glob.glob("*.txt")
print(x)
y = sum(os.path.getsize(i) for i in x if not os.path.islink(i) and i.is_file())
print(y)

x = list(cur_path.glob("*.txt"))
print(x)
y = sum(getsize(i.name) for i in x if not i.is_symlink() and i.is_file())
# y = sum(i.stat().st_size for i in x if not i.is_symlink())
print(y)


x = list(cur_path.glob("*.txt"))
print(x)
# new_path = Path("APP")
# new_path = cur_path / "APP"
# new_path = cur_path.joinpath("APP")
new_path.mkdir(parents=True, exist_ok=True)

for i in x:
    if not i.is_symlink():
        old_path = Path(i.name)
        new_path = Path(cur_path.joinpath("APP", i.name))
        old_path.rename(new_path)

# 4、walk

import os

for root, dirs, files in os.walk(os.curdir):
    print("{0} has {1} files".format(root, len(files)))
    if ".git" in dirs:  # A
        dirs.remove(".git")  # B
