my_set = set() 
set_a = {4,2,3,1,5,6,9,8,7}
list = [1,4,3,2,5,6,7,8,9]
for num in list:
    my_set.add(num)
print(my_set)
if my_set == set_a:
    print("True")
else:
    print("False")

# set_b.add(10)
# if list == set:
#     print("true")
# else:
#     print("false")
