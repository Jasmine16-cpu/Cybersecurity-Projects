import re

def check_password_strength(temp):
    length_criteria = len(temp) >= 8
    uppercase_criteria = bool(re.search(r'[A-Z]', temp))
    lowercase_criteria = bool(re.search(r'[a-z]', temp))
    digit_criteria = bool(re.search(r'[0-9]', temp))
    symbols_criteria = bool(re.search(r'[!@#$%^&*()_+]', temp))

    if length_criteria and uppercase_criteria and lowercase_criteria and digit_criteria and symbols_criteria:
        return "Strong"
    elif length_criteria and (uppercase_criteria or lowercase_criteria) and symbols_criteria:
        return "Moderate"
    else:
        return "Weak"

if __name__ =="__main__":
    while True:
        password = input("Enter password:")
        strength = check_password_strength(password)
        print(f"Your password strength is:{strength}")

        if strength == 'Strong':
            break








