import pyfiglet
import random
attempt=0
min_range=1
max_range=100
ascii_art = pyfiglet.figlet_format("Guess The Number",width=200)
print(ascii_art)
print("Choose level of difficulty......'easy' or 'hard' : ")
try:
    difficult=int(input("Press 1 for easy and 0 for hard:"))
    if difficult==1:
            answer=random.randint(1,50)
            max_range=50
            attempt=10
            print("You have 10 attempts remaining to guess the number")
    elif difficult==0:
            answer=random.randint(1,100)
            max_range=100
            attempt=5
            print("You have 5 attempts remaining to guess the number")
    else:
        print("Invalid Input. Restart the Game")
        exit()
except ValueError:
    print("Invalid Input, Please enter valid input")
    exit()
while attempt>0:
    try:
        guess=int(input(f"Make a Guess (1-{max_range}) "))
        if guess<1 or guess>max_range:
            print(f"OUT OF RANGE,Please entere number between {min_range}-{max_range}")
            continue
        if guess<answer:
            print("Too Low")
            print("Try again")
            attempt-=1
            if attempt>0:
                print(f"You have {attempt} attempts remaining to guess the number")
            else:
                print("No attempts are remaining")
        elif guess>answer:
            print("Too High")
            print("Try again")
            attempt-=1
            if attempt>0:
                print(f"You have {attempt} attempts remaining to guess the number")
            elif attempt==0:
                print("Restart the game")
            else:
                print("No attempts are remaining")
        elif guess==answer:
            print(f"Congratulations!!, You guessed it right in {attempt} attempt")
            break
    except ValueError:
        print("Invalid Input,Please enter a valid number")
if attempt==0 and guess!=answer:
    print("Game Over!. The correct number was {answer}.Better luck next time!.")