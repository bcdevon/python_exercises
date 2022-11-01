from user_module import User, Admin, Privileges

privileges = ['can add post', 'can delete post', 'can ban user']
my_user_account = Admin('brady', 'devon', 35, 'bdevon', privileges)
my_user_account.show_privileges()