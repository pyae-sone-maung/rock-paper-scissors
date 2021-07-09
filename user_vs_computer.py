import random
from termcolor import colored

items = ["Rock", "Paper", "Scissor"]
def judgment(playing):
    player_point =0
    computer_point =0
    play =0
    while play < playing:
        computer = random.choice(items)
        player_choice = choose_option()

        if player_choice:
            if (computer=="Scissor" and player_choice=="Paper") or (computer=="Rock" and player_choice=="Scissor") or (computer=="Paper" and player_choice=="Rock"):
                print("{} vs {} \nComputer win!".format(player_choice, computer))
                play = play+1
                computer_point = computer_point +1
            elif (computer=="Paper" and player_choice=="Scissor") or (computer=="Scissor" and player_choice=="Rock") or (computer=="Rock" and player_choice=="Paper"):
                print("{} vs {} \nYou win!".format(player_choice, computer))
                play = play+1
                player_point = player_point +1
            else:
                print("{} vs {} \nEven".format(player_choice, computer))
                play = play+1
        else:
            print(colored("Invalid your choice. Try again.", "red"))

    print("\n>>> End Jaken <<< \nThe score is: {} - {}".format(player_point, computer_point))
    is_winner(player_point, computer_point)

def choose_option():
    userinput = input("\nEnter your choice (R, P, S): ").lower()
    if userinput=="r":
        player_choice = "Rock"
    elif userinput=="p":
        player_choice = "Paper"
    elif  userinput=="s":
        player_choice = "Scissor"
    else:
        player_choice = None
    return player_choice

def is_winner(player, computer):
    if player > computer:
        print("You win the game.")
    elif  player == computer:
        print("Game Draw")
    else:
        print("Computer win the game.")

def welcome_janken():
    while True:
        try:
            print("\n*********************************************\n")
            print("   >>>>> Welcome to Janken Game <<<<<")
            print("\t* Rock, Paper, Scissor *\n")
            playtimes = int(input("Enter number of game play round: "))
            judgment(playtimes)

            play_again = input("\nDo you want to play again (Y/N) ? : ").lower()
            if play_again=="y":
                continue
            else:
                break

        except(ValueError):
            print(colored("Invalid input number of game play.", "red"))
            continue

if __name__ == "__main__":
    welcome_janken()
