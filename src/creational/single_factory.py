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
    
class WindowFactory:
    @staticmethod
    def make_window(width, height):
        return WoodenWindow(width, height)
    
if __name__ == "__main__":
    window = WindowFactory.make_window(10, 10)
    print(window.get_height())
    print(window.get_width())