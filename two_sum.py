num_list = [1,12,3,4,5,6,7]

def twoSum(nums, target):
   for i in range(len(nums)):
        for j in range(i + 1, len(nums)):
            if nums[i] + nums[j] == target:
                print([i, j])
                break
    
            


twoSum(num_list, 13)


