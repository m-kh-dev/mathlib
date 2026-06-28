#this is a library ive been working on for quite a bit
#its a basic non bloated but probably slow math library
from typing import List, Any, Optional
from math import atan, sin, cos

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

class array():
    def make():
        array_base = []
        return []
    
    def add(item,contaner):
        
        if contaner != dict:
            ValueError
        contaner.append(item)


class Complex():
    def __init__(self, R : Optional[float], C : Optional[float]):
        self.a = R if (R!=None) else 0.0
        self.b = C if (C!=None) else 0.0
    def __add__(self, other):
        if(isinstance(other,(float,int))):
            return Complex(self.a + other, self.b)
        if(isinstance(other,(Complex))):
            return Complex(self.a + other.a, self.b + other.b)
    def __sub__(self, other):
        return self.__add__(-other)
    def __iadd__(self, other):
        self = self.__add__(other)
    def __isub__(self, other):
        self = self.__sub__(other)
    def __radd__(self, other):
        return self.__add__(other)
    def __rsub__(self, other):
        return self.__sub__(other)
    def __neg__(self):
        return Complex(-self.a, -self.b)
    def __invert__(self):
        return self.conjugate()
    def __mul__(self, other):
        if(isinstance(other,(float,int))):
            return Complex(self.a * other, self.b * other)
        if(isinstance(other,(Complex))):
            return Complex(
                (self.a * other.a) - (self.b * other.b), 
                (self.a * other.b) + (self.b * other.a)
                )
    def __imul__(self, other):
        self = self.__mul__(other)
    def __int__(self):
        return int(self.a)
    def __float__(self):
        return (self.a)
    def toVector(self):
        return Vector([self.a, self.b])
    def argument(self):
        return atan(self.b/self.a)
    def flip(self):
        return Complex(self.b, self.a)
    def real(self):
        return self.a
    def complex(self):
        return self.b
    def conjugate(self):
        return Complex(self.a, -self.b)
    def __str__(self):
        return(f"""{self.a} + {self.b}i""")
    def fromAngle(a : Optional[float], r : Optional[float]):
        return (Complex(cos(a),sin(a))*r)
    



def toVector(self):
    return Vector([self.a, self.b])
def argument(self):
    return atan(self.b/self.a)
def flip(self):
    return Complex(self.b, self.a)
def real(self):
    return self.a
def complex(self):
    return self.b
def conjugate(self):
    return Complex(self.a, -self.b)
def ComplexfromAngle(a : Optional[float], r : Optional[float]):
    return (Complex(cos(a),sin(a))*r)


class Vector():
    def __init__(self, dtype : Optional[Any], dim : int): 
        self.dtype = dtype
        self.dim = dim 
        #i took an hour of procrastinating before writing these two lines
        self.array = [dtype()]*dim
        print(self.array)
    def __init__(self, initList : List[Any]): 
        self.dtype = type(initList[0])
        self.dim = len(initList)
        #i took an hour of procrastinating before writing these two lines
        self.array = initList
        print(self.array)
    def __getitem__(self, key):
        return self.array[key]
    def __setitem__(self, key, value): 
        if(isinstance(value,self.dtype)):
            self.array[key] = value
        print(self.array)


