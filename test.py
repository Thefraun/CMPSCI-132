class MyInt():
    def __init__(self, val=0):
        if type(val) == int:
            self.__val = val
        else:
            self.__val = 0
            
    def __str__(self):
        return str(self.__val)
    
    def __add__(self, b):
        assert type(b) == MyInt, 'b\'s type is not MyInt'
        return MyInt(self.__val + b.__val)
    
    def __iadd__(self, b):
        assert type(b) == MyInt
        self.__val = self.__val + b.__val
        return self
    
    def __eq__(self, b):
        assert type(b) == MyInt
        return self.__val == b.__val
    
    def __int__(self):
        return self.__val

a = MyInt(1)
b = MyInt(5)
print(int(a))