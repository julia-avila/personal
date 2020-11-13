num = int(input("Enter a dividend: "))
check = int(input("Enter a divisor: "))
if num == 4:
    print("You have entered the integer 4.")
    if num % check == 0:
        print("Modulo is true.")
    else: 
        print("Modulo is false.")
elif num != 4:
    if num % check == 0:
        print("Modulo is true.")
    else:
        print("Modulo is false.")
else:
    print("Modulo is false.")

