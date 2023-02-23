#changed for exercise 20

import random
import sys

def check_guess(guess, correct_answer, start, end):
    if start <= guess <= end:
        if guess == correct_answer:
                return True
    else:
        print("Out of range!")
    return False

def main():
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
                if(check_guess(guess, num, start, end) ):
                    print("Congrats! you win!")
                    break
                else:
                    print("Try again...")
            except ValueError:
                print("Enter numbers only!")
                continue
    except KeyboardInterrupt:
        print("\nBye!")

if __name__ == "__main__":
    main()