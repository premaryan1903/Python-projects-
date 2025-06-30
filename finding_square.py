# This program calculates the square of a number entered by the user. The program continues to prompt for numbers until the user enters 0 to exit.
    
def square(number):
    result = number ** 2
    print(f"The square of {number} is {result}")

while True:
    try:
        user_input = int(input("Enter a number (0 = exit): "))
        if user_input == 0:
            print("Exiting the program.")
            break
        square(user_input)
    except ValueError:
        print("Please enter a valid integer.")

