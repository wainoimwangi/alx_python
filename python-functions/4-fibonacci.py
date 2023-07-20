#!/usr/bin/env python3
def fibonacci_sequence(n):
    fibonacci_list = []
    a, b = 0, 1

    for _ in range(n):
        fibonacci_list.append(a)
        a, b = b, a + b

    return fibonacci_list

