is_magician = False
is_expert = False

# Not required, I preferred using input.
is_magician = int(input("Are you a magician? (0 for no, any other kye for yes.)"))
is_expert = int(input("Are you an expert? (0 for no, any other kye for yes.)"))

if is_magician and is_expert:
    print("you are a master magician!")
elif is_magician:
    print("at least you're getting there...")
else:
    print("you need magic powers.")