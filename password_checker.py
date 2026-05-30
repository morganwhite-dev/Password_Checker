user_password = input("Enter your password: ")
has_good_length = len(user_password) >= 8
if len(user_password) < 8: 
    print("Your password is too short. It must be at least 8 characters long.")
has_uppercase = False 
has_lowercase = False
has_number = False
has_special_character = False
has_spaces = False
special_characters = "!@#$%^&*()_+-=[]{}|;:,.<>?/`~"

for character in user_password:
    if character.isupper():
        has_uppercase = True
    if character.islower():
        has_lowercase = True
    if character.isdigit():
        has_number = True
    if character.isspace():
        has_spaces = True
    if character in special_characters:
        has_special_character = True

if not has_uppercase: 
    print("Your password must contain at least one uppercase letter.")

   
if not has_lowercase:
    print("Your password must contain at least one lowercase letter.")

if not has_number:
    print("Your password must contain at least one number.")

if not has_special_character:
    print("Your password must contain at least one special character.")

if has_spaces:
    print("Your password cannot contain spaces.")

if has_good_length and has_uppercase and has_lowercase and has_number and has_special_character and not has_spaces:
    print("Your password is strong.")
else: 
    print("Your password is weak. Please try again.")



      