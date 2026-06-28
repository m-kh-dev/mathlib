#this is a library ive been working on for quite a bit
#its a basic non bloated but probably slow math library
from typing import List, Any, Optional
from math import atan, sin, cos, sqrt
import ctypes as ct

REAL = float|int

AXIES = {
    "x" : 0,
    "y" : 1,
    "z" : 2,
    "w" : 3
}

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
    def __init__(self, R : Optional[REAL], C : Optional[REAL]):
        self.a = R if (R!=None) else 0.0
        self.b = C if (C!=None) else 0.0
    def __add__(self, other):
        if(isinstance(other,REAL)):
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
        if(isinstance(other,REAL)):
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
    def imaginery(self):
        return self.b
    def conjugate(self):
        return Complex(self.a, -self.b)
    def __str__(self):
        return(f"""{self.a} + {self.b}i""")
    def fromAngle(a : Optional[REAL], r : Optional[REAL]):
        return (Complex(cos(a),sin(a))*r)
    def __abs__(self):
        return sqrt(self.a**2 + self.b**2)

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
def ComplexfromAngle(a : Optional[REAL], r : Optional[REAL]):
    return (Complex(cos(a),sin(a))*r)


class Vector():
    def __init__(self, dtype : Optional[REAL], dim : REAL): 
        self.dtype = dtype
        self.dim = dim 
        #i took an hour of procrastinating before writing these two lines
        self.array = [dtype()]*(dim-1)
    def __init__(self, initList : Optional[List[REAL]]): 
        self.dtype = type(initList[0])
        self.dim = len(initList)
        self.array = initList
    def __getitem__(self, key):
        return self.array[key]
    def __setitem__(self, key, value): 
        if(isinstance(value,self.dtype)):
            self.array[key] = value
    def __mul__(self, other):
        if(isinstance(other, REAL)):
            temp = self.array.copy()
            for n in range(self.dim):
                temp[n]*=other
        elif(isinstance(other, Vector)):
            if(other.dim == self.dim):
                temp = self.array.copy()
                for n in range(self.dim):
                    temp[n]*=other[n]
        else:
            raise ArithmeticError("unsupported opration")
        return temp
    def __str__(self):
        return str(self.array)
    def innerProduct(self, other):
        if(isinstance(other,Vector)):
            temp = 0
            for i in range(self.dim):
                temp += self[i]*other[i]
        return temp
    def __add__(self, other):
        if(isinstance(other, Vector)):
            if(other.dim == self.dim):
                temp = self.array.copy()
                for n in range(self.dim):
                    temp[n]+=other[n]
        else:
            raise ArithmeticError("unsupported opration")
        return temp
    def __neg__(self):
        temp = self.array.copy()
        for n in range(self.dim):
            temp[n] = -temp[n]
        return temp
    def __sub__(self, other):
        return self.__add__(-other)
    def __mod__(self, other):
        return self.innerProduct(other)
    def __iadd__(self, other):
        self = self + other
    def __isub__(self, other):
        self = self - other
    def __imul__(self, other):
        self = self*other
    def __itruediv__(self, other):
        self = self/other
    def __truediv__(self, other):
        if(isinstance(other,REAL)):
            return self*(1/other)
    def __radd__(self, other):
        return(self.__add__(other))
    def __rsub__(self, other):
        return(self.__sub__(other))
    def __rmul__(self, other):
        return(self.__mul__(other))
    def squaredMagnitude(self):
        temp = 0
        for i in range(self.dim):
            temp += self[i]**2
        return temp
    def magnitude(self):
        return sqrt(self.squaredMagnitude())
    def __abs__(self):
        return self.magnitude()
    def __invert__(self):
        return self.squaredMagnitude()
    def normalized(self):
        return self/abs(self)
    def normalize(self):
        self /= abs(self)
    def __getattr__(self, attr):
        if(attr in AXIES):
            return self.array[AXIES[attr]]
        else:
            raise AttributeError("does not exist")
    def __xor__(self, other):
        self.innerProduct(other)


class Vector2(Vector):
    def __init__(self, x : Optional[REAL], y : Optional[REAL]):
        c1 = x if x!=None else 0.0
        c2 = y if y!=None else x
        super().__init__([c1,c2])
    def crossProduct(self, other):
        return (self.x*other.y) - (self.y*other.x)
    def __pow__(self, other):
        self.crossProduct(other)
    def __rpow__(self, other):
        self.__pow__(other)
    def __ipow__(self, other):
        self = self**other
class Vector3(Vector):
    def __init__(self, x : Optional[REAL], y : Optional[REAL], z : Optional[REAL]):
        c1 = x if x!=None else 0.0
        c2 = y if y!=None else x
        c3 = z if z!=None else y
        super().__init__([c1,c2,c3])
    def crossProduct(self, other : Vector3):

        return Vector3(self.y*other.z-self.z*other.y,
                       self.z*other.x-self.x*other.z,
                       self.x*other.y-self.y*other.x)
    def __pow__(self, other):
        self.crossProduct(other)
    def __rpow__(self, other):
        self.__pow__(other)
    def __ipow__(self, other):
        self = self**other
    
    
def crossProduct(self : Vector2|Vector3, other : Vector2|Vector3):
        if(isinstance(self,Vector2),isinstance(other,Vector2)):
            return (self.x*other.y) - (self.y*other.x)
        if(isinstance(self,Vector3),isinstance(other,Vector3)):
            return Vector3(self.y*other.z-self.z*other.y,
                           self.z*other.x-self.x*other.z,
                           self.x*other.y-self.y*other.x)
        else:
            raise ArithmeticError("undefined Opration")
def innerProduct(self, other):
    if(isinstance(other,Vector)):
        temp = 0
        for i in range(self.dim):
            temp += self[i]*other[i]
    return temp
def squaredMagnitude(self):
    return ~self
def magnitude(self):
    return abs(self)
def normalized(self):
    return self/abs(self)
def normalize(self):
    self /= abs(self)