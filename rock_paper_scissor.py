import random
import pyfiglet
art=(pyfiglet.figlet_format("Rock_Paper_Scissor",width=100))
print(art)
choices=['r','p','s']
rounds=0
player_score=0
computer_score=0
player2_score=0
print("Welcome to Rock-Paper-Scissor Game")
total_round=int(input("Choose total rounds: 1 or 3 or 5 "))
choice=input("Whom you want to play with: Choose 'c' for Computer' or 'p' for 'player' ").lower()
#Choose Rounds
def game_round(total_round):
    global rounds
    if total_round==1:
            rounds=1
    elif total_round==3:
            rounds=3
    elif total_round==5:
            rounds=5
    else:
            return "Invalid Input"
#Choice
def valid_choice():
    while True:
        player=input("Choose 'r' for Rock 'p' for Paper and 's' for Scissor : ")
        if player  in choices:
            return player
        else:
            print("Enter Valid Choice")
#player Vs player
def winner_user(player,player2):
    global player2_score,player_score
    if player==player2:
        return f"It's a Tie.\nplayer1 chose {player} \nplayer2 chose {player2}."
    elif ((player=='r' and player2=='s') or (player=='p' and player2=='r') or (player=='s' and player2=='p')):
        player_score+=1
        return f"player1 chose {player} \nplayer2 chose {player2}.\nPlayer1 won the round"
    else:
        player2_score+=1
        return f"Player chose {player} \nplayer2 chose {player2}.\nplayer2 won the round"
#Player Vs Computer 
def winner_computer(player,computer):
    global player_score,computer_score
    if player==computer:
        return f"It's a Tie.\nplayer chose {player} \n computer chose {computer}."
    elif ((player=='r' and computer=='s') or (player=='p' and computer=='r') or (player=='s' and computer=='p')):
        player_score+=1
        return f"Player chose {player} \ncomputer chose {computer}.\nYou won the round"
    else:
        computer_score+=1
        return f"Player chose {player} \ncomputer chose {computer}.\ncomputer won the round"
game_round(total_round)
for round in range(rounds):
    print(f"Round {round+1} of {rounds}")
    if choice in ['player', 'p']:
        player=valid_choice()
        player2=valid_choice()
        print(winner_user(player,player2))
    elif choice in ['computer', 'c']:
        player=valid_choice()
        computer=random.choice(choices)
        print(winner_computer(player,computer))
    else:
        print("Invalid choice")
        exit()
print("\nFinal Scores")
#Display Final Score
if choice in ['player', 'p']:
    print(f"player1's Score = {player_score} and player2's Score = {player2_score}")
else:
    print(f"Your Score = {player_score} and Computer's Score = {computer_score}")
# Check Who Win the Challenge
if player_score > player2_score and choice in ['player', 'p']:
    print("Congratulations! player1 Has Won the Game.")
elif player2_score > player_score and choice in ['player', 'p']:
    print("Congratulations! player2 Has Won the Game.")
elif player_score > computer_score and choice in ['computer', 'c']:
    print("Congratulations! You Won the Game.")
elif computer_score > player_score and choice in ['computer', 'c']:
    print("Computer Won the Game.")
else:
    print("It's a Tie!")