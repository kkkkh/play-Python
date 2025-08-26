# python script5.py file1 file2
import fileinput
def main():
    for line in fileinput.input():
        if fileinput.isfirstline():
            print("<start of file {0}>".format(fileinput.filename()))
        print(line, end="")
main()
# <start of file file1>
# ......  .     .       ..
# .......................
# <start of file file2>
# .......  .     .       ..
# .......................
