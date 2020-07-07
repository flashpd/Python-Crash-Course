from restaurant import Restaurant
class IceCreamStand(Restaurant):
    def __init__(self, restaurant_name = '', cuisine_type = ''):
        super().__init__(restaurant_name, cuisine_type)
        self.flavors = []
    
    def increase_flavors(self, *flavor):
        self.flavors = flavor[:]

    def get_flavors(self):
        for i in self.flavors:
            print(i)

ice_creamstand = IceCreamStand()
# ice_creamstand.describle_restaurant('111', '222')

flavors = ['a', 'b', 'c']

ice_creamstand.increase_flavors(flavors)
# ice_creamstand.increase_flavors('a', 'b')
ice_creamstand.get_flavors()
        