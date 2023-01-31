
def maxDepth(s):
    counter = 0
    max_counter = 0
    for i in(range(len(s))):
        if s[i] == "(":
            counter += 1
        if s[i] == ")":
            counter -= 1
        if counter > max_counter:
            max_counter = counter
    return max_counter


print(maxDepth("(1+(2*3)+((8)/4))+1"))