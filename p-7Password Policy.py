# Password Policy Validation Engine

import string

# Password policy rules
MIN_LENGTH = 8
MAX_REPEATED = 2
PROHIBITED_SUBSTRINGS = ["password", "admin", "123456"]

def validate_password(password):
    errors = []

    # Check minimum length
    if len(password) < MIN_LENGTH:
        errors.append("Password must contain at least 8 characters.")

    # Check uppercase letters
    if not any(char.isupper() for char in password):
        errors.append("Password must contain at least one uppercase letter.")

    # Check lowercase letters
    if not any(char.islower() for char in password):
        errors.append("Password must contain at least one lowercase letter.")

    # Check digits
    if not any(char.isdigit() for char in password):
        errors.append("Password must contain at least one digit.")

    # Check special characters
    if not any(char in string.punctuation for char in password):
        errors.append("Password must contain at least one special character.")

    # Check repeated consecutive characters
    for i in range(len(password) - MAX_REPEATED):
        if (password[i] == password[i + 1] ==
                password[i + 2]):
            errors.append(
                "Password must not contain 3 consecutive identical characters."
            )
            break

    # Check prohibited substrings (case-insensitive)
    lower_password = password.lower()

    for word in PROHIBITED_SUBSTRINGS:
        if word in lower_password:
            errors.append(
                "Password must not contain the prohibited substring: "
                + word
            )

    # Display validation result
    if errors:
        print("\nPassword: Invalid")
        for error in errors:
            print("-", error)
    else:
        print("\nPassword: Valid")
        print("All password policy rules are satisfied.")

# Main program
print("========== PASSWORD POLICY VALIDATION ==========")

n = int(input("Enter the number of passwords to check: "))

for i in range(n):
    password = input("\nEnter password " + str(i + 1) + ": ")
    validate_password(password)

print("\n========== VALIDATION COMPLETED ==========")