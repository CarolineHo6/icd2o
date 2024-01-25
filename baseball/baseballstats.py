def read_baseball_data(file_path):
    names, hits, runs, rbis = [],[],[],[]
    try:
        with open(file_path, "r") as file:
            #Skip the header line
            next(file)
            for line in file:
                data = line.strip().split(",") #Strips the stuff (numbers) out of the line then split it by commas
                names.append(data[0])
                hits.append(int(data[1]))
                runs.append(int(data[2]))
                rbis.append(int(data[3]))
    except FileNotFoundError:
        print(f"Error: File {file_path} no found.")
    return names, hits, runs, rbis

def display_all_baseball_stats(names, hits, runs, rbis):
    for i in range(len(names)):
        print(f"|{names[i]:<25}|{hits[i]:>6}|{runs[i]:>6}|{rbis[i]:>6}|")

def calculate_and_display_average(hits, runs, rbis):
    print(f"Average Hits: {sum(hits)/len(hits)}")
    print(f"Average Runs: {sum(runs)/len(runs)}")
    print(f"Average rbis: {sum(rbis)/len(rbis)}")

if __name__ == "__main__":
    # Specify the file path
    file_path = "baseball_stats.txt"
    # Read baseball data from the file
    names, hits, runs, rbis = read_baseball_data(file_path)
    # Display menu and handle user choices
    while True:
        print("\nMenu:")
        print("1. Display all baseball player statistics")
        print("2. Calculate and display average baseball statistics")
        print("3. Identify player with the most hits")
        print("4. Identify player with the most RBIs")
        print("5. Display top 10 players in a category")
        print("6. Add a new baseball player")
        print("7. Exit")
        choice = input("Enter your choice (1-7): ")
        
        if choice == '1':
            display_all_baseball_stats(names, hits, runs, rbis)
        elif choice =="2":
            calculate_and_display_average(hits, runs, rbis)
        elif choice == "7":
            print("Exiting the program. Goodbye!")
            break
        else:
            print("Invalid choice. Please enter a number from 1 to 7.")
