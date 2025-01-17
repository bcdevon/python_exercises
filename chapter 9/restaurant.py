class Restaurant:
    
    def __init__(self, restaurant_name, cuisine_type):
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type
        self.number_served = number_served = 0

    def describe_restaurant(self):
        print(f"{self.restaurant_name} serves {self.cuisine_type} food.")

    def open_restaurant(self):
        print(f"{self.restaurant_name} is open.")
    
    def increment_number_served(self):
        self.number_served += 100
        
    def set_number_served(self):
       self.number_served = input('how many people were served: ')


restaurant = Restaurant('mcdonalds', 'fast food')
new_restaurant = Restaurant('evangelos', 'italian')
my_food = Restaurant('mcdonalds', 'american')
your_food = Restaurant('KFC', 'southern')
print(f"{new_restaurant.restaurant_name}")
print(f"{new_restaurant.cuisine_type}")
restaurant.increment_number_served()
restaurant.increment_number_served()
restaurant.increment_number_served()
restaurant.increment_number_served()
print(f"{restaurant.restaurant_name} {restaurant.number_served}")