# Program to print disarium numbers from 1 to 100
print("The disarium numbers from 1 to 100 are: ")
for n in range(1,101):
    ans=0
    for i in range(len(str(n))):
        ans+=int(str(n)[i])**(i+1)
    if(ans==n):
        print(n)