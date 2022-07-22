current_users = ['Brady', 'alyssa', 'nellie', 'devon', 'harlow']
new_users = ['brady', 'nellie', 'macy', 'indy', 'piper']

current_users_lower = [current_user.lower() for current_user in current_users]
for new_user in new_users:
    if new_user.lower() in current_users_lower:
        print(f"Sorry {new_user}, that name is taken.")
    else:
        print(f"Great, {new_user} is still available.")
