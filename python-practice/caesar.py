cipher = ['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','W','X','Y','Z']

print("Welcome to the Caesar Cipher!")
print("Options: ENCRYPT     DECRYPT     QUIT")
option = input()

if option.lower() == "encrypt":
    print("Shift size (integer):")
    shift = int(input())
    print("Encrypt your message:")
    entry = str(input().upper())

    entry_modified = []

    i = 0
    while i < len(entry):
        entry_modified.append(entry[i])
        i += 1

    encrypted = [] 

    for x in range(len(entry_modified)):
        for y in range(len(cipher)):
            if entry_modified[x].upper() == cipher[y]:
                encrypted.append(cipher[y+shift])
     
    #type indices error resolved: https://stackoverflow.com/questions/35957085/python3-typeerror-list-indices-must-be-integers-or-slices-not-str 
    #fuckn dumbass lmao 

    final = ""
    j = 0
    while j < len(entry_modified):
        final += str(entry_modified[j])
        j += 1

    encryption = ""
    l = 0
    while l < len(encrypted):
        encryption += str(encrypted[l])
        l += 1
        
    print("Plaintext: " + final)
    print("Ciphertext: " + encryption)
elif option.lower() == "decrypt":
    print("Shift size (integer):")
    shift = int(input())
    print("Decrypt your message:")
    entry = str(input().upper())

    entry_modified = []

    i = 0
    while i < len(entry):
        entry_modified.append(entry[i])
        i += 1

    decrypted = [] 

    for x in range(len(entry_modified)):
        for y in range(len(cipher)):
            if entry_modified[x].upper() == cipher[y]:
                decrypted.append(cipher[y-shift])
     
    #type indices error resolved: https://stackoverflow.com/questions/35957085/python3-typeerror-list-indices-must-be-integers-or-slices-not-str 
    #fuckn dumbass lmao 

    final = ""
    j = 0
    while j < len(entry_modified):
        final += str(entry_modified[j])
        j += 1

    decryption = ""
    l = 0
    while l < len(decrypted):
        decryption += str(decrypted[l])
        l += 1
        
    print("Ciphertext: " + final)
    print("Plaintext: " + decryption)
elif option.lower() == "quit":
    print("Goodbye!")
else:
    print("Invalid input!")