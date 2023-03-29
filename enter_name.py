found_end = False
while found_end == False:
    name = input("What is your name: ")
    if name != "END":
        print(name)
    elif name == "END": 
        found_end = True
        print("I am done.")