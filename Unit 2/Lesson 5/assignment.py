Bug_type = "Bug Type"
Count = "Count"
Percentage = "Percentage"
Total = "Total"
def input_bug_counts():
    bug_name = input("Enter the type of bug: ")
    bug_count = int(input(f"Enter the count of {bug_name} bugs: "))
    bug_name2 = input("Enter the type of bug: ")
    bug_count2 = int(input(f"Enter the count of {bug_name2} bugs: "))
    bug_name3 = input("Enter the type of bug: ")
    bug_count3 = int(input(f"Enter the count of {bug_name3} bugs: "))
    return bug_name, bug_count, bug_name2, bug_count2, bug_name3, bug_count3

bug_name, bug_count, bug_name2, bug_count2, bug_name3, bug_count3 = input_bug_counts()
total_bugs = bug_count+bug_count2+bug_count3

def calculate_percent():
    total = bug_count+bug_count2+bug_count3
    percent = (bug_count/total)*100
    percent2 = (bug_count2/total)*100
    percent3 = (bug_count3/total)*100
    percent_total = (total_bugs/total)*100
    return percent, percent2, percent3, percent_total

percent, percent2, percent3, percent_total = calculate_percent()

def display_table():
    print(f"{Bug_type:<20}{Count:<10}{Percentage}")
    print("="*40)
    print(f"{bug_name}{bug_count:>17}{percent:>15.2f}")
    print(f"{bug_name2}{bug_count2:>22}{percent2:>15.2f}")
    print(f"{bug_name3}{bug_count3:>15}{percent3:>15.2f}")
    print("="*40)
    print(f"{Total:<23}{total_bugs:<11}%{percent_total}")

print("   ")
print(display_table())