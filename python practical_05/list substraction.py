# Python program to compute difference between 2 lists

from sys import stdin, stdout, setrecursionlimit
def inlist(): return list(map(str, stdin.readline().strip().split()))
print("This is a python program to multiply 2 lists ")
print("-------------------------------------------------------------------------------------\n")
print("Enter the elements of list A seperated by space: ")
a=inlist()
print("Enter the elements of list B seperated by space: ")
b=inlist()
print("A - B gives")
ans=a.copy()
for i in a:
    if i in b:
        b.remove(i)
        ans.remove(i)
for i in ans:
    print(i,end=' ')
