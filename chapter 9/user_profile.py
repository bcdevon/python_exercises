class User:

    def __init__(self, first_name, last_name, age, user_name):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age
        self.user_name = user_name
        self.login_attempts = login_attempts = 0

    def describe_user(self):
        print(f"{self.first_name} {self.last_name} {self.age} {self.user_name}")

    def greet_user(self):
        print(f"Hello {self.first_name}.")
    
    def increment_login_attempts(self):
        self.login_attempts += 1

class Admin(User):

    def __init__(self, first_name, last_name, age, user_name, privileges):
        super().__init__(first_name, last_name, age, user_name)
        self.privileges = privileges
        
    
    def show_privileges(self):
        print(f"Hello {self.first_name} list of privileges: ")
        for privilege in privileges:
            print(privilege)

class Privileges():

    def __init__(self, privileges):
        self.privileges = privileges

    def show_privileges(self):
        print(f"Hello {self.first_name} list of privileges: ")
        for privilege in privileges:
            print(privilege)


privileges = ['can add post', 'can delete post', 'can ban user']
# new_user = User('brady', 'devon', 35, 'bdevon')
# old_man = User('kurt', 'devon', 65, 'kdevon')
# the_boss = Admin('Alyssa', 'devon', 28, 'adevon', privileges)
# new_user.greet_user()
# new_user.describe_user()
# old_man.describe_user()
# old_man.increment_login_attempts()
# old_man.increment_login_attempts()
# old_man.increment_login_attempts()
# old_man.increment_login_attempts()
# old_man.greet_user()
# print(f"you have made {old_man.login_attempts} login attempts")
# the_boss.show_privileges()


