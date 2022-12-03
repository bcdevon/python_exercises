nums = [1, 2, 3, 2]

#     def containsNearbyDuplicate(self, nums, k):
#         """
#         :type nums: List[int]
#         :type k: int
#         :rtype: bool
#         """
#         last_seen_index = {}
#         for idx, x in enumerate(nums):
#             if x in last_seen_index and idx - last_seen_index[x] <= k:
#                 return True
#             last_seen_index[x] = idx
        
#         print(last_seen_index)

# containsNearbyDuplicate(nums, 4)


dict1 = {}
for i, v in enumerate(nums):
    if v in dict1 and i - dict[v] <= 3:
        print("True")
    dict[v] = i
print("False")