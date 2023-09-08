class Burger:
    _size = None
    _cheese = False
    _tomato = False
    _lettuce = False,
    _pepperoni = False

    def __init__(self, builder):
        self._size = builder.size
        self._cheese = builder.cheese
        self._tomato = builder.tomato
        self._letttuce = builder.lettuce
        self._pepperoni = builder.pepperoni

class BurgerBuilder:
    size = None
    cheese = False
    tomato = False
    lettuce = False,
    pepperoni = False 
    
    def __init__(self, size):
        self._size = size

    def add_cheese(self):
        self.cheese = True
        return self
    
    def add_tomato(self):   
        self.tomato = True
        return self
    
    def add_lettuce(self):
        self.lettuce = True
        return self
    
    def add_pepperoni(self):
        self.pepperoni = True
        return self
    
    def build(self):
        return Burger(self)
    

if __name__ == "__main__":

    burger = BurgerBuilder(10).add_cheese().add_lettuce().add_tomato().add_cheese().build()
    print(vars(burger))