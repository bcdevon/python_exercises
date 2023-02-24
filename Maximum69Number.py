def maximum69Number(num):
    result = ""
    found = False
    num = str(num)
    for i in num:
        if i == "6" and found == False:
            result += "9"
            found = True
        elif i == "9":
            result += "9"
        else:
            result += "6"
    result = int(result)
    print(result)

maximum69Number(6696)