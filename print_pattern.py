
# for i in range(1, 6):
#     for j in range(1, i + 1):
#         print(j, end=' ')
#     print('')
# print(1, end=' ')
# print(2)
# print('')
# print(' ',3)
sum = 0
user_num = input("Enter a number: ")
user_num = int(user_num)
for i in range(user_num + 1):
    print(i)
    sum += i
print(sum)

