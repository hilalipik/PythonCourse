import re

pattern = re.compile(r"^[a-zA-Z0-9@#$%]{8,}$")

while True:
    print("Enter password:")
    password = input("- At least 8 characters long. Only use a-z, numbers and @#$% -\n")
    valid = pattern.match(password)
    if(valid):
        print("Ok!")
        break

