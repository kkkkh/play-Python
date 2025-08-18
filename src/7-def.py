# def
# 1、函数
def fact(n): 
     """Return the factorial of the given number."""            #1
     r = 1
     while n > 0:
         r = r * n
         n = n - 1
     return r                                      #2
x = fact(4)                        #3
print(x)
# 24

# 2、参数
# 2.1 形参
def power(x, y):
     r = 1
     while y > 0:
         r = r * x
         y = y - 1
     return r
x = power(3, 3)
print(x)
# 27
# power(3)
# Traceback (most recent call last):
#   File "<stdin>", line 1, in <module>
# TypeError: power() missing 1 required positional argument: 'y'

# 2.2 默认值
def power(x, y=2):
     r = 1
     while y > 0:
         r = r * x
         y = y - 1
     return r

x = power(3, 3)
print(x)
# 27
x = power(3)
print(x)
# 9

x = power(2, 3)
print(x)
# 8
x = power(3, 2)
print(x)
# 9
x = power(y=2, x=3)
print(x)
# 9

def list_file_info(size=False, create_date=False, mod_date=False ):
    # get file names
    if size:
        # code to get file sizes goes here
        pass
    if create_date:
        # code to get create dates goes here
        pass
    # do any other stuff desired
    fileinfostructure = 123
    return fileinfostructure

fileinfo = list_file_info(size=True, mod_date=True)
print(fileinfo)
# 2.3 参数量不定时的处理  (* 返回的是元组)
def maximum(*numbers):  
    #  寻找最大值
     print(numbers) # 是一个元组
     if len(numbers) == 0:
        return None
     else:
         maxnum = numbers[0]
         for n in numbers[1:]:
             if n > maxnum:
                 maxnum = n
         return maxnum


x = maximum(3, 2, 8)
print(x)
# 8
x = maximum(1, 5, 9, -2, 2)
print(x)
# 9

# 2.4 参数量不定时的处理  (** 返回的是字典)
def example_fun(x, y, **other):
     print("x: {0}, y: {1}, keys in 'other': {2}".format(x, 
           y, list(other.keys())))
     other_total = 0
     for k in other.keys():
         other_total = other_total + other[k]
     print("The total of values in 'other' is {0}".format(other_total))


example_fun(2, y="1", foo=3, bar=4)
# x: 2, y: 1, keys in 'other': ['foo', 'bar']
# The total of values in 'other' is 7

# 速测题目
def reversedPrint (*numbers):
    print(*reversed(numbers))
    # print(*[1,2,3,4])
reversedPrint(1,2,3,410,9,89)

# 3、将可变对象用作函数实参
def f(n, list1, list2):
    list1.append(3)
    list2 = [4, 5, 6]
    n = n + 1

x = 5
y = [1, 2] # 只有y收到了影响
z = [4, 5]
f(x, y, z)
print(x, y, z)
# (5, [1, 2, 3], [4, 5])

# 4、全局变量
# 局部变量
def fact(n):
    """Return the factorial of the given number."""
    r = 1
    while n > 0:
        r = r * n
        n = n - 1
    return r

def fun():
     global a
     a = 1
     print("fun b",b) # 闭包
    #  b = 2

a = "one"
b = "two"

fun()
print(a)
# 1
print(b)
# 'two'

g_var = 0
nl_var = 0 #innertest函数中的gvar绑定为同名的顶级变量
print("top level-> g_var:{0} nl_var:{1}".format(g_var, nl_var))
def test():
    nl_var = 2 #  inner_test函数中的nlvar绑定为test函数中的同名变量
    print("in test->g_var:{0} nl_var:{1}".format(g_var,nl_var))
    def innertest():
        global g_var # innertest函数中的g_var绑定为同名的顶级变量
        nonlocal nl_var #inner_test函数中的nlvar绑定为test函数中的同名变量
        print("in inner test-> g var: {0} nl var: {1}".format(g_var,nl_var))
        g_var = 1
        nl_var =4
        print("in inner test-> g var: {0} nl var: {1}".format(g_var,nl_var))
    innertest()
    print("in test->g_var:{0} nl_var:{1}".format(g_var,nl_var))
test()
print("toplevel-> gvar: {0} nl_var: {1}".format(g_var,nl_var))

# top level-> g_var: 0 nl_var: 0
# in test-> g_var: 0 nl_var: 2
# in inner test-> g var: 0 nl var: 2
# in inner_test-> g_var: 1 nl_var: 4
# in test-> g_var: 1 nl_var: 4
# top level-> g_var: 1 nl_var: 0

# 动手题
x = 5
def funct_1():
    x = 3
def funct_2():
    global x
    x = 2

funct_1()
print(x)
funct_2()
print(x)

# 5 将函数赋给变量

def f_to_kelvin(degrees_f):                     #A
     return 273.15 + (degrees_f - 32) * 5 / 9

def c_to_kelvin(degrees_c):                      #B
     return 273.15 + degrees_c

abs_temperature = f_to_kelvin                    #C
x = abs_temperature(32)
print(x)
# 273.15
abs_temperature = c_to_kelvin                      #D
x= abs_temperature(0)
print(x)
# 273.15

t = {'FtoK': f_to_kelvin, 'CtoK': c_to_kelvin}      #1
x = t['FtoK'](32)                                       #A
print(x)
# 273.15
x = t['CtoK'](0)                                        #B
print(x)
# 273.15

# 6 lambda

t2 = {
    'FtoK': lambda deg_f: 273.15 + (deg_f - 32) * 5 / 9, #1 
    'CtoK': lambda deg_c: 273.15 + deg_c
}                #1
x = t2['FtoK'](32)
print(x)
# 273.15

# 7 Generator
def four():
     x = 0                                    #A
     while x < 4:
         print("in generator, x =", x)
         yield x                               #B
         x += 1                               #C

for i in four():
    print(i)
# in generator, x = 0
# 0
# in generator, x = 1
# 1
# in generator, x = 2
# 2
# in generator, x = 3
# 3

def subgen(x):
    for i in range(x):
        yield i
def gen(y):
       yield from subgen(y)
for q in gen(6):
       print(q)
# 0
# 1
# 2
# 3
# 4
# 5

print(2 in four())
# in generator, x = 0
# in generator, x = 1
# in generator, x = 2
# True
print(5 in four())
# in generator, x = 0
# in generator, x = 1
# in generator, x = 2
# in generator, x = 3
# False

# 速测题
def range_x(max):
    for e in range(max + 1):
        yield e
print(1 in range_x(5))
print(5 in range_x(5))
print(6 in range_x(5))
print(6 in range_x(10))

# 8、 Decorators

def decorate(func):
     print("in decorate function, decorating", func.__name__)
     def wrapper_func(*args):
         print("Executing", func.__name__)
         return func(*args)
     return wrapper_func

def myfunction(parameter):
     print(parameter)

myfunction = decorate(myfunction)
# in decorate function, decorating myfunction
myfunction("hello")
# Executing myfunction
# hello


def decorate(func):
     print("in decorate function, decorating", func.__name__)  #1
     def wrapper_func(*args):
        print("Executing", func.__name__)
        # 动手题
        args = map(lambda x: "<html>" + x + "</html>", args)
        return func(*args)
     return wrapper_func                                       #2

@decorate                                                     #3
def myfunction(parameter):
    print(parameter)

# in decorate function, decorating myfunction                      #4
myfunction("hello")
# Executing myfunction
# hello
