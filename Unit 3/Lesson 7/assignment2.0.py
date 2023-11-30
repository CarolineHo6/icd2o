import random
# This is the superhero selection function
# Choose superhero 1, 2, or 3
# This is the function where they choose their superhero and get random health
def character_choice():
    print("Welcome to the Python Marvel Superhero Adventure!")
    print("Choose your superhero!")
    print("The superhero choices are:")
    print("1 - Iron Deficient Man")
    print("2 - SpooderMan")
    print("3 - Capsicule America")
    character_choice = input("Choose the number for the superhero of your choice (1-3): ")

    # Character Validation
    while character_choice not in ['1', '2', '3']:
        print("Invalid Input. Choose the number beside the character:")
        print("1. Iron Deficient Man")
        print("2. SpooderMan")
        print("3. Capsicule America")
        character_choice = input("Choose the number for the superhero of your choice (1-3): ")

    # Character name and health
    if character_choice == 1:
        print("Iron Deficient Man")
    elif character_choice == 2:
        print("SpooderMan")
    else:
        print("Capsicule America")
    
    # Set initial health between 50 and 200
    initial_health = random.randint(50, 200)

    return character_choice, initial_health

# This is the game introduction function
def game_intro(character, initial_health):
    print(f"You are the superhero of Canada, {character}! The supervillain Thanoose is coming to attack Canada the citizens of Canada have called for your help to defeat him! Your initial health is {initial_health}")
    print(f"You must save the citizens of this Country!")

# This is the Decision
# Attack or Seek help
def make_decision():
    print("The supervillain, Thanose, is causing trouble.")
    print("Do you want to...")
    print("1. Confront the villain")
    print("2. Seek assistance from another hero")
    decision = input("Enter the number beside the decision you would like to make (1-2): ")

    return decision

# What happens after the choice
def choice(decision):
    if decision == '1':
        print("You have decided to attack Thanoose! Your bravery is awarded when you trip and fall and find 5 points on the ground!")
        return 5 #Bonus points
    elif decision == '2':
        print("You have decided to ask for help. You find a shiny coin on the ground and it is worth 10 points!")
        return 10 #Bonus points
    else:
        print("Invalid choice. A penalty will be given")
        return -20 #Penalty

# Function for Superhero Mission
def superhero_mission(action, player_superhero):
    player_superhero = character_choice()
    if make_decision() == 1:
        print("Since you are confronting Thanoose, choose your attack")
        print("1 - Scold")
        print("2 - Yell")
        print("3 - Hit with slipper")
        action = input("Enter the number beside the action you would like to do (1-3): ")
        if action == 1:
            return "You have scolded Thanoose. Thanoose's health is now " + t_current_health - random.randint(1, 30)
        elif action == 2:
            return "You have yelled at Thanoose. Thanoose's health is now " + t_current_health - random.randint(20, 100)
        elif action == 3:
            return "You have hit Thanoose with a slipper. Thanoose's health is now " + t_current_health - random.randint(1, 250)
        else:
            return "You missed"
    return action, player_superhero

# Thanoose's health
def thanoose_health(t_current_health):
    t_current_health = random.randint(100, 250)
    return t_current_health

# The player's health
def manage_health(current_health, damage_taken, initial_health):
    initial_health = random.randint(100, 200)
    damage_taken = random.randint(10, 201)
    current_health = initial_health - damage_taken
    return current_health, damage_taken, initial_health

# Game completion function
def game_completed():
    return "Thanks for playing the Simple Python Adventure Game!"

# Main function, excecutes everything
def main():
    # Character choice separated
    character, initial_health = character_choice()

    # Calls game intro
    game_intro(character, initial_health)

    # Calls the decision
    decision = make_decision()

    # Making the decision
    choice(decision)

    # Superhero mission
    superhero_mission(action, player_superhero)

    # Thanoose's health
    t_current_health = thanoose_health(t_current_health)

    # Player's health
    manage_health(current_health, initial_health)

    t_current_health = thanoose_health()
    action, player_superhero = superhero_mission()
    current_health, damage_taken = manage_health()
    character, initial_health = game_intro()

    # Game completion
    game_completed()
    
# Running the game
main()

