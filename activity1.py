import random 
while True : 
    user_actions= input("CHOOSE ROCK , PAPER OR SCISSORS :-").upper()
    possible_actions=["ROCK","PAPER","SCISSORS"]
    computer_actions = random. choice(possible_actions)
    print("YOU CHOSE",user_actions,",COMPUTER CHOSE",computer_actions)
    if user_actions == computer_actions: 
        print("ITS A TIE") 
    elif user_actions == "ROCK":
        if computer_actions == "SCISSORS":
            print("ROCK SMASHES SCISSORS THEREFORE YOU WIN")
        else: 
            print("PAPER COVERS ROCK THEREFORE YOU LOSE") 
    elif user_actions == "PAPER":
        if computer_actions == "ROCK":
            print("PAPER COVERS ROCK THEREFORE YOU WIN") 
        else:
            print("SCISSORS CUT PAPER THEREFORE YOU LOSE")
    elif user_actions == "SCISSORS":
        if computer_actions == "PAPER":
            print("SCISSORS CUT PAPER THEREFORE YOU WIN")
        else:
            print("ROCK SMASHES SCISSORS THEREFORE YOU LOSE")
    play_again = input("DO YOU WANT TO PLAY AGAIN? YES/NO:-").upper()
    if play_again != "YES":
        break 