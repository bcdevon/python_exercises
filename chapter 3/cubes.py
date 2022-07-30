# cubes = []
# for value in range (1, 11):
#     cube = value ** 3
#     cubes.append(cube)

#     cubes.append(value ** 3)
# print(cubes)

#this is a comprehension
cubes = [value**3 for value in range(1,11)]
print(cubes)
