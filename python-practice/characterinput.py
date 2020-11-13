name = input("Please type your name.\n")
age = int(input("And your age, please.\n"))
hundred = (100 - age) + 2019
times = int(input("How many times would you like the message to print?\n"))
i = 0

while i < times:
    print("Hello " + name + ". You will turn one hundred years old in the year " + str(hundred) + ".")
    i += 1

