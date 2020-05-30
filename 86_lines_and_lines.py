# 85_lines_and_lines.py


def printLine(length):
    for i in range(length):
        print("_", end="")
    print()


def main():
    for i in range(1, 11):
        printLine(i)


# start here
main()
