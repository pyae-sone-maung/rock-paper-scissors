import random
from termcolor import colored

items = ["Rock", "Paper", "Scissor"]

def random_strategy():
    item_chosen = random.choice(items)
    return item_chosen

def onlyrock_strategy():
    item_chosen = "Rock"
    return item_chosen

def cycle_strategy(item_index):
    index = item_index % 3
    item_chosen = items[index]
    return item_chosen

def player_chosen_item(choice_item, index):
    if choice_item == "random":
        player_item = random_strategy()
    elif choice_item == "onlyrock":
        player_item = onlyrock_strategy()
    elif choice_item == "cycle":
        player_item = cycle_strategy(index)
    return player_item

def judgment(play_times):
    player_one_win =0
    player_two_win =0
    play = 0

    while play <play_times:
        player_one = player_chosen_item(player_one_choice, play)
        player_two = player_chosen_item(player_two_choice, play)

        if (player_one=="Scissor" and player_two=="Paper") or (player_one=="Rock" and player_two=="Scissor") or (player_one=="Paper" and player_two=="Rock"):
            print("{} vs {} \nPlayer1 win. \n".format(player_one, player_two))
            player_one_win = player_one_win +1
        elif (player_one=="Paper" and player_two=="Scissor") or (player_one=="Scissor" and player_two=="Rock") or (player_one=="Rock" and player_two=="Paper"):
            print("{} vs {} \nPlayer2 win. \n".format(player_one, player_two))
            player_two_win = player_two_win +1
        else:
            print("{} vs {} \nEven. \n".format(player_one, player_two))           
        play =  play + 1

    print(">>> End Janken <<< \nThe score is: {} - {}".format(player_one_win, player_two_win))
    
    if player_one_win > player_two_win:
        print("Player1 win the game.")
    elif player_one_win < player_two_win:
        print("Player2 win the game.")
    else:
        print("The game draw.")   


if __name__ == "__main__":
    strategy = ["random", "onlyrock", "cycle"]
    while True:
        print("\n***********************************************************************")
        print("\n\t\t* Welcome To Janken Game * \n")
        print("\t\t    [ Game Strategy ]")
        print("\tRandom \t\t= Scissors-rock-paper are random.")
        print("\tOnlyRock \t= You are only rock.")
        print("\tCycle \t\t= You are Rock-Scissors-Paper ordered. \n")

        try:
            play_times = int(input("Enter number of game play round : "))
            player_one_choice = input("Enter strategy for Player1 (random, onlyrock, cycle)   :").lower()
            if not player_one_choice in strategy:
                print(colored("Invalid input Player1 strategy.","red"))
                continue

            player_two_choice = input("Enter strategy for Player2 (random, onlyrock, cycle)   :" ).lower()
            if not player_two_choice in strategy:
                print(colored("Invalid input Player2 strategy.", "red"))
                continue

            print()
            judgment(play_times)
            play_again = input("\nDo you want to play again (Y/N) ? : ").lower()
            if play_again=="y":
                continue
            else:
                break
            
        except (ValueError):
            print(colored("Invalid input number of game play.","red"))
            continue