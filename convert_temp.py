def convertTemperature(celsius): 
    kelvin = celsius + 273.15
    fahrenheit = (celsius * 1.8) + 32.00
    ans = [kelvin, fahrenheit]
    return ans

print(convertTemperature(0))