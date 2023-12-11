import time

def intro():
    print("Welcome to the Choose Your Own Adventure Game!")
    time.sleep(1)
    print("You find yourself standing in front of two mysterious doors.")
    time.sleep(1)
    print("Do you want to go through Door 1 or Door 2?")

def door_1():
    print("\nYou open Door 1 and find a room filled with treasure!")
    time.sleep(1)
    print("Congratulations! You're rich!")

def door_2():
    print("\nYou open Door 2 and a dragon appears!")
    time.sleep(1)
    print("Do you want to:")
    print("1. Try to fight the dragon")
    print("2. Close the door and run away")

    choice = input("Enter 1 or 2: ")

    if choice == "1":
        print("\nYou bravely attempt to fight the dragon...")
        time.sleep(1)
        print("But unfortunately, the dragon is too powerful.")
        time.sleep(1)
        print("Game over!")
    elif choice == "2":
        print("\nYou wisely close the door and run away.")
        time.sleep(1)
        print("You manage to escape safely.")

def play_game():
    intro()

    chosen_door = input("Enter 1 or 2: ")

    if chosen_door == "1":
        door_1()
    elif chosen_door == "2":
        door_2()
    else:
        print("Invalid choice. Game over.")

if __name__ == "__main__":
    play_game()