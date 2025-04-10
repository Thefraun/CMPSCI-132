# class MyInt():
#     def __init__(self, val=0):
#         if type(val) == int:
#             self.__val = val
#         else:
#             self.__val = 0
            
#     def __str__(self):
#         return str(self.__val)
    
#     def __add__(self, b):
#         assert type(b) == MyInt, 'b\'s type is not MyInt'
#         return MyInt(self.__val + b.__val)
    
#     def __iadd__(self, b):
#         assert type(b) == MyInt
#         self.__val = self.__val + b.__val
#         return self
    
#     def __eq__(self, b):
#         assert type(b) == MyInt
#         return self.__val == b.__val
    
#     def __int__(self):
#         return self.__val

# class A:
#     __slots__ = ['a', 'b', '__c']
#     def __init__(self):
#         self.a = 1
#         self.b = 'xyz'
#         self.d = 1.23
#     def get(self):
#         return self.__c
#     def set(self, val):
#         self.__c = val

# a = A()

def reverse(str):
    temp = ""
    for i in range(1, len(str) + 1):
        temp+=str[-i]
    return temp
print(reverse("hellos"))