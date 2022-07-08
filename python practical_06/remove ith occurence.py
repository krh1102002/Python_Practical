# Program to remove the I-th occurrence of given word in a list where words repeat

from sys import stdin, stdout, setrecursionlimit
def inlist(): return list(map(str, stdin.readline().strip().split()))

print("This is a python program to remove the I-th occurrence of given word in a list where words repeat ")
print("-------------------------------------------------------------------------------------\n")
print("Enter the elements of list seperated by space: ")
l = inlist()
key=input("Enter the element to remove")
n=int(input("Enter which occurence of the word you want to remove: "))
x=n
for i in range(len(l)):
    if l[i]==key:
        n-=1
        if n==0:
            l.pop(i)
            break
if n:
    print(key, "doesn't occur for",x,"times in the list")
else:
    print("The list after removing",x,"th occurence of ",key,"is: ",l)
