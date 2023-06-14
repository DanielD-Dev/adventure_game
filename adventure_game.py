import time
import random

# Function to print a message and pause for a short duration
def print_pause(input):
    print(input)
    time.sleep(0.5)

items = []
characters = ["pirate", "dude", "spider"]
character = random.choice(characters)

# Function for the player's encounter with a house
def house(character):
    print_pause("You approach the door of the house.")
    print_pause("You are about to knock when the door opens and out steps a {character}.")
    print_pause(f"Eep! This is the {character}'s house!")
    print_pause(f"The {character} attacks you!")
    if "sword" not in items:
        print_pause("You feel under-prepared with only a tiny dagger.")
    else:
        print_pause("You have a sword and are ready to fight!")
    print_pause("Choose (1) to fight or (2) to run away.")

    while True:
        input_after_the_house = input()
        if input_after_the_house == "1":
            fight(character)
        elif input_after_the_house == "2":
            field()
        else:
            print_pause("Wrong input. Please select 1 or 2\n")

# Function for the player's exploration of a cave
def cave():
    print_pause("You peer cautiously into the cave.")
    print_pause("It turns out to be only a very small cave.")
    print_pause("Your eye catches a glint of metal behind a rock.")
    print_pause("You have found the magical Sword of Ogoroth!")
    print_pause("You discard your dagger and take the sword.")
    print_pause("You walk back out to the field.")
    items.append("sword")
    make_initial_choice(character)

# Function for the player winning the fight
def win():
    print_pause("As the pirate moves to attack, you unsheath your new sword.")
    print_pause("The Sword of Ogoroth shines brightly as you brace yourself.")
    print_pause("But the pirate takes one look at your shiny new toy and runs away!")
    print_pause("You have rid the town of the pirate. You are victorious!")
    play_again()

# Function for the player losing the fight
def lose(character):
    print_pause("You do your best...")
    print_pause(f"But your dagger is no match for the {character}.")
    print_pause("You have been defeated!")
    play_again()

# Function for the player choosing to fight
def fight(character):
    if "sword" in items:
        win()
    else:
        lose(character)

# Function for the player returning to the field
def field():
    print_pause("You run back into the field. Luckily, you weren't followed.")
    print_pause("Enter 1 to knock on the door of the house.")
    print_pause("Enter 2 to peer into the cave.")
    print_pause("What would you like to do?")
    print_pause("(Please enter 1 or 2.)")
    input_after_field = input("(Please enter 1 or 2.)").lower()
    if input_after_field == "1":
        house(random.choice(["pirate", "dude", "spider"]))
    elif input_after_field == "2":
        cave()
    else:
        print_pause("Sorry, I don't understand. Please choose 1 or 2.")
        input_after_field = input("(Please enter 1 or 2.)\n").lower()

# Function for the player's decision to play again or quit
def play_again():
    choice = input("Would you like to play again? (y/n)").lower()
    if choice == "y":
        game()
    elif choice == "n":
        print_pause("BYE")
    else:
        print_pause("I don't understand. Please write Y or N?")
        play_again()

# Function for the game introduction and initial choice
def intro(character):
    print_pause("You find yourself standing in an open field, filled with grass and yellow wildflowers.")
    print_pause(f"Rumor has it that a {character} is somewhere around here and has been terrifying the nearby village.")
    print_pause("In front of you is a house.")
    print_pause("To your right is a dark cave.")
    print_pause("In your hand, you hold your trusty (but not very effective) dagger.")

# Function for the initial choice in the game
def make_initial_choice(character):
    print_pause("Enter 1 to knock on the door of the house.")
    print_pause("Enter 2 to peer into the cave.")
    print_pause("What would you like to do?")
    print_pause("(Please enter 1 or 2).")
    initial_input = input()
    if initial_input == "1":
        house(character)
    elif initial_input == "2":
        cave()
    else:
        print_pause("Invalid input. Please enter 1 or 2.")
        make_initial_choice(character)

# Function to start the game
def game():
    characters = ["pirate", "dude", "spider"]
    character = random.choice(characters)
    intro(character)
    make_initial_choice(character)

# Start the game
game()
