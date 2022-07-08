# Python program to find max and min elements of tuple

from sys import stdin, stdout, setrecursionlimit
def intuple(): return tuple(map(int, stdin.readline().strip().split()))
print("This is a python program to find size of tuple ")
print("-------------------------------------------------------------------------------------\n")
print("Enter the elements of tuple seperated by space: ")
t=intuple()
s=0
min=t[0]
max=t[0]
for i in t:
    if i>max:
        max=i
    if i<min:
        min=i
print("The maximum element in the enetered tuple is",max)
print("The minimum element in the enetered tuple is",min)