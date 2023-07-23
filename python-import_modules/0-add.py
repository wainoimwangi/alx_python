#!/usr/bin/python3
#import module
#from add_0 import add
if __name__ == "__main__":
    import add_0

#define variables
a = 1
b = 2
#create the main function
def main():
    print("{} + {} = {}".format(a, b, add_0.add(a,b)))
#call the main function
main()