class Datatypes():
    
    def __init__(self, *args):
        self.args = list(args[0])
        
    def __call__(self):
        print(self.args)

    @classmethod
    def from_list(cls, arglist):
        args = tuple(arglist)
        instance = cls(args)
        return instance

    @classmethod
    def from_tuple(cls, argtuple):
        args = argtuple
        instance = cls(args)
        return instance

    @classmethod
    def from_dict(cls, argdict):
        args = tuple(argdict.values())
        instance = cls(args)
        return instance
    
list_instance = Datatypes.from_list(["one", "two", "three"])
tuple_instance = Datatypes.from_tuple(("one", "two", "three"))
dict_instance = Datatypes.from_dict({1:"one", 2:"two", 3:'three'})

list_instance() # runs __call__ method in the class (by default).
tuple_instance()
dict_instance()

