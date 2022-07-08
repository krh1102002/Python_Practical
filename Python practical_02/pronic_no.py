#Pronic No
import math as m
n=int(input("Enter the no : "))
b=False
for i in range(m.ceil(m.sqrt(n))):
    if(i*(i+1)==n):
        print("Pronic NO ")
        b=True
if(b==False):
    print("Not a Pronic No ")