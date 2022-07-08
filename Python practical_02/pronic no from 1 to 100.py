# Program to print pronic numbers between 1 to 100
import math
print("Pronic numbers between 1 to 100 are: ")
for n in range(1,101):
    for i in range(int(math.sqrt(n))+1):
        if i*(i+1)==n:
            print(n)
            break