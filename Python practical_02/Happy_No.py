#Happy No
def ishappy(num):
    sum=0
    n=num
    while(n>0):
        x=n%10
        sum=sum + (x**2)
        n=n//10
    return sum
n=int(input("Enter the No : "))
temp=ishappy(n)
b=0
b1=False
if(temp==1):
    print("Happy No ")
    b1=True
elif(temp==4):
    print("Not a happy No ")
else:
    while temp>=10:
        temp=ishappy(temp)
        if(temp==1):
            print("Happy No ")
            b1=True
            break
if(b1==False):
    print("Not a Happy No ")
