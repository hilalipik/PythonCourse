import random
import sys
try:

    try:
        start = int(sys.argv[1])
        end = int(sys.argv[2])
    except ValueError:
        print("Could not run the game, please enter numbers as parameters.")
        exit()
    except IndexError:
        print("Could not run the game, please enter 2 parameters.")
        exit()
    
    try:
        num = random.randint(start, end)
    except ValueError:
        print("Could not run the game, make sure the 1st parameter is a lower value than the 2nd.")
        exit()

    while True:
        try:
            guess = int(input(f"Your guess (between {start}-{end}): "))
        except ValueError:
            print("Enter numbers only!")
            continue
        
        if(start <= guess <= end):
            if guess == num:
                print("Congrats! you win!")
                break
        else:
            print("guess out of range.")
            continue
        print("Try again...")
except KeyboardInterrupt:
    print("\nBye!")