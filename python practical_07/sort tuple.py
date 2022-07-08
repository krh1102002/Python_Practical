# Python program to sort tuples by total digits

print("This is a python program to sort tuples by total digits ")
print("-------------------------------------------------------------------------------------\n")
l=eval(input("Enter a list of tuples: "))
t=[]
for i in l:
    if type(i)!=tuple:
        print("Invalid input. You are asked to input a list of tuples")
        exit()
    t.append(len(i))
print("Tuples in sorted order by length are: ")
for i in range(len(t)):
    x=t.index(min(t))
    print(l[x])
    t[x]=float('inf')