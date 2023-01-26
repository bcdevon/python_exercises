def arithmeticTriplets(nums, diff):
    triplets = 0
    for i in(range(len(nums))):
        for j in(range(len(nums))):
            if nums[j]-nums[i] == diff:
                for k in(range(len(nums))):
                    if nums[k]-nums[j] == diff:
                        triplets += 1
    print(triplets)
nums = [0,1,4,6,7,10] 
diff = 3
arithmeticTriplets(nums, diff)