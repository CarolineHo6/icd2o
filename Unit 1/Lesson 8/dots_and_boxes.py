y_name = input("Enter your name: ")

print(f"Game #1:")
o_name1 = input("Opponent's Name: ")
y_boxes1 = int(input("Your Points: "))
o_boxes1 = int(input("Opponent Points: "))

print(f"Game #2:")
o_name2 = input("Opponent's Name: ")
y_boxes2 = int(input("Your Points: "))
o_boxes2 = int(input("Opponent Points: "))

print(f"Game #3:")
o_name3 = input("Opponent's Name: ")
y_boxes3 = int(input("Your Points: "))
o_boxes3 = int(input("Opponent Points: "))

print(f"Game #4:")
o_name4 = input("Opponent's Name: ")
y_boxes4 = int(input("Your Points: "))
o_boxes4 = int(input("Opponent Points: "))

print(f"Game #5:")
o_name5 = input("Opponent's Name: ")
y_boxes5 = int(input("Your Points: "))
o_boxes5 = int(input("Opponent Points: "))

opponent = "Opponent"
your_points = "Your Points"
opponent_points = "Opponent Points"
box_percent = "Box %"
box_percent1 = float(y_boxes1/49*100)
box_percent2 = float(y_boxes2/49*100)
box_percent3 = float(y_boxes3/49*100)
box_percent4 = float(y_boxes4/49*100)
box_percent5 = float(y_boxes5/49*100)

print("  ")
print(f"Dots and Boxes Score Tracker")

print(f"Player's Name: {y_name}")

print(f"{opponent:<15}{your_points:<13}{opponent_points:<23}{box_percent}")
print(f"=========================================================")
print(f"{o_name1:<24}{y_boxes1:<17}{o_boxes1:<11}{box_percent1:.2f}")
print(f"{o_name2:<24}{y_boxes2:<17}{o_boxes2:<11}{box_percent2:.2f}")
print(f"{o_name3:<24}{y_boxes3:<17}{o_boxes3:<11}{box_percent3:.2f}")
print(f"{o_name4:<24}{y_boxes4:<17}{o_boxes4:<11}{box_percent4:.2f}")
print(f"{o_name5:<24}{y_boxes5:<17}{o_boxes5:<11}{box_percent5:.2f}")
print(f"=========================================================")
