import re

pattern = re.compile(r"^[a-zA-Z0-9@#$%]{8,}$")

while True:
    print('''- At least 8 characters long.
- Only use a-z, numbers and @#$%.''')
    password = input("Enter password: ")
    valid = pattern.match(password)
    if(valid):
        print("Ok!")
        break
    print("try again...\n")
