import re

def check_password_strength(password):
    # Criteria
    length = len(password) >= 8
    uppercase = re.search(r"[A-Z]", password)
    lowercase = re.search(r"[a-z]", password)
    digit = re.search(r"\d", password)
    special_char = re.search(r"[ !#$%&'()*+,-./[\\\]^_`{|}~""]", password)

    # Check if all criteria are met
    if length and uppercase and lowercase and digit and special_char:
        return "Strong"
    else:
        return "Weak"

while True:
    password = input("Enter your password: ")
    strength = check_password_strength(password)
    print("Your password strength is:", strength)

    choice = input("Do you want to check another password? (yes/no): ")
    if choice.lower() != "yes":
        break
