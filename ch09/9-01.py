class Restaurant():
    def __init__(self, restaurant_name, cuisine_type):
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type
    
    def describle_restaurant(self):
        print("Name: " + self.restaurant_name + " Cuisine type: " + self.cuisine_type)
    
    def open_restaurant(self):
        print(self.cuisine_type)

restaurant = Restaurant("aaa", "bbb")
restaurant.describle_restaurant()
restaurant.open_restaurant()
