# Python program to find sum of tuple elements

from sys import stdin, stdout, setrecursionlimit
def intuple(): return tuple(map(int, stdin.readline().strip().split()))
print("This is a python program to find sum of tuple elements ")
print("-------------------------------------------------------------------------------------\n")
print("Enter the elements of tuple seperated by space: ")
t=intuple()
s=0
for i in t:
    s+=i
print("The sum of tuple elements is",s)