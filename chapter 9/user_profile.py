class User:

    def __init__(self, first_name, last_name, age, user_name):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age
        self.user_name = user_name

    def describe_user(self):
        print(f"{self.first_name} {self.last_name} {self.age} {self.user_name}")

    def greet_user(self):
        print(f"Hello {self.first_name}.")


new_user = User('brady', 'devon', 35, 'bdevon')
old_man = User('kurt', 'devon', 65, 'kdevon')
new_user.greet_user()
new_user.describe_user()
old_man.greet_user()
old_man.describe_user()
