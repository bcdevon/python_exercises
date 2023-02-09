
def difference_of_sum(nums):
    element_sum = 0
    digit_sum = 0
    for num in nums:
        element_sum += num
        while num > 0:
            digit = num % 10
            digit_sum += digit
            num //= 10
    print(element_sum, digit_sum)
    print(abs(element_sum - digit_sum))

difference_of_sum([1,4,11,5,3,30])