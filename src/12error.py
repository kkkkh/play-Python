# 报错处理

# const ERROR = 1;
# const OK = 0;
# int save_to_file(filename) {
#     int status;
#     status = save_prefs_to_file(filename);
#     if (status == ERROR) {
#         ...handle the error...
#     }
#     status = save_text_to_file(filename);
#     if (status == ERROR) {
#         ...handle the error...
#     }
#     status = save_formats_to_file(filename);
#     if (status == ERROR) {
#         ...handle the error...
#     }
#     .
#     .
#     .
# }
# int save_text_to_file(filename) {
#     int status;
#     status = ...lower-level call to write size of text...
#     if (status == ERROR) {
#         return(ERROR);
#     }
#     status = ...lower-level call to write actual text data...
#     if (status == ERROR) {
#         return(ERROR);
#     }
#     .
#     .
#     .
# }


# def save_to_file(filename)
#     try to execute the following block
#         save_text_to_file(filename)
#         save_formats_to_file(filename)
#         save_prefs_to_file(filename)
#         .
#         .
#         .
#     except that, if the disk runs out of space while
#         executing the above block, do this
#         ...handle the error...

# def save_text_to_file(filename)
#     ...lower-level call to write size of text...
#     ...lower-level call to write actual text data...
#     .
#     .
#     .

# 1、raise
alist = [1, 2, 3]
# element = alist[7]
# Traceback (innermost last):
#   File "<stdin>", line 1, in ?
# IndexError: list index out of range


# raise IndexError("Just kidding")
# Traceback (innermost last):
#   File "<stdin>", line 1, in ?
# IndexError: Just kidding

# 2、try except finally
# try:
#     body
# except exception_type1 as var1:
#     exception_code1
# except exception_type2 as var2:
#     exception_code2
#     .
#     .
#     .
# except:
#     default_exception_code
# else:
#     else_body
# finally:
#     finally_body

# 动手题
# try:
#     x = int(input("1"))
#     y = int(input("2"))
#     z = x / y
#     print(z)

# except ZeroDivisionError as e:
#     print("Error", e)
# finally:
#     print("Finally")


# 3、自定义异常


class MyError(Exception):
    pass


# raise MyError("Some information about what went wrong")
# Traceback (most recent call last):
#   File "<stdin>", line 1, in <module>
# __main__.MyError: Some information about what went wrong

# try:
#     raise MyError("Some information about what went wrong")
# except MyError as error:
#     print("Situation:", error)

# try:
#     raise MyError("Some information", "my_filename", 3)
#     # raise Exception("Some information", "my_filename", 3)
# except Exception as e:
#     print("Exception:", e)
# except MyError as error:
#     print("MyError:", error)
#     print(
#         "Situation: {0} with file {1}\n error code: {2}".format(
#             error.args[0], error.args[1], error.args[2]
#         )
#     )

# 4、assert
x = (1, 2, 3)
# assert len(x) > 5
# Traceback (most recent call last):
#   File "<stdin>", line 1, in <module>
# AssertionError: len(x) not > 5

# 动手题
# python -O 12error.py 执行不触发断言
# 14.2.6 Exception inheritance hierarchy

# try:
#     body
# except LookupError as error:
#     exception code
# except IndexError as error:
#     exception code

# 5、正常计算过程中的异常

# def cell_value(string):
#     try:
#         return float(string)
#     except ValueError:
#         if string == "":
#             return 0
#         else:
#             return None


# def safe_apply(function, x, y, spreadsheet):
#     try:
#         return function(x, y, spreadsheet)
#     except TypeError:
#         return None

# 速测题
try:
    y = {}
    y[0] = "Hello"
    print(y[1])
except KeyError as e:
    print("KeyError", e)
x = 1
print(x)

# 6、with 上下文管理器

# try:
#     infile = open(filename)
#     data = infile.read()
# finally:
#     infile.close()


# with open(filename) as infile:
#     data = infile.read()
