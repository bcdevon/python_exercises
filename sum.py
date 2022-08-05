num_list = [3, 4, 6, 9, 1, 3]


def find_sum(nums, target):
    for i in range(len(nums)):
        for j in range(i + 1, len(nums)):
            if nums[i] + nums[j] == target:
                return True

    return False


print(find_sum(num_list, 12))
