# Armstrong  No
n=input("Enter the number")
b=len(n)
b1=int(n)
sum=0
temp=b1
x=0
while b1>0:
    x=b1%10
    sum += (x**b)
    b1=b1//10
if(sum==temp):
    print("Armstrong no")
else:
    print("no")