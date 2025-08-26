# python replace.py zero 0 # 手动标准输入 ctrl+z 回车结束
# python replace.py zero 0 < infile > outfile # 文件中读取
# python replace.py a A < infile >> outfile # 追加
# python replace.py 0 zero < infile | python replace.py 1 one > outfile #管道

import sys
def main():
   contents = sys.stdin.read()                                    #A
   # print(contents) # 这里打印内容会一起输出到outfile
   sys.stdout.write(contents.replace(sys.argv[1], sys.argv[2]))   #B
main()
