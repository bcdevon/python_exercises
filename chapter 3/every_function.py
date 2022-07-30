cities =['albany', 'lebanon', 'portland', 'corvallis', 'wilsonville', 'independence']
print(len(cities))

cities.reverse()
print(cities)

print(sorted(cities))
print(cities)

cities.sort()
print(cities)

cities.insert(0, 'havana')
print(cities)

cities.remove("havana")
print(cities)

cities.pop(2)
print(cities)

del cities[0]
print(cities)

cities.append('aurora')
print(cities)

print(cities[-1])
