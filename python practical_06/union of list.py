# Python program to print union of 2 lists

from sys import stdin, stdout, setrecursionlimit
def inlist(): return list(map(str, stdin.readline().strip().split()))
print("This is a python program to print union of 2 lists ")
print("-------------------------------------------------------------------------------------\n")
print("Enter the elements of list A seperated by space: ")
a=inlist()
print("Enter the elements of list B seperated by space: ")
b=inlist()
print("Union of the given lists is: ")
for i in a:
    print(i,end=' ')
    if i in b:
        b.remove(i)
for i in b:
    print(i,end=' ')