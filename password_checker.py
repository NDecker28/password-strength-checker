def has_min_length(password):
    return len(password) >= 8

def has_uppercase(password):
    for char in password:
        if char.isupper():
            return True
    return False

def has_number(password):
    for char in password:
        if char.isdigit():
            return True
    return False

SPECIAL_CHARACTERS = "!@#$%^&*()_-+="

def has_special_character(password):
    for char in password:
        if char in SPECIAL_CHARACTERS:
            return True
    return False

password = input("Enter a password: ")

score = 0

if has_min_length(password):
    score += 1
if has_number(password):
    score += 1
if has_uppercase(password):
    score += 1
if has_special_character(password):
    score += 1

if score <= 1:
    print("Password strength: WEAK")
elif score == 2 or score == 3:
    print("Password strength: MEDIUM")
else:
    print("Password strength: STRONG")