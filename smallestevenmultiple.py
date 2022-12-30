def smallestEvenMultiple(n): 
    if n%2 == 0:
        return n
    elif (n * 2)%2 == 0:
        n = n * 2
        return n
print(smallestEvenMultiple(4))
