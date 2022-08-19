# target_num = input("enter number ")
# num_list = [3, 4, 6, 9, 1, 3]


# def find_sum(nums, target):
#     for i in range(len(nums)):
#         for j in range(i + 1, len(nums)):
#             if nums[i] + nums[j] == target:
#                 return True

#     return False



# print(find_sum(num_list, 12))
numbers=[1,2,3,4,9,8,5,10,20,30,6]
def two_no_summer(n,L):
     for i in range(0,len(L)):
         for j in range(i,len(L)):
             if (L[i]+L[j]==n) & (L[i]!=L[j]):
                  print(L[i],L[j])
two_no_summer(11, numbers)