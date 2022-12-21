
# o(n*2)
# counter = 0
# for i in range(len(nums)):
#     for j in range(len(nums)):
#         print(nums[i], nums[j])
#         if nums[i] == nums[j] and i < j:
#             counter += 1
# print(counter)

nums = [1,2,5,1,1,5] 
 #o(n)#  
hashMap = {}
res = 0
for number in nums:            
    if number in hashMap:
        res += hashMap[number]
        hashMap[number] += 1
        print(res)
        print(hashMap[number])
    else:
        hashMap[number] = 1
        print(hashMap[number])
