# Write your code here
import random

beat_dict = {"rock": ["lightning", "gun", "air", "water", "dragon", "paper", "devil"],
             "gun": ["lightning", "sponge", "air", "water", "dragon", "paper", "devil"],
             "lightning": ["wolf", "sponge", "air", "water", "dragon", "paper", "devil"],
             "devil": ["wolf", "sponge", "air", "water", "dragon", "paper", "tree"],
             "dragon": ["wolf", "sponge", "air", "water", "human", "paper", "tree"],
             "water": ["wolf", "sponge", "air", "snake", "human", "paper", "tree"],
             "air": ["wolf", "sponge", "scissors", "snake", "human", "paper", "tree"],
             "paper": ["wolf", "sponge", "scissors", "snake", "human", "fire", "tree"],
             "sponge": ["wolf", "rock", "scissors", "snake", "human", "fire", "tree"],
             "wolf": ["gun", "rock", "scissors", "snake", "human", "fire", "tree"],
             "tree": ["gun", "rock", "scissors", "snake", "human", "fire", "lightning"],
             "human": ["gun", "rock", "scissors", "snake", "devil", "fire", "lightning"],
             "snake": ["gun", "rock", "scissors", "dragon", "devil", "fire", "lightning"],
             "scissors": ["gun", "rock", "water", "dragon", "devil", "fire", "lightning"],
             "fire": ["lightning", "gun", "air", "water", "dragon", "rock", "devil"]}


def decide_winner(user_choice, computer_choice, beat_dict):

    if user_choice in beat_dict[computer_choice]:
        print(f"Well done. The computer chose {computer_choice} and failed")
        return 1
    elif computer_choice in beat_dict[user_choice]:
        print(f"Sorry, but the computer chose {computer_choice}")
    else:
        print(f"There is a draw ({user_choice})")
        return 0


def play_game():

    score = 0
    user_name = input("Enter your name: ")
    print(f"Hello, {user_name}")

    with open("rating.txt", "r") as file:
        a = file.readlines()
    file.close()

    a = [x.rstrip() for x in a]

    for line in a:
        if user_name in line:
            score = int(line[len(user_name) + 1:])
            break

    mode = input().split(",")
    if len(mode) == 1:
        mode = ["rock", "paper", "scissors"]

    print("Okay, let's start")
    while True:

        user_input = input()

        if user_input == "!exit":
            print("Bye!")
            break
        elif user_input == "!rating":
            print(f"Your rating: {score}")
            continue
        elif user_input not in beat_dict:
            print("Invalid input")
            continue

        computer_option = random.choice(mode)
        score_ = decide_winner(user_input, computer_option, beat_dict)

        if score_ == 0:
            score += 50
        elif score_ == 1:
            score += 100


if __name__ == "__main__":
    play_game()




