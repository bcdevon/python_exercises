nums = [1,1]
max = 0
     
missing_numbers = []
for i in range(len(nums)):
    max += 1
not_disappeared = set(range(1,max + 1))
nums_set = set(nums)
for j in not_disappeared:
    if j not in nums_set:
        missing_numbers.append(j)
print(missing_numbers)