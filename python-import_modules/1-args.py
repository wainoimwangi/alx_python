#!/usr/bin/python3
if __name__ == "__main__":
    import sys
# get number of arguments
num = len(sys.argv) - 1
if num == 0:
    end_char = ".\n"
    print("{} arguments".format(num), end=end_char)
elif num == 1:
    end_char = ":\n"
    print("{} argument".format(num), end=end_char)
else:
    end_char = ":\n"
    print("{} arguments".format(num), end=end_char)
for i in range(1, num + 1):
    print("{}: {}".format(i, sys.argv[i]), end="\n")
