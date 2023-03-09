def minBitFlips(start, goal):
    #convert numbers to binary
    binary_start = bin(start)
    binary_goal = bin(goal)
    print(binary_start)
    print(binary_goal)
    i = len(binary_start)-1
    j = len(binary_goal)-1
    count = 0
    while binary_start[i] != "b" or binary_goal[i] != "b":
        if binary_start[i] != binary_goal[j]:
            count += 1
        i -= 1
        j -= 1
    print(count)

minBitFlips(3,4)
  binary_start = bin(start)
        binary_start = binary_start[2:]
        print(binary_start)
        binary_goal = bin(goal)
        binary_goal = binary_goal[2:]
        print(binary_goal)
        count = 0
        i = len(binary_start) -1
        j = len(binary_goal) -1
        print(i,j)
        count += abs(i-j)
        print(count)
        while i > 0 or j > 0:
            print(i,j)
            if binary_start[i] != binary_goal[j]:
                count += 1
            i -= 1
            j -= 1
        return count