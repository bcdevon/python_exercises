class Dog:
    """A simple attempt to model a dog."""

    def __init__(self, name, age):
        """Initialize name and age attributes."""

        self.name = name
        self.age = age

    def sit(self):
        """Simulate a dog sitting in response to a command."""
        print(f"{self.name} is now sitting.")

    def roll_over(self):
        """Simulate rolling over in response to a command."""
        print(f"{self.name} rolled over!")


my_dog = Dog('willie', 6)
your_dog = Dog('lucy', 3)

print(f"my dogs name is {my_dog.name}")
print(f"my dog is {my_dog.age} years old.")
my_dog.sit()

print(f"\nyour dogs name is {your_dog.name}")
print(f"your dog is {your_dog.age} years old")
your_dog.sit()
