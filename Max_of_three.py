nums = [1,1,2]
nums.sort(reverse=True)
if len(nums) < 3:
    print(nums[0])
count = 1
max = nums[0]
for i in range(len(nums)):
    if nums[i] < max:
        max = nums[i]
        count += 1
    if count == 3:
        print(max)
if count != 3:
    print(nums[0])
     

    