#quadric equation
import math
a=int(input("Enter the value of a : "))
b=int(input("Enter the value of b : "))
c=int(input("Enter the value of c : "))
d=math.sqrt(b**2- 4 * a * c)
res1= (-b + d) / (2 * a)
res2= (-b - d) / (2 * a)
print("first result is : ",res1)
print("second result is :",res2)
