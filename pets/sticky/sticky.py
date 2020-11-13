#sticky

def option():
    opt = input(("read/write/new/close\n"))
    if opt.lower() == "read":
        read()
    elif opt.lower() == "write":
        write()
    elif opt.lower() == "close":
        close()
    elif opt.lower() == "new":
        new()
    else:
        print("wrong input\n")
        option()

def read():
    f = open("sticky.txt", "r")
    print("")
    print("#########################")
    print(f.read())
    print("#########################\n")
    f.close()
    option()
    
def write():
    f = open("sticky.txt", "a")
    add = str(input())
    f.writelines("\n")
    f.writelines(add)
    print("")
    f.close()
    option()
    
def new():
    f = open("sticky.txt", "w")
    add = input()
    f.write(add)
    print("")
    f.close()
    option()

def close():
    quit()
 

option()