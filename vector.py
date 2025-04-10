class Vector:
    def __init__(self, dim):
        self.__vals = [0] * dim
    
    def __str__(self):
        return f"<{str(self.__vals)[1:-1]}>"
    
    def __len__(self):
        return len(self.__vals)
    
    def __getitem__(self, idx):
        assert type(idx) == int
        assert 0 <= idx < len(self.__vals)
        return self.__vals[idx]
    
    def __setitem__(self, idx, val):
        assert type(idx) == int
        assert 0 <= idx < len(self.__vals)
        self.__vals[idx] = val
        
    def __contains__(self, val):
        for v in self.__vals:
            if v == val:
                return True
        return False
    
    def __delitem__(self, idx):
        assert type(idx) == int
        assert 0 <= idx < len(self.__vals)
        del self.__vals[idx]
        
    def __call__(self, arg1, arg2):
        return self.__vals + [arg1, arg2]
    
v = Vector(3)
v[0] = 1
v[1] = 2
v[2] = 3
del v[1]
print(v)