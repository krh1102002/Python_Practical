# Program to find length of list using recursion

from sys import stdin, stdout, setrecursionlimit
def inlist(): return list(map(str, stdin.readline().strip().split()))

def lengthOfList(l):
    global length
    if l:
        length+=1
        lengthOfList(l[1::])

print("This is a python program to find length of list using recursion ")
print("-------------------------------------------------------------------------------------\n")
print("Enter the elements of list seperated by space: ")
l = inlist()
length = 0
lengthOfList(l)
print("Length of the given list is ", length)