import sys
from counter import counter

def main():
    if len(sys.argv) == 1:
        try:
            arg = input("What is the text to count?\n")
        except EOFError:
            arg = ""
    elif len(sys.argv) == 2:
        arg = sys.argv[1]
    else:
        raise AssertionError("Please provide only one argument")
    counter(arg)

if __name__ == "__main__":
    main()