# Python program to count number of tuples in a list

from sys import stdin, stdout, setrecursionlimit
def inlist(): return list(map(str, stdin.readline().strip().split()))
print("This is a python program to find tuples with all elements divisible by k in a list")
print("-------------------------------------------------------------------------------------\n")
l=eval(input("Enter a list of tuples: "))
k=int(input("Enter the value of k: "))
count=True
t=[]
for i in l:
    if type(i)==tuple:
        for j in i:
            if j%k!=0:
                break
        else:
            t.append(i)
            count=False
if count:
    print("There are no tuples in the given list with all elements divisible by",k)
else:
    print("The tuples with all elements divisible by",k,"are: ")
    for i in t:
        print(i)