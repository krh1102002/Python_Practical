# Python program to multiply 2 lists

from sys import stdin, stdout, setrecursionlimit
def inlist(): return list(map(str, stdin.readline().strip().split()))
print("This is a python program to multiply 2 lists ")
print("-------------------------------------------------------------------------------------\n")
print("Enter the elements of first list seperated by space: ")
a=inlist()
print("Enter the elements of second list seperated by space: ")
b=inlist()

print("The multiplication of the given matrices is as follows: ")
for i in a:
    for j in b:
        print(i+j,end=" ")
