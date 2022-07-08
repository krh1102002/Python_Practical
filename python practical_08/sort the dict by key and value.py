# Python program to sort the given dictionary by keys and values

from collections import OrderedDict
print("This is a python program to merge 2 lists into a dictionary ")
print("-------------------------------------------------------------------------------------\n")
d=eval(input("Enter a dictionary: "))
print("The dictionary in sorted order by keys is: ")
key_sorted=OrderedDict(sorted(d.items()))
print(key_sorted)
print()
print("The dictionary in sorted order by values is: ")
val_sorted=sorted(d.items(), key=lambda kv:(kv[1], kv[0]))
print(val_sorted)

