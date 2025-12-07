
# N-Dimension Vector
import numpy as np
class Vector:
    def __init__(self,vec1,pi=0.5):
        self.vec1 = vec1  #nD( n-Dimension of a vector)
        self.pi = pi

    def __check(self,vec2):
        if len(self.vec1) != len(vec2.vec1):
            raise ValueError("Vector dimension not equal!")
    

    def __add__(self,vec2):
        self.__check(vec2)
        add = [i+j for i,j in zip(self.vec1,vec2.vec1)]
        return  add
    
    def __sub__(self,vec2):
        self.__check(vec2)
        sub = [i-j for i,j in zip(self.vec1,vec2.vec1)]
        return  sub

    
    def __mul__(self,vec2):
        self.__check(vec2)
        dot_Product = sum([i*j for i,j in zip(self.vec1,vec2.vec1)])
        return (dot_Product,self.__magnitude(vec2))
    
    # Calculate magnitude of vectors(dot product)
    def __magnitude(self,vec2):
        magnitude_vec1 = (sum([i**2 for i in self.vec1]))**0.5
        magnitude_vec2 = (sum([i**2 for i in vec2.vec1]))**0.5
        
        magnitude = (magnitude_vec1*magnitude_vec2)*np.cos(self.pi)
        return round(magnitude,2)

def format_sign(sign):
    if not sign :
        return None
    
    result = []
    for i,v in enumerate(sign):
    
        if v > 0:
            result.append(f"+ {v}k{i}")
        elif v < 0 :
            result.append(f"- {abs(v)}k{i}")
        else:
            result.append(f"{v}k{i}")
    
    if result:
        s = ' '.join(result)
        if s.startswith('+ '):
            return s[2:]
        return s
    


a = (2,3,-4,3,-1)
b = (1,-9,0,1,-5)

v1 = Vector(a)
v2 = Vector(b)
print(f"Addition :   {(format_sign(v1+v2))}")
print(f"Subtration : {(format_sign(v1-v2))}")
prod,mag = v1*v2
print(f"DotProduct : {prod}")
print(f"Magnitude:   {mag}rad")
