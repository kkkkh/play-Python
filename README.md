# play-Python

start to study python from 《Python 快速入门》

- [python 3.13 文档](https://docs.python.org/zh-cn/3.13/reference/index.html)

## 1、基础知识
- 缩进、代码块构建：使用缩进、不用大括号
- 注释：#
- 变量、赋值：不是容器、标签
- 表达式：// 整除
- 字符串：`"abc"`、`'abc'`、`"""abc"""`
- 数值：
  - 整数可为任意大小
  - 函数
    - 内置处理函数：abs、divmod、float、hex、int、max、min、oct、pow、round
    - 高级（math模块）：acos、asin、atan、atan2、ceil、cos、cosh、e、exp、fabs、floor、fmod、frexp、hypot、ldexp、log、log10、mod、pi、pow、sin、sinh、sqrt、tan、tanh
    - 复数计算
    - 复数函数(cmath模块)：acos、acosh、asin、asinh、atan、atanh、cos、cosh、e、exp、log、log10、pi、sin、sinh、sqrt、tan、tanh
  - Python中科学计算的基本算法
    - [NumPy](https://numpy.org/) (执行密集型数值计算)
    - [scipy](https://scipy.org/)
- None
- input 输入
- 操作符
- 编码风格：Python增强提案8​（Python Enhancement Proposal 8，PEP 8）

## 2、列表、元组、集合
- 列表
  - 索引、修改、排序、其他操作、深拷贝
- 元组
- 集合

## 3、字符串
- 索引、切片、拼接、转义字符、
- 其他方法：join、split、转换为数值、strip去除空白符（lstrip、rstrip）、find搜索（rfind）、startswith、endswith、replace替换、maketrans多个字符对应替换translate、等等
- 其他操作：repr对象转为字符串、格式化字符串format（新）、用%格式化字符串（旧）、encode

## 4、字典
- 字典获取 keys、values、items、
- get获取对应key的值、setdefault设置默认值、
- copy拷贝一个字典、update更新合并、
- 稀疏矩阵、用作缓存

## 5、流程控制
- if elseif else
- for循环：range函数、元组拆包、enumerate、zip合并
- 列表推导式`[]`、字典推导式`{}`、生成器表达式`()`
- `and` `or` `is` `==` `!=` `not`

## 6、函数
- def、参数、形参、默认值、
- 实参
  - 参数数量不定：*（返回元组）、**（返回字典）、
  - 对象用作函数实参
- 全局变量global、非局部变量nonlocal
- lambda、Generator、Decorators

## 7、模块
- import mymath
- from mymath import pi
- 命名空间
  - locals() 当前全局作用域的变量名和值字典
  - globals() 前局部作用域的变量名和值字典
  - dir()返回给定模块中定义的对象名称列表

## 8、程序
- sys.argv
- from argparse import ArgumentParser
- sys.stdin.read()、sys.stdout.write()
- import fileinput
- def main():
  ```python
  if __name__ == "__main__":
      main()
  ```
## 9 文件系统的使用
- os(旧)：
  - os.getcwd、os.listdir、os.curdir
  - os.path.join、os.path.split、os.path.basename、os.path.dirname、os.path.splitext、os.path.commonprefix、os.path.isabs等等
  - os.path.exists、os.path.isdir、os.path.isfile、os.path.getsize、islink
  - glob.glob("*")
  - os.walk
- pathlib（新）：
  - `cur_path = pathlib.Path()`
  - cur_path.cwd()、cur_path.joinpath、cur_path / "bin"
  - cur_path.parts、cur_path.name、cur_path.parent、cur_path.suffix
  - cur_path.resolve()、iterdir、cur_path.glob、
  - is_file、is_symlink
