# Python program to find size of tuple

from sys import stdin, stdout, setrecursionlimit
def intuple(): return tuple(map(int, stdin.readline().strip().split()))
print("This is a python program to find size of tuple ")
print("-------------------------------------------------------------------------------------\n")
print("Enter the elements of tuple seperated by space: ")
t=intuple()
s=0
for i in t:
    s+=1
print("The size of entered tuple is",s)