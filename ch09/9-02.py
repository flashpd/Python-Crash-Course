class Restaurant():
    def __init__(self, restaurant_name, cuisine_type):
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type
    
    def describle_restaurant(self):
        print(self.restaurant_name)
        print(self.cuisine_type)
    
    def open_restaurant(self):
        print(self.cuisine_type)

restaurant_0 = Restaurant("aaa", "bbb")
restaurant_1 = Restaurant("ccc", "ddd")
restaurant_2 = Restaurant("eee", "fff")

restaurant_0.describle_restaurant()
restaurant_0.open_restaurant()
restaurant_1.describle_restaurant()
restaurant_1.open_restaurant()
restaurant_2.describle_restaurant()
restaurant_2.open_restaurant()
