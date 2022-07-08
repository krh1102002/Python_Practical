# Program to check if the list contains 3 consecutive common numbers

from collections import Counter
from sys import stdin, stdout, setrecursionlimit
def inlist(): return list(map(int, stdin.readline().strip().split()))

print("This is a python program to check if the list contains 3 consecutive common numbers")
print("-------------------------------------------------------------------------------------\n")
print("Enter the elements of list seperated by space: ")
l=inlist()
key=l[0]
count=1
for i in l[1::]:
    if key==i:
        count+=1
    else:
        count=1
        key=i
    if count>=3:
        print("Yes, the given list contains 3 consecutive common numbers")
        break
else:
    print("No, the list does not contain 3 consecutive common numbers")