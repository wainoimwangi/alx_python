#!/usr/bin/env python3
def validate_password(password):
    # Check if the password is at least 8 characters long
    if len(password) < 8:
        return False

    # Check if the password contains at least one uppercase letter
    if not any(char.isupper() for char in password):
        return False

    # Check if the password contains at least one lowercase letter
    if not any(char.islower() for char in password):
        return False

    # Check if the password contains at least one digit
    if not any(char.isdigit() for char in password):
        return False
    
    # Check if the password contains any spaces
    if ' ' in password:
        return False

    # If all checks pass, the password is valid
    return True
#validate_password = __import__('6-password').validate_password

print(validate_password("Password123"))
print(validate_password("abc123"))
print(validate_password("Password 123"))
print(validate_password("password123"))