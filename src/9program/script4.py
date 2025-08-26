
# python script4.py sole1.tst sole2.tst
import fileinput
def main():
    for line in fileinput.input():
        if not line.startswith('##'):
            print(line, end="")
main()

# 0 0 0
# 0100 0
# 0100100
# 12 15 0
# 100100 0
