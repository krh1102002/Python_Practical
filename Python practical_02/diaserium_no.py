#Diaserium No
n=input("Enter the number : ")
b=len(n)
x=int(n)
temp=x
sum=0
v=0
while(x>0):
    v=x%10
    sum=sum + (v**b)
    b=b-1
    x=x//10
if(sum==temp):
    print("Yes,Diaserium No")
else:
    print("No,Not a Diaserium No")