'''Given an integer num, repeatedly add all its digits until the result has only one digit, 
and return it.
 '''
'''
edge cases
entered number already one digit
entered number negative
entered number more than two digits
'''
def addDigits(num):
    while num > 9:
        firstDigit = int(num/10)
        secondDigit = num%10
        if num < 10:
            print(num)
        else:
            num = firstDigit + secondDigit
            print(num)
        
addDigits(39)



    