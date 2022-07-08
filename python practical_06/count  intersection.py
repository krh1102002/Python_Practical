# Python program to print intersection of 2 lists

from sys import stdin, stdout, setrecursionlimit
from collections import Counter
def inlist(): return list(map(str, stdin.readline().strip().split()))
print("This is a python program to print intersection of 2 lists ")
print("-------------------------------------------------------------------------------------\n")
print("Enter the elements of list A seperated by space: ")
a=inlist()
print("Enter the elements of list B seperated by space: ")
b=inlist()
A=Counter(a)
B=Counter(b)
print("Intersection of the given lists is: ")
for i in A:
    if i in B:
        x=min(A[i],B[i])
        for j in range(x):
            print(i,end=' ')
