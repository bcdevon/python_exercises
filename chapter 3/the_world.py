from audioop import reverse


locations = ['galapagos islands', 'switzerland', 'iceland', 'bahamas', 'new zealand']
print(locations)

locations.reverse()
print(locations)

print(sorted(locations))
print(locations)

print(sorted(locations, reverse=True))
print(locations)
locations.reverse()
print(locations)
locations.reverse()
print(locations)
locations.sort(reverse=True)
print(locations)