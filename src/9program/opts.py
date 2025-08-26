# python opts.py -x100 -q -f outfile 2 arg2
from argparse import ArgumentParser

def main():
    parser = ArgumentParser()
    parser.add_argument("indent", type=int, help="indent for report")  
    parser.add_argument("input_file", help="read data from this file")  #1
    # 两个位置参数indent和input_file，这是在全部可选参数都解析完毕后输入的参数。
    # 位置参数是指那些没有前缀字符（通常是“-”​）且必须给定的参数。
    parser.add_argument("-f", "--file", dest="filename",             #2
                  help="write report to FILE", metavar="FILE")
    parser.add_argument("-x", "--xray",
                  help="specify xray strength factor")
    parser.add_argument("-q", "--quiet",
                  action="store_false", dest="verbose", default=True, #3
                  help="don't print status messages to stdout")

    args = parser.parse_args()

    print("arguments:", args)
main()
# arguments: Namespace(filename='outfile', indent=2, input_file='arg2',verbose=False, xray='100')
