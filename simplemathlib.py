#this is a library ive been working on for quite a bit
#its a basic non bloated but probably slow math library

def abs(N):
    if N == 0:
        return 0
    
    if N > 0:
        return N
    
    if N < 0:
        return N - 2*N
    
def range_calc(list,delta,N,start):
    mult = 1
    chips = delta / N
    range_list = [start]
    __start__ = list[0]
    for i in range(N):
        range_list.append(start + (chips * mult))
        mult = mult + 1
    
    return range_list

class Complex:
    def __init__(self, R : float, C : float):
        self.a = R
        self.b = C
    def __add__(self, other : Complex):
        return Complex(self.a + other.a, self.b + other.b)
    def __sub__(self, other : Complex):
        return Complex(self.a - other.a, self.b - other.b)
    def __iadd__(self, other : Complex):
        self.a += other.a
        self.b += other.b
    def __isub__(self, other : Complex):
        self.a -= other.a
        self.b -= other.b
    def __radd__(self, other):
        return self.__add__(other)
    def __rsub__(self, other):
        return self.__sub__(other)
    def __neg__(self):
        return Complex(-self.a, -self.b)
    def __invert__(self):
        return Complex(self.a, -self.b)
    def __mul__(self, other):
        if(isinstance(other,(float,int))):
            return Complex(self.a * other, self.b * other)
        if(isinstance(other,(Complex))):
            return Complex(
                (self.a * other.a) - (self.b * other.b), 
                (self.a * other.b) + (self.b * other.a)
                )
        

class array():
    def make():
        array_base = []
        return []
    
    def add(item,contaner):
        
        if contaner != dict:
            ValueError
        contaner.append(item)

class Vector:
    def __init__(self, dtype, dim): 
        self.dtype = dtype
        self.dim = dim 
        #i took an hour of procrastinating before writing these two lines
        self.array = [dtype()]*dim
        print(self.array)
    def __getitem__(self, key):
        return self.array[key]
    def __setitem__(self, key, value): 
        if(isinstance(value,self.dtype)):
            self.array[key] = value
        print(self.array)


