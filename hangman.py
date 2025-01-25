from words import words
import random
hangman_art = {0: ("   ",
                                   "   ",
                                   "   "),
                             1: (" o ",
                                   "   ",
                                   "   "),
                             2: (" o ",
                                   " | ",
                                   "   "),
                             3: (" o ",
                                   "/| ",
                                   "   "),
                             4: (" o ",
                                  "/|\\",
                                   "   "),
                              5: (" o ",
                                   "/|\\",
                                   "/  "),
                              6: (" o ",
                                   "/|\\",
                                   "/ \\")}
def display_man(wrong_guess):
    print("************")
    for line in hangman_art[wrong_guess]:
        print(line)
    print("************")
def display_hint(hint):
    print(" ".join(hint))

def display_answer(answer):
   print(" ".join(answer))

def main():
    print("########## WELCOME TO HANG-MAN GAME ###########")
    print("_____________________________________________")
    answer=random.choice(words)
    hint=["_"]*len(answer)
    wrong_guess=0
    guessed_letter=set()
    is_running=True
    
    while is_running:
        display_man(wrong_guess)
        display_hint(hint)
        guess=input("Enter a letter ").lower()
        if len(guess)!=1 or not guess.isalpha():
            print("Invalid Input")
            continue
        if guess in guessed_letter:
            print(f"{guess} is already guessed")
            continue
        guessed_letter.add(guess)
        if guess in answer:
            for i in range(len(answer)):
                if answer[i]==guess:
                    hint[i]=guess
        else:
            wrong_guess+=1
        if "_" not in hint:
            display_man(wrong_guess)
            display_answer(answer)
            print("You Win")
            is_running=False
        elif wrong_guess>=len(hangman_art)-1:
            display_man(wrong_guess)
            display_answer(answer)
            print("You Lose!")
            is_running=False
            
    
    
    
if __name__=="__main__":
    main()