#!/usr/bin/python3
for i in range(100):
    end_char = ", " if i < 99 else ""
    print("{:02d}".format(i), end=end_char)
