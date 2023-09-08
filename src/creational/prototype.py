from copy import copy, deepcopy

class Component:
    def __init__(self, some_int, some_list_of_objects, some_circular_ref):
        self.some_int = some_int
        self.some_list_of_objects = some_list_of_objects
        self.some_circular_ref = some_circular_ref
    
    def __copy__(self):
        some_list_of_objects = copy(self.some_list_of_objects)
        some_circular_ref = copy(self.some_circular_ref)
        new = self.__class__(self.some_int, some_list_of_objects, some_circular_ref)
        new.__dict__.update(self.__dict__)
        return new
    
    def __deepcopy__(self, memo={}):
        some_list_of_objects = copy(self.some_list_of_objects)
        some_circular_ref = copy(self.some_circular_ref)
        new = self.__class__(self.some_int, some_list_of_objects, some_circular_ref)
        new.__dict__ = deepcopy(self.__dict__, memo)
        return new
    