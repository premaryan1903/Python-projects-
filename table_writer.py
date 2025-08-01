a = "true"
print("if you want to exit the program, enter 0.") 
while "true":
    num = int(input("enter number of which you want table: "))

    i = 1

    while i <= 10:
        print(num*i)
        i += 1

    if num == 0:
        print("Exiting the program.")
        break

  
