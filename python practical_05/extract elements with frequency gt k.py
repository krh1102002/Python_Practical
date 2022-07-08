# Python program to extract elements with frequency greater than k

from sys import stdin, stdout, setrecursionlimit
from collections import Counter
def inlist(): return list(map(int, stdin.readline().strip().split()))

print("This is a python program to extract elements with frequency greater than k")
print("-----------------------------------------------------------------------------\n")
print("Enter the elements of list seperated by space: ")
l=inlist()
k=int(input("Enter value of k: "))

d=Counter(l)
ans=[]
for i in d:
    if d[i]>k:
        ans.append(i)

print("Elements with frequency greater than ",k," are:")
for i in ans:
    print(i,end=' ')