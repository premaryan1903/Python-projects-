# This program calculates the square of a number entered by the user.  The program continues to prompt for numbers until the user enters 0 to exit.
while "true":
  

    def num(n):
        if (n == 0):
            return
    
        print(n)
        num(n - 1)

    prem = int(input("Enter a number (0 = exit): "))

    num(prem)

    if prem == 0:
        print("Exiting the program.")
        break
    

