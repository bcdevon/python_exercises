                    
s = "yo|uar|e**|b|e***au|tifu|l"
pair_count = 0
count = 0
for i in s:
    if i == "|":
        pair_count += 1
    if pair_count%2 == 0 and i == "*":
        count += 1
print(count)

"""time complexity is O(n) n is the length of s"""

