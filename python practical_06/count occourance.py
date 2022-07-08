# Program to count occurences of all words in a sentence

from collections import Counter

print("This is a python program to count occurences of all words in a sentence ")
print("-------------------------------------------------------------------------------------\n")
s=input("Enter a string: ")
l=list(map(str, s.split(" ")))
d=Counter(l)
print(d)
print("Number of occurences of each word in the given sentence are: ")
for i in d:
    print(i,d[i],sep=': ')