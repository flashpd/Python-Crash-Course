class Restaurant():
    def __init__(self, restaurant_name, cuisine_type):
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type
        self.number_served = 0
    
    def describle_restaurant(self): #   打印餐馆名称和美食类型
        print("Name: " + self.restaurant_name + " Cuisine type: " + self.cuisine_type)
    
    def open_restaurant(self):  #   单独打印美食类型
        print(self.cuisine_type)
    
    def updata_restaurant(self, num):   #   更新餐馆人数
        self.number_served = num
    
    def get_restaurant_number(self):   #   读取餐馆人数
        print("The number of this restaurant: " + str(self.number_served))

    def set_number_served(self, num):   #   设置餐馆人数并打印
        self.number_served = num
        print("The number of people you set is " + str(self.number_served))

    def increment_number_served(self, num): #   增加餐馆人数
        self.number_served += num
