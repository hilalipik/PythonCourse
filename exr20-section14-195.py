import re

pattern = re.compile(r"^[a-zA-Z0-9@#$%]{7,}[0-9]+$")

while True:
    print('''- At least 8 characters long.
- Only use a-z, numbers and @#$%.
- Must end with a number.''')
    password = input("Enter password: ")
    valid = pattern.match(password)
    if(valid):
        print("Ok!")
        break
    print("try again...\n")

