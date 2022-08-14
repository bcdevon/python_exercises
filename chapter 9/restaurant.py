class Restaurant:

    def __init__(self, restaurant_name, cuisine_type):
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type

    def describe_restaurant(self):
        print(f"{self.restaurant_name} serves {self.cuisine_type} food.")

    def open_restaurant(self):
        print(f"{self.restaurant_name} is open.")


new_restaurant = Restaurant('evangelos', 'italian')
my_food = Restaurant('mcdonalds', 'american')
your_food = Restaurant('KFC', 'southern')
print(f"{new_restaurant.restaurant_name}")
print(f"{new_restaurant.cuisine_type}")
new_restaurant.describe_restaurant()
my_food.describe_restaurant()
your_food.describe_restaurant()
<<<<<<< HEAD
new_restaurant.open_restaurant()
=======
new_restaurant.open_restaurant()
>>>>>>> 83de09af7e6efa49d99697bbe552c4b4cddf0ef1
