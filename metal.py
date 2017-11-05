
class Metal:
    '''A class for storing different types of metal'''
    metals = []

    def __init__(self, name, price):
        self.name = name
        self.price = price
        Metal.metals.append(self)

    @classmethod
    def get_num_metals(cls):
        return len(cls.metals)

    @classmethod
    def get_price(cls, name):
        # would be easier to search for an element if we used a map {name:price}
        # but doing it this way is more OOP
        for obj in cls.metals:
            if name == obj.name:
                return obj.price
        # if not found return None
        return None

    @classmethod
    def remove_all_metals(cls):
        cls.metals = []