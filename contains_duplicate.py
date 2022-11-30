'''Given an integer array nums and an integer k, 
return true if there are two distinct indices i and j 
in the array such that nums[i] == nums[j] and abs(i - j) <= k.

Example 1:

Input: nums = [1,2,3,1], k = 3
Output: true
Example 2:

Input: nums = [1,0,1,1], k = 1
Output: true
Example 3:

Input: nums = [1,2,3,1,2,3], k = 2
Output: false'''

'''
no matching numbers
no mathing numbers within k
empty array
more than one match
matching numbers within k
matching numbers but not within k
'''
nums = [1, 2, 3, 2]

def containsNearbyDuplicate(nums, k):
    duplicate = set()
    nums_set = set(nums)
    for i in range (len(nums)):
        if nums[i] in duplicate and abs() :
            duplicate.add(nums[i])
        if abs(num_set[0] - nums_set[1]) <=k:
            print("True")
    # for i in range (len(nums)):
    #     for j in range (i+1, len(nums)):
    #         if nums[i] == nums[j] and abs(i - j) <= k:
    #             return True

containsNearbyDuplicate(nums, 2)
    


    
