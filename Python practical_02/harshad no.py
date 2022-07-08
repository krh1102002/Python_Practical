#Harshad no
n=int(input("Enter the number : "))
temp=n
sum=0
x=0
while(temp>0):
    x=temp%10
    sum+=x
    temp=temp//10
if(n%sum==0):
    print("Harshad No")
else:
    print("Not a harshad No")