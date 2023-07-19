#!/usr/bin/python3
for i in range(100):
    if (i < 99):
        end_char = "," 
    else:
        end_char = " "
    print("{:02d}".format(i), end=end_char)