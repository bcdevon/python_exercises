car = 'subaru'
car_0 = 'audi'
car_1 = 'bmw'
car_2 = 'BMW'
motorcycles = ['ducati', 'harley', 'suzukui']
numbers = [1, 6, 8, 13]

print("\nIs 5 <= 11 I predict True")
print(5 < 11)

print("\nIs 21 < 12 I predict False")
print(12 > 21)

print("\nIs 21 != to 13 I predict True")
print(21 != 13)

print("\nIs 21 != to 21 I predict False")
print(21 != 21)

print("\nIs 5 in numbers? I predict False")
print(5 in numbers)

print("\nIs 6 in numbers? I predict True")
print(6 in numbers)

print("\ncar_2.lower() == 'bmw'. I predict True.")
print(car_2.lower() == 'bmw')

print("\nIs 'ducati' in motorcycles? I predict True.")
print('ducati' in motorcycles)

print("\nIs 'Yamaha' in motorcycles? I predict False.")
print('Yamaha' in motorcycles)

print("\nIs car == 'subaru'? I predict True.")
print(car == 'subaru')

print("\nIs car != 'audi'? I predict True")
print(car != 'audi')

print("\nIs car == 'subaru' and car_0 == 'audi'? I predict True.")
print(car == 'subaru' and car_0 == 'audi')

print("\nIs car == 'ford' or car_0 == 'audi' I predict True.")
print(car == 'ford' or car_0 == 'audi')

print("\nIs car == 'ford' or car_0 == 'dodge' I predict False.")
print(car == 'ford' or car_0 == 'dodge')

print("\nIs car == subaru and car_0 == 'ford'? I predict False.")
print(car == 'subaru' and car_0 == 'ford')

print("\nIs car == 'audi'? I predict False.")
print(car == 'audi')

print("\nIs car != 'subaru'? I predict False")
print(car != 'subaru')
