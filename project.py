import time
import random
import sys


def print_like_typewriter(the_end):
    for character in the_end:
        sys.stdout.write(character)
        sys.stdout.flush()
        time.sleep(0.25)


def house_scene():
    while True:
        house = valid_input("Yes or No?", "yes", "no").lower()
        if house == "yes":
            print_sleep("The door opens", 2)
            print_sleep("Inside is a family that takes you in", 3)
            print("and cares for you")
            print_like_typewriter("You win!")
            break
        if house == "no":
            print_sleep("You dash through the entrance", 2)
            print_sleep("Back outside", 2)
            print_sleep("The wicked fairy kills you!", 2)
            print_like_typewriter("Game over\n")
            print_like_typewriter("You lose!\n")
            break


def game():
    while True:
        response = valid_input("What would you like to do?", "1", "2")
        if response == "1":
            print_sleep("You enter the abandoned house", 2)
            print_sleep("Where you find weapons, food, and supplies", 2)
            print_sleep("Suddenly you hear a sound", 2)
            print_sleep("Turns out the house isn't abandoned after all!", 2)
            print_sleep("You head towards where the sound came from", 2)
            print_sleep("You find a door", 2)
            print_sleep("Enter 'yes' to open the door", 2)
            print_sleep("Enter 'no' to leave the house", 2)
            house_scene()
            break
        elif response == "2":
            print_sleep("You get into the shed", 2)
            print_sleep("You find a shovel and a bottle of water", 2)
            print_sleep("You begin to hear strange sounds", 2)
            print_sleep("It's the fairy!", 2)
            print_like_typewriter("Game over\n")
            print_like_typewriter("You lose!\n")
            break


def print_sleep(string, sleep):
    print(string)
    time.sleep(sleep)


def intro():
    print_sleep("You find yourself standing in an open field,", 2)
    print("filled with grass and yellow wildflowers.")
    print_sleep("Rumor has it that a wicked fairy is somewhere", 3)
    print("around here, and has been terrifying the nearby village.")
    print_sleep("Run to shelter to avoid being caught by the wicked fairy!", 2)
    print_sleep("You stumble upon an abandoned house and a shed", 2)
    print_sleep("Enter 1 to enter abandoned house", 2)
    print_sleep("Enter 2 to enter shed", 2)


def valid_input(prompt, opt1, Opt2):
    while True:
        Answer = input(prompt).lower()
        if opt1 in Answer:
            return Answer
        elif Opt2 in Answer:
            return Answer
        else:
            print_sleep("Sorry, I don't understand.", 2)


def intro2():
    print_sleep("You are caught in a traffic jam", 2)
    print_sleep("News of zombies killing humans plays on the radio", 2)
    print_sleep("Your family is at the breakout area", 2)
    print_sleep("Go back and save them", 2)
    print_sleep("or let them die", 2)
    print_sleep("Enter 1 to go back and save your family", 2)
    print_sleep("Enter 2 to runaway", 2)


def game2():
    while True:
        path = valid_input("What will you do?", "1", "2")
        if path == "1":
            print_sleep("You get out of the car", 2)
            print_sleep("Run back to save your family", 2)
            print_like_typewriter("You're a loyal person")
            break
        elif path == "2":
            print_sleep("You run away leaving your family behind", 2)
            print_like_typewriter("You're not a loyal person")
            break


def choice1():
    intro()
    game()


def choice2():
    intro2()
    game2()


if random.randint(1, 2)== 1:
    print(choice1())
else:
    print(choice2())
