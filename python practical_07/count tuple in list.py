# Python program to count number of tuples in a list

from sys import stdin, stdout, setrecursionlimit
def inlist(): return list(map(str, stdin.readline().strip().split()))
print("This is a python program to find number of tuples in a list ")
print("-------------------------------------------------------------------------------------\n")
l=eval(input("Enter a list: "))
count=0
for i in l:
    if type(i)==tuple:
        count+=1
print("The number of tuples in the given list are ",count)