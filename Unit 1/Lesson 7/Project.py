#Variables
school = "Bayveiw Glen Independent School, Moatfield Campus"
print(f"Welcome to the School Resources Assessment Program!")
print(f"Location: {school}")
print(f"Data Collection: ")
print(f"1. Water Fountains: ")
water_fountain = input("  - Enter number of water fountains: ")
location_f = input("  - Enter location of water fountains (seperated with commas): ")
condition_f = input("  - Describe the condition of the water fountains: ")
print(f"2. Restrooms: ")
restroom = input("  - Enter number of restrooms: ")
location_r = input("  - Enter location of restrooms (seperated with commas): ")
condition_r = input("  - Describe the cleanliness of the restrooms: ")
print(f"3. Cafeteria: ")
cafeteria = input("  - Enter the seating capacity of the cafeteria: ")
cafeteria_a = input("  - Enter the average daily attendance in the cafeteria: ")
condition_c = input("  - Enter the condition of the cafeteria: ")
print(f"4. Classrooms: ")
classrooms = input("  - Enter the total number of classrooms: ")
num_water_f = float(water_fountain)/float(classrooms)
num_restroom = float(water_fountain)/float(classrooms)
fountain = "Water Fountains"
washroom = "Restrooms"
cafeteria_name = "Cafeteria"
classroom = "Classrooms",

#Output
print(f"   ")
print(f"   ")
print(f"   ")
print("Data Collection")
print("1. Water Fountains:")
print(f"  - Number of Water Fountains: {water_fountain}")
print(f"  - Locations: {location_f}")
print(f"  - Condition: {condition_f}")
print(" ")
print(f"2. Restrooms: ")
print(f"  - Number of Restrooms: {restroom}")
print(f"  - Locations: {location_r}")
print(f"  - Cleanliness: {condition_r}")
print(f" ")
print(f"3. Cafeteria: ")
print(f"  - Seating Capacity: {cafeteria}")
print(f"  - Average Daily Attendance: {cafeteria_a}")
print(f"  - Condition: {condition_c}")
print(" ")
print(f"4. Classrooms: ")
print(f"  - Total Number of {classrooms}: {classrooms}")
print(f"  - Number of Water Fountains per Classroom: {num_water_f}")
print(f"  - Number of Restrooms per Classroom: {num_restroom}")