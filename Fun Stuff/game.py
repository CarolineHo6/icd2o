import math

def calculate_factorial(num):
    return math.factorial(num)

def main():
    print("Welcome to the Factorial Game!")
    print("Player 1, you will provide a number, and Player 2, you will calculate the factorial of that number.")

    while True:
        try:
            # Player 1 input
            num = int(input("Player 1, enter a non-negative integer (or enter -1 to quit): "))
            
            # Check if the game should end
            if num == -1:
                print("Game over. Thanks for playing!")
                break

            # Player 2 calculates factorial
            result = calculate_factorial(num)
            print(f"The factorial of {num} is: {result}")

        except ValueError:
            print("Invalid input. Please enter a non-negative integer.")

if __name__ == "__main__":
    main()