# Program to print happy numbers between 1 to 100
def sumofsqofdig(n):
    s=0
    for i in str(n):
        s+=int(i)*int(i)
    return s

print("Happy numbers between 1 to 100 are: ")
for n in range(1,101):
    ans=sumofsqofdig(n)
    while ans!=1 and ans!=4:
        ans=sumofsqofdig(ans)

    if ans==1:
        print(n)