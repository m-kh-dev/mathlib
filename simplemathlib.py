#this is a library ive been working on for quite a bit
#its a basic non bloated but probably slow math library
from typing import List, Any, Optional
from math import atan, sin, cos, sqrt, acos, copysign
import ctypes as ct

REAL = float|int

AXIES = {
    "x" : 0,
    "y" : 1,
    "z" : 2,
    "w" : 3
}


def sign(n) -> int: 
    """Returns 0 if - and 1 if +"""
    return copysign(1.0,n) + 1.0

def range_calc(list,delta,N,start):
    chips = delta / N
    range_list = [start]
    __start__ = list[0]
    for i in range(N):
        range_list.append(start + (chips * (i+1)))
    
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
    """a complex number of the format a + bi"""
    i = None
    def __init__(self, R : Optional[REAL], C : Optional[REAL]):
        self.a = R if (R!=None) else 0.0
        self.b = C if (C!=None) else 0.0
    def __add__(self : Complex, other : Complex):
        if(isinstance(other,REAL)):
            return Complex(self.a + other, self.b)
        if(isinstance(other,(Complex))):
            return Complex(self.a + other.a, self.b + other.b)
    def __sub__(self : Complex, other : Complex):
        return self.__add__(-other)
    def __iadd__(self : Complex, other : Complex):
        self = self.__add__(other)
    def __isub__(self : Complex, other : Complex):
        self = self.__sub__(other)
    def __radd__(self : Complex, other : Complex):
        return self.__add__(other)
    def __rsub__(self : Complex, other : Complex):
        return self.__sub__(other)
    def __neg__(self):
        return Complex(-self.a, -self.b)
    def __invert__(self):
        return self.conjugate()
    def __mul__(self : Complex, other : Complex):
        if(isinstance(other,REAL)):
            return Complex(self.a * other, self.b * other)
        if(isinstance(other,(Complex))):
            return Complex(
                (self.a * other.a) - (self.b * other.b), 
                (self.a * other.b) + (self.b * other.a)
                )
    def __imul__(self : Complex, other : Complex):
        self = self.__mul__(other)
    def __int__(self : Complex):
        return int(self.a)
    def __float__(self : Complex):
        return (self.a)
    def toVector(self : Complex):
        return Vector([self.a, self.b])
    def argument(self : Complex):
        return atan(self.b/self.a)
    def flip(self : Complex):
        return Complex(self.b, self.a)
    def real(self : Complex):
        return self.a
    def imaginery(self : Complex):
        return self.b
    def conjugate(self : Complex):
        return Complex(self.a, -self.b)
    def __str__(self : Complex):
        return(f"""{self.a} {"+"*sign(self.b)} {self.b}i""")
    def fromAngle(a : Optional[REAL], r : Optional[REAL]):
        return (Complex(cos(a),sin(a))*r)
    def __abs__(self : Complex):
        return sqrt(self.a**2 + self.b**2)

Complex.i = Complex(0,1)

def toVector(self : Complex):
    return Vector([self.a, self.b])
def argument(self : Complex):
    return atan(self.b/self.a)
def flip(self : Complex):
    return Complex(self.b, self.a)
def real(self : Complex):
    return self.a
def complex(self : Complex):
    return self.b
def conjugate(self : Complex):
    return Complex(self.a, -self.b)
def ComplexfromAngle(a : Optional[REAL], r : Optional[REAL]):
    return (Complex(cos(a),sin(a))*r)

#liner algebra
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
    def __mul__(self : Vector, other):
        if(isinstance(other, REAL)):
            temp = self.array.copy()
            for n in range(self.dim):
                temp[n]*=other
        elif(isinstance(other, Vector)):
            return self.innerProduct(other)
        else:
            raise ArithmeticError("unsupported opration")
        return Vector(temp)
    def __str__(self : Vector):
        return str(self.array)
    def innerProduct(self : Vector, other : Vector):
        temp = 0
        if(isinstance(other,Vector)):
            for i in range(self.dim):
                temp += self[i]*other[i]
        return temp
    def __add__(self : Vector, other):
        if(isinstance(other, Vector)):
            if(other.dim == self.dim):
                temp = self.array.copy()
                for n in range(self.dim):
                    temp[n]+=other[n]
        else:
            raise ArithmeticError("unsupported opration")
        return Vector(temp)
    def __neg__(self : Vector):
        temp = self.array.copy()
        for n in range(self.dim):
            temp[n] = -temp[n]
        return Vector(temp)
    def __sub__(self : Vector, other):
        return self.__add__(-other)
    def __mod__(self : Vector, other : Vector):
        return self.innerProduct(other)
    def __iadd__(self : Vector, other):
        self.array = (self + other).array
        return self
    def __isub__(self : Vector, other):
        self.array = (self - other).array
        return self
    def __imul__(self : Vector, other):
        self.array = (self*other).array
        return self
    def __itruediv__(self : Vector, other):
        self.array = (self/other).array
        return self
    def __truediv__(self : Vector, other):
        if(isinstance(other,REAL)):
            return self*(1/other)
    def __radd__(self : Vector, other):
        return(self.__add__(other))
    def __rsub__(self : Vector, other):
        return(self.__sub__(other))
    def __rmul__(self : Vector, other):
        return(self.__mul__(other))
    @property
    def squaredMagnitude(self : Vector):
        temp = 0
        for i in range(self.dim):
            temp += self[i]**2
        return temp
    @property
    def magnitude(self : Vector):
        return sqrt(self.squaredMagnitude)
    def __abs__(self : Vector):
        return self.magnitude
    def __invert__(self : Vector):
        return self.squaredMagnitude
    @property
    def normalized(self : Vector):
        return self / abs(self)
    def normalize(self):
        self /= abs(self)
    def __getattr__(self, attr):
        if(attr in AXIES):
            return self.array[AXIES[attr]]
        else:
            raise AttributeError("does not exist")
    def scalerProjection(self : Vector, other : Vector):
        return innerProduct(self,other)/other.magnitude()
    def vectorProjection(self : Vector, other : Vector):
        return (innerProduct(self,other)/other.squaredMagnitude())*other
    def vectorProject(self : Vector, other : Vector):
        self.array = ((innerProduct(self,other)/other.squaredMagnitude())*other).array
        return self
    def AngleBetweenVectors(self : Vector,other : Vector):
        return acos(innerProduct(self,other)/(self.magnitude*other.magnitude))
    def AngleBetweenVectors(self : Vector,other : Vector):
        return acos(innerProduct(self,other)/(self.magnitude*other.magnitude))
    def addScaledVector(self : Vector, other : Vector, scale : REAL):
        return self + scale*other
    def perpendicularToVector(self : Vector, other: Vector):
        return (innerProduct(self,other) == 0.0)



class Vector2(Vector):
    i = None
    j = None
    def __init__(self, x : Optional[REAL], y : Optional[REAL]):
        c1 = x if x!=None else 0.0
        c2 = y if y!=None else x
        super().__init__([c1,c2])
    def crossProduct(self : Vector, other : Vector):
        return (self.x*other.y) - (self.y*other.x)
    def __pow__(self : Vector2, other : Vector2):
        return self.crossProduct(other)
    def __rpow__(self : Vector2, other : Vector2):
        return self.__pow__(other)
    def __ipow__(self : Vector2, other : Vector2):
        self.array = (self**other).array
        return self
    def toComplex(self):
        return Complex(self.x,self.y)

class Vector3(Vector):
    i = None
    j = None
    k = None
    def __init__(self, x : Optional[REAL], y : Optional[REAL], z : Optional[REAL]):
        c1 = x if x!=None else 0.0
        c2 = y if y!=None else x
        c3 = z if z!=None else y
        super().__init__([c1,c2,c3])
    def crossProduct(self, other : Vector3):

        return Vector3(self.y*other.z-self.z*other.y,
                       self.z*other.x-self.x*other.z,
                       self.x*other.y-self.y*other.x)
    def __pow__(self : Vector3, other : Vector3):
        return self.crossProduct(other)
    def __rpow__(self : Vector3, other : Vector3):
        return self.__pow__(other)
    def __ipow__(self : Vector3, other : Vector3):
        self.array = (self**other).array
        return self
    

Vector2.i = Vector2(1.0, 0.0)
Vector2.j = Vector2(0.0, 1.0)

Vector3.i = Vector3(1.0, 0.0, 0.0)
Vector3.j = Vector3(0.0, 1.0, 0.0)
Vector3.k = Vector3(0.0, 0.0, 1.0)

def crossProduct(self : Vector2|Vector3, other : Vector2|Vector3):
        if(isinstance(self,Vector2),isinstance(other,Vector2)):
            return (self.x*other.y) - (self.y*other.x)
        if(isinstance(self,Vector3),isinstance(other,Vector3)):
            return Vector3(self.y*other.z-self.z*other.y,
                           self.z*other.x-self.x*other.z,
                           self.x*other.y-self.y*other.x)
        else:
            raise ArithmeticError("undefined Opration")
def innerProduct(self : Vector, other : Vector):
    if(isinstance(other,Vector)):
        temp = 0
        for i in range(self.dim):
            temp += self[i]*other[i]
    return temp
def squaredMagnitude(self : Vector):
    return self.squaredMagnitude
def magnitude(self : Vector):
    return self.magnitude
def normalized(self : Vector):
    return self.normalized
def normalize(self : Vector):
    self /= abs(self)

def scalerProjection(self : Vector, other : Vector):
    return innerProduct(self,other)/other.magnitude()
def vectorProjection(self : Vector, other : Vector):
    return (innerProduct(self,other)/other.squaredMagnitude())*other
def vectorProject(self : Vector, other : Vector):
    self.array = ((innerProduct(self,other)/other.squaredMagnitude())*other).array
    return self

def AngleBetweenVectors(self : Vector,other : Vector):
    return acos(innerProduct(self,other)/(self.magnitude*other.magnitude))
def addScaledVector(self : Vector, other : Vector, scale : REAL):
    return self + scale*other
def perpendicularToVector(self : Vector, other: Vector):
    return (innerProduct(self,other) == 0.0)
