command = "G()(al)"
# Output: "Gooooal"
string = ""
for i in range(len(command)):
    if command[i] == "G":
        string += "G"
    elif command[i] == "(" and command[i + 1]  == ")":
        string += "o"
    elif command[i] == "(" and command[i + 2] == "l":
        string += "al"
print(string)
        
