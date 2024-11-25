import random
import sys
import time

choices = ["rock", "paper", "scissors"]

machine_choice = random.choice(choices)

def coolprint(text):
    for character in text:
        sys.stdout.write(character)
        sys.stdout.flush()
        time.sleep(0.025)
    print("")



def game():
    wanttoplay = True

    yourwins = 0
    botwins = 0
    ties = 0
    yourlosses = 0
    botlosses = 0

    coolprint("Welcome to Rock, Paper, Scissors")
    while wanttoplay:
        coolprint("What are you choosing?\nYou can choose between 'rock' 'paper' 'scissors'")
        player_choice = input("")

        if player_choice.lower() == machine_choice:
            coolprint("You and the bot chose the same! It's a tie!")
            ties += 1
        elif player_choice.lower() == "paper" and machine_choice == "rock":
            coolprint("Player won!")
            print(f"Bot choice: rock")
            yourwins += 1
            botlosses += 1
        elif player_choice.lower() == "scissors" and machine_choice == "paper":
            coolprint("Player won!")
            print(f"Bot choice: paper")
            yourwins += 1
            botlosses += 1
        elif player_choice.lower() == "rock" and machine_choice == "scissors":
            coolprint("Player won!")
            print("Bot choice: scissors")
            yourwins += 1
            botlosses += 1
        else:
            coolprint("Bot won!")
            print(f"Bot choice: {machine_choice}")
            botwins += 1
            yourlosses += 1
        want_input = input("Do you want to play again? (y/n)")
        if want_input.lower() == "y":
            wanttoplay = True
        elif want_input.lower() == "n":
            wanttoplay = False
            coolprint(f"Your stats:\nWins: {yourwins}\nLosses: {yourlosses}\n\nBot stats:\nWins: {botwins}\nLosses: {botlosses}\n\nTies: {ties}")


game()