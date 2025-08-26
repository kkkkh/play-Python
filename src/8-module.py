# 模块 module

# pi
# Traceback (innermost last):
#   File "<stdin>", line 1, in ?
# NameError: name 'pi' is not defined
# area(2)
# Traceback (innermost last):
#   File "<stdin>", line 1, in ?
# NameError: name 'area' is not defined


import mymath

# pi
# Traceback (innermost last):
#   File "<stdin>", line 1, in ?
# NameError: name 'pi' is not defined
print(mymath.pi)
# 3.14159
print(mymath.area(2))
# 12.56636
print(mymath.__doc__)
# 'mymath - our example math module'
print(mymath.area.__doc__)
# 'area(r): return the area of a circle with radius r.'


from mymath import pi

print(pi)
# 3.14159
# print(area(2))
# Traceback (innermost last):
#   File "<stdin>", line 1, in ?
# NameError: name 'area' is not defined


import mymath, importlib

x = importlib.reload(mymath)
print(x)
# <module 'mymath' from '/home/doc/quickpythonbook/code/mymath.py'>

import sys

print(sys.path)
# _list of directories in the search path_


# 5 私有

from modtest import *

print(f(3))
# 3
# print(_g(3))
# Traceback (innermost last):
#   File "<stdin>", line 1, in ?
# NameError: name '_g' is not defined
print(a)
# 4
# print(_b)
# Traceback (innermost last):
#   File "<stdin>", line 1, in ?
# NameError: name '_b' is not defined

import modtest

print(modtest._b)
# 2
from modtest import _g

print(_g(5))
# 5

# 2	命名空间
print(locals())
# {'__builtins__': <module 'builtins' (built-in)>,
# '__name__': '__main__',
# '__doc__': None,
# '__package__': None}
print(globals())
# {'__builtins__': <module 'builtins' (built-in)>,
# '__name__': '__main__',
# '__doc__': None,
# '__package__': None}

z = 2
import math
from cmath import cos

print(globals())
# {'cos': <built-in function cos>, '__builtins__': <module 'builtins'
# (built-in)>, '__package__': None, '__name__': '__main__', 'z': 2,
# '__doc__': None, 'math': <module 'math' from
# '/usr/local/lib/python3.0/libdynload/math.so'>}
locals()
# {'cos': <built-in function cos>, '__builtins__':
# <module 'builtins' (built-in)>, '__package__': None, '__name__':
# '__main__', 'z': 2, '__doc__': None, 'math': <module 'math' from
# '/usr/local/lib/python3.0/libdynload/math.so'>}
print(math.ceil(3.4))
# 4


del z, math, cos
print(locals())
# {'__builtins__': <module 'builtins' (built-in)>, '__package__': None,
# '__name__': '__main__', '__doc__': None}
# math.ceil(3.4)
# Traceback (innermost last):
#   File "<stdin>", line 1, in <module>
# NameError: math is not defined
import math

print(math.ceil(3.4))
# 4

print("--------------------------------")


def f(x):
    print(globals())
    print("Entry local: ", locals())
    y = x
    print("Exit local: ", locals())


z = 2
print(globals())
# {'f': <function f at 0xb7cbfeac>, '__builtins__': <module 'builtins'
# (built-in)>, '__package__': None, '__name__': '__main__', 'z': 2,
# '__doc__': None}
f(z)
# global:  {'f': <function f at 0xb7cbfeac>, '__builtins__': <module
# 'builtins' (built-in)>, '__package__': None, '__name__': '__main__',
# 'z': 2, '__doc__': None}
# Entry local:  {'x': 2}
# Exit local:  {'y': 2, 'x': 2}

import scopetest

z = 2
scopetest.f(z)
# global:  ['__name__', '__doc__', '__package__', '__loader__', '__spec__', '__file__', '__cached__', '__builtins__', 'v', 'f']
# entry local: {'x': 2}
# exit local: dict_keys(['x', 'w', 'y'])


print(max.__doc__)
# max(iterable[, key=func]) -> value
# max(a, b, c, [, key=func]) -> value

# With a single iterable argument, return its largest item.
# With two or more arguments, return the largest argument.


print(list("Peyto Lake"))
# ['P', 'e', 'y', 't', 'o', ' ', 'L', 'a', 'k', 'e']
list = [1, 3, 5, 7]
# print(list("Peyto Lake"))
# Traceback (innermost last):
#   File "<stdin>", line 1, in ?
# TypeError: 'list' object is not callable


import mymath

mymath = mymath.area
# mymath.pi
# Traceback (most recent call last):
#   File "<stdin>", line 1, in <module>
# AttributeError: 'function' object has no attribute 'pi'


del list
print(list("Peyto Lake"))
# ['P', 'e', 'y', 't', 'o', ' ', 'L', 'a', 'k', 'e']
import mymath

print(mymath.pi)
3.14159


x1 = 6
xl = x1 - 2
print(x1)
# 6
print(dir())  # 返回当前命名空间中定义的对象名称列表
# ['__annotations__', '__builtins__', '__doc__', '__loader__', '__name__', '__package__', '__spec__', 'x1', 'xl']
