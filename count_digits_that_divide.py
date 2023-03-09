def countsDigits(num):
    result = 0
    for i in str(num):
        if num % int(i) == 0:
            result += 1
    print(result)

countsDigits(121)
"""loop through num
    result = 0
    for i in num
        if num%i == 0 
            result += 1
    return result
    I converted num to a string to iterate through it then back to an int"""
   
