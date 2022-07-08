# Program to print centre aligned triangle

r=int(input("Enter number of rows: "))
for i in range(1,r+1):
    s=r-i
    while(s>0):
        print(" ",end='')
        s-=1
    c=1
    while(c<=2*i-1):
        print("*",end='')
        c+=1
    print()