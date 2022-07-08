#sort array in Ascending order

n = int(input("Enter length of array : "))
list1 = []
print("Enter Elements : ")
for i in range(n):
    x = int(input())
    if (i == 0) or (x > list1[- 1]):
        list1.append(x)
    else:
        pos = 0
        while pos < len(list1):
            if x <= list1[pos]:
                list1.insert(pos, x)
                break
            pos = pos + 1

print(list1)