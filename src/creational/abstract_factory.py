class Window:
    def get_height(self):
        pass
    def get_width(self):
        pass

class WoodenWindow(Window):
    width = None
    height = None
    def __init__(self, width, height):
        self.width = width
        self.height = height
    
    def get_height(self):
        return self.height
    
    def get_width(self):
        return self.width
    
    def __str__(self) -> str:
        return "This is a Wooden Window!"
    
class IronWindow(Window):
    width = None
    height = None
    def __init__(self, width, height):
        self.width = width
        self.height = height
    
    def get_height(self):
        return self.height
    
    def get_width(self):
        return self.width
    
    def __str__(self) -> str:
        return "This is an Iron Window!"

class WindowFittingExpret:
    def get_description(self):
        pass

class WoodenWindowFittingExpert(WindowFittingExpret):
    def get_description(self):
        return "I'm a Wooden Window Expert!"

class IronWindowFittingExpert(WindowFittingExpret):
    def get_description(self):
        return "I'm a Iron Window Expert!"


class WindowFactory:
    def make_window(self, width, height):
        pass
    
    def make_fitting_expert(self):
        pass

class WoodenWindowFactory(WindowFactory):
    def make_window(self, width, height):
        return WoodenWindow(width, height)
    
    def make_fitting_expert(self):
        return WoodenWindowFittingExpert()

class IronWindowFactory(WindowFactory):
    def make_window(self, width, height):
        return IronWindow(width, height)
    
    def make_fitting_expert(self):
        return IronWindowFittingExpert()


    
if __name__ == "__main__":
    wooden_factory = WoodenWindowFactory()
    window = wooden_factory.make_window(10, 10)
    expert = wooden_factory.make_fitting_expert()
    print(window)
    print(expert.get_description())

    iron_factory = IronWindowFactory()
    window = iron_factory.make_window(10, 10)
    expert = iron_factory.make_fitting_expert()
    print(window)
    print(expert.get_description())