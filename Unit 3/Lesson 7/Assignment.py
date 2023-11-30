choose = int(input("Choose your superhero, 1 = Iron Deficient Man, 2 = SpooderMan, 3 = Capsicle America: "))

import random
def choose_superhero():
    if choose == 1:
        return "Iron Deficient Man"
    elif choose == 2:
        return "SpooderMan"
    elif choose == 3:
        return "Capsicle America"
    else:
        return "Invalid Number chosen"

def game_intro(player_superhero):
        player_superhero = choose_superhero()
        intro = "Welcome " + player_superhero + ", the supervillain, Thianos, is trying to find all the Infinity Stones. Defeat Thianos in a battle to stop him from destroying this world."
        return intro

def make_decision():
    decision = int(input("Choose 1 to confront the villain, Choose 2 to seek assistance: "))
    if decision == 1:
         return "Confront Villain"
    elif decision == 2:
         return "Seek Assistance"
    else:
         return "Invalid Input"

def superhero_mission(action, player_superhero):
    if player_superhero == "Iron Deficient Man":
         if action == 1:
              return thianos_health - 10
         elif action == 2:
              return thianos_health - 50
         elif action == 3:
              return thianos_health - 75
         else:
              return thianos_health
    if player_superhero == "SpooderMan":
         if action == 1:
              return thianos_health - 10
         elif action == 2:
              return thianos_health - 60
         elif action == 3:
              return thianos_health - 85
         else:
              return thianos_health
    if player_superhero == "Capsicle America":
         if action == 1:
              return thianos_health - 30
         elif action == 2:
              return thianos_health - 50
         elif action == 3:
              return thianos_health - 80
         else:
              return thianos_health

def thianos_health():
     return int(100)

def manage_health(current_health, damage_taken):
    if superhero_mission:
        current_health = 100 - random.randint(100)
    damage_taken = 100 - current_health
    if current_health <= 0:
         return "Game ends, you have died"

def bonus_points():
     if superhero_mission == 1:
          return 

def game_completion():
     

print(game_intro())
print("Thanos is causing trouble. Do you want to confront the villain or seek assistance from another hero?")
print(make_decision())

