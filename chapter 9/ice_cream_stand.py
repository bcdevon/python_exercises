class Restaurant:

    def __init__(self, restaurant_name, cuisine_type):
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type

    def describe_restaurant(self):
        print(f"{self.restaurant_name} serves {self.cuisine_type} food.")

    def open_restaurant(self):
        print(f"{self.restaurant_name} is open.")

class Ice_cream_stand(Restaurant):

    def __init__(self, restaurant_name, cuisine_type, flavors):
        super().__init__(restaurant_name, cuisine_type)
        self.flavors = flavors

    def different_flavors(self):
        for flavor in flavors:
            print(f'{flavor.title()} ice cream')

flavors = ['strawberry', 'chocolate', 'vanilla']
my_icecream = Ice_cream_stand('baskin robbins', 'dessert', flavors)
my_icecream.describe_restaurant()
my_icecream.different_flavors()