# Created by Sam Kim
# Assisted by Dominic Sangster

import random
import time

# define variables
cpu_roll = 0
player_roll = 0

# you and the cpu roll 2 dice (it's really one die but don't tell Mr. Cozort)
def roll():
    global cpu_roll
    global player_roll
    cpu_roll += random.randint(2,12)
    print("CPU rolled " + str(cpu_roll))
    time.sleep(2)
    player_roll += random.randint(2,12)
    print("You rolled " + str(player_roll))

# comparing the dice rolls of the cpu and Mr. Cozort
def scoring():
    global cpu_roll
    global player_roll
    cpu_roll = 0
    player_roll = 0
    roll()
    # if Mr. Cozort scores higher, he wins (rare scenario)
    if player_roll > cpu_roll:
        print("Alright Mr. C, I guess you got lucky.")
    # WHEN the cpu scores higher, Mr. Cozort loses
    elif player_roll < cpu_roll:
        print("Oh no, you lost.")
    # if for some reason there is a tie, run tiebreaker code
    else:
        print("Dang, slap on a suit becuase that's a tie.")
        tiebreaker()

# if Mr. Cozort ties the computer, roll and compare again
def tiebreaker():
    global cpu_roll
    global player_roll
    tie = True
    if tie == True:
        scoring()

# ask if Mr. Cozort wants to get schooled
def play():
    playing = False
    yes = ["yes", "Yes"]
    no = ["no", "No"]
    while playing == False:
        playing = input("Yo Mr. Cozort, you wanna roll? [Yes/No]")
        if playing in yes:
            print("Aight fosho.")
            time.sleep(1)
            scoring()
            playing = True
        elif playing in no:
            print("Incorrect answer, you must play. Choose again.")
            playing = False 
        else:
            print("I didn't understand that. I'll take it as a yes.")
            time.sleep(2)
            scoring()
            playing = True

# run game
play()  