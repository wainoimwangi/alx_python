#!/usr/bin/env python3
def convert_to_celsius(fahrenheit):
    result = (fahrenheit - 32) * 5 / 9
    return result
    
#convert_to_celsius = __import__('2-temperature').convert_to_celsius

print(convert_to_celsius(100))
print(convert_to_celsius(-40))
print(convert_to_celsius(-459.67))
print(convert_to_celsius(32))