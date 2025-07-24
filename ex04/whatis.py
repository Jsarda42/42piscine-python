import sys

if len(sys.argv) < 2:
    raise AssertionError("argument missing")
elif len(sys.argv) > 2:
    raise AssertionError("more than one argument is provided")
arg = sys.argv[1]
try:
    num = int(arg)
except ValueError:
    raise AssertionError("argument is not an integer")
if num % 2 == 0:
    print("I'm Even.")
else:
    print("I'm Odd.")




