def addDigits(num):
    while num > 9:    
        first_Digit = int(num/10)
        second_Digit = num%10
        num = first_Digit + second_Digit
    print(num)
        
addDigits(38)