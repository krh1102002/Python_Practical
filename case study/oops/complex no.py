question='''Write a python program to perform the following operations on complex numbers by 
creating a class complex_number. Create two objects c1 and c2.
a. Addition
b. Subtraction
c. Multiplication
d. Check if two complex numbers are equal or not
e. Check if c1>=c2
f. Check if c1==c2
Perform these operations using operator overloading in python'''


class complex_number:
    def __init__(self,real,img):
        self.real=real
        self.imaginary=img
    def display_complex(self):
        print(self.real,' + ',self.imaginary,'i',sep='')
    def __add__(self, other):
        return complex_number(self.real+other.real,self.imaginary+other.imaginary)
    def __sub__(self, other):
        return complex_number(self.real-other.real,self.imaginary-other.imaginary)
    def __mul__(self, other):
        return complex_number(self.real*other.real,self.imaginary*other.imaginary)
    def __eq__(self, other):
        return self.real==other.real and self.imaginary==other.imaginary
    def __le__(self, other):
        return self.real<=other.real and self.imaginary<=other.imaginary
    def __ge__(self, other):
        return self.real>=other.real and self.imaginary>=other.imaginary

c1=complex_number(10,9)
c2=complex_number(8,4)
print("c1 = ",end='')
c1.display_complex()
print("c2 = ",end='')
c2.display_complex()

print("c1 + c2 =",end='')
(c1+c2).display_complex()

print("c1 - c2 =",end='')
(c1-c2).display_complex()

print("c1 * c2 =",end='')
(c1*c2).display_complex()

print("c1 <= c2:",end='')
print(bool(c1<=c2))

print("c1 >= c2:",end='')
print(bool(c1>=c2))

print("c1 == c2:",end='')
print(bool(c1==c2))