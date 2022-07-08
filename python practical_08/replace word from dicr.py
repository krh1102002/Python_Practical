# Python program to replace values from the dictionary
print("This is a python program to replace values in the dictionary ")
print("-------------------------------------------------------------------------------------\n")
d=eval(input("Enter a dictionary: "))

print("\nThe entered dictionary is: \n",d)
k=eval(input("\n Enter the key whose value you want to replace: "))
v=eval(input("Enter the new value for the entered key"))
d[k]=v
print("\nThe updated dictionary is: ",d)