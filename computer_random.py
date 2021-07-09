import random
from termcolor import colored

items = ["Rock", "Paper", "Scissor"]
def judgment(playing):
    player_one_win =0
    player_two_win =0
    play = 0
    while play < playing:
        player_one = random.choice(items)
        player_two = random.choice(items)

        if (player_one=="Scissor" and player_two=="Paper") or (player_one=="Rock" and player_two=="Scissor") or (player_one=="Paper" and player_two=="Rock"):
            print("{} vs {}".format(player_one, player_two),"\nPlayer1 win! \n")
            player_one_win = player_one_win +1
            play = play + 1

        elif (player_one=="Paper" and player_two=="Scissor") or (player_one=="Scissor" and player_two=="Rock") or (player_one=="Rock" and player_two=="Paper"):
            print("{} vs {}".format(player_one, player_two),"\nPlayer2 win! \n")
            player_two_win = player_two_win +1
            play = play + 1

        else:
            print("{} vs {}".format(player_one, player_two),"\nEven \n")

    print(">>> End Janken <<<")
    print("The score is: {} - {}".format(player_one_win, player_two_win))
    
    if player_one_win > player_two_win:
        print("Player1 win the game.\n")

    elif player_one_win < player_two_win:
        print("Player2 win the game. \n")

    else:
        print("The game draw. \n")   

def choice_item():
    while True:
        try:
            print("\n*******************************************\n")
            print(">>>>> Welcome to Janken Game <<<<<")
            print("     * Rock, Paper, Scissor *")
            playtimes = int(input("\nEnter number of game play round : "))
            print()
            judgment(playtimes)
            
            play_again = input("Do you want to play again (Y/N) ? : ").lower()
            if play_again=="y":
                continue
            else:
                break
        except (ValueError):
            print(colored("Invalid input number of game play.", "red"))
            continue

if __name__ == "__main__":
    choice_item()