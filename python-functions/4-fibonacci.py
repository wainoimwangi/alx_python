#!/usr/bin/env python3
def fibonacci_sequence(n):
    fibonacci_list = []
    a, b = 0, 1

    for _ in range(n):
        fibonacci_list.append(a)
        a, b = b, a + b

    return fibonacci_list

#fibonacci_sequence = __import__('4-fibonacci').fibonacci_sequence
print(fibonacci_sequence(6))
print(fibonacci_sequence(1))
print(fibonacci_sequence(0))
print(fibonacci_sequence(20))