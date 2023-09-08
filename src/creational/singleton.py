class SingletonMeta(type):
    _instances = {}

    def __call__(cls, *args, **kwargs):
        if cls not in cls._instances:
            instance = super().__call__(*args, **kwargs)
            cls._instances[cls] = instance
        return cls._instances[cls]

class MyClass(metaclass=SingletonMeta):
    def __init__(self, value):
        self.value = value
    
    def get_value(self):
        return self.value

if __name__ == "__main__":

    instance0 = MyClass(5)
    instance1 = MyClass(10)

    print(instance0.get_value())
    print(instance1.get_value())