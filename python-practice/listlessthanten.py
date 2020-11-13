list = []
print("How many elements in the list?")
els = int(input())

i = 0;
print("Enter numbers to fill the list.")
while i < els:
    enter = int(input())
    list.append(enter)
    i += 1
    
new = []

print("Enter a number to compare to elements in the list.")
num = int(input())
    
for x in list:
    if x < num:
        new.append(x)
    
print(new)

