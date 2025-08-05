# 乘法
"2.2" * 2
# '2.22.2'
"123"*2
# '123123'

"12.2" * 2.2

# Traceback (most recent call last):
#   File "<pyshell#7>", line 1, in <module>
#     "12.2" * 2.2
# TypeError: can't multiply sequence by non-int of type 'float'

"12" * 2.2

# Traceback (most recent call last):
#   File "<pyshell#8>", line 1, in <module>
#     "12" * 2.2
# TypeError: can't multiply sequence by non-int of type 'float'

"12" * 2+1j

# Traceback (most recent call last):
#   File "<pyshell#9>", line 1, in <module>
#     "12" * 2+1j
# TypeError: can only concatenate str (not "complex") to str

"12" * (2+1j)

# Traceback (most recent call last):
#   File "<pyshell#10>", line 1, in <module>
#     "12" * (2+1j)
# TypeError: can't multiply sequence by non-int of type 'complex'

# 加法
"123" + 1

# Traceback (most recent call last):
#   File "<pyshell#11>", line 1, in <module>
#     "123"+1
# TypeError: can only concatenate str (not "int") to str

"12"+1.1

# Traceback (most recent call last):
#   File "<pyshell#12>", line 1, in <module>
#     "12"+1.1
# TypeError: can only concatenate str (not "float") to str

"12"+(2+1j)

# Traceback (most recent call last):
#   File "<pyshell#13>", line 1, in <module>
#     "12"+(2+1j)
# TypeError: can only concatenate str (not "complex") to str

# 除法
"123" /2

# Traceback (most recent call last):
#   File "<pyshell#14>", line 1, in <module>
#     "123" /2
# TypeError: unsupported operand type(s) for /: 'str' and 'int'

"123" /2.2

# Traceback (most recent call last):
#   File "<pyshell#15>", line 1, in <module>
#     "123" /2.2
# TypeError: unsupported operand type(s) for /: 'str' and 'float'
