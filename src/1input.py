# 整数不允许输入浮点数
int(input("?"))
# ?22.2

# Traceback (most recent call last):
#   File "<pyshell#3>", line 1, in <module>
#     int(input(1))
# ValueError: invalid literal for int() with base 10: '22.2'

# 整数允许输入整数
int(input("?"))
# ?22
# 22

# 浮点数允许输入浮点数
float(input("?"))
# ?2222.22
# 2222.22

# 浮点数允许输入整数
float(input("?"))
# ?222
# 222.0
