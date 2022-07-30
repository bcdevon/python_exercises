guest_list = ['alyssa devon', 'grandpa devon', 'kurt devon']
message = (f"Hello {guest_list[0]} you are invited to dinner")
message1 = (f"Hello {guest_list[1]} you are invited to dinner")
message2 = (f"Hello {guest_list[2]} you are invited to dinner")
print(f"{message}\n{message1}\n{message2}")

not_coming = 'grandpa devon'
print(f"{not_coming} will not be able to attend the dinner.")

new_guest = 'grandma devon'
guest_list[1] = new_guest
message = (f"Hello {guest_list[0]} you are invited to dinner")
message1 = (f"Hello {guest_list[1]} you are invited to dinner")
message2 = (f"Hello {guest_list[2]} you are invited to dinner")
print(f"{message}\n{message1}\n{message2}")

print(f"Hello {guest_list} we found a bigger table and are inviting more people.")
guest_list.insert(0, 'zach')
guest_list.insert(2, 'kelly')
guest_list.append('kurtis')
print(guest_list)

message = (f"Hello {guest_list[0]} you are invited to dinner")
message1 = (f"Hello {guest_list[1]} you are invited to dinner")
message2 = (f"Hello {guest_list[2]} you are invited to dinner")
message3 = (f"Hello {guest_list[3]} you are invited to dinner")
message4 = (f"Hello {guest_list[4]} you are invited to dinner")
message5 = (f"Hello {guest_list[5]} you are invited to dinner")
print(f"{message}\n{message1}\n{message2}\n{message3}\n{message4}\n{message5}")

print("The table wont be here in time I only have room for 2 people!")
no_room = guest_list.pop(5)
print(f"Sorry {no_room} not enough room for you.")
no_room = guest_list.pop(4)
print(f"Sorry {no_room} not enough room for you.")
no_room = guest_list.pop(0)
print(f"Sorry {no_room} not enough room for you.")
no_room = guest_list.pop(0)
print(f"Sorry {no_room} not enough room for you.")

print(f"Hello {guest_list[0]} and {guest_list[1]} you are invited to dinner")

del guest_list[0]
del guest_list[0]


print(guest_list)

