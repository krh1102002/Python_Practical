# Python Program to Print Diamond Star Pattern

rows = int(input("Enter Diamond Pattern Rows : "))

print("Diamond Star Pattern")
k = 0
for i in range(1, rows + 1):
    for j in range(1, rows - i + 1):
        print(end=' ')
    while k != 2 * i - 1:
        print('*', end='')
        k = k + 1
    k = 0
    print()

k = 2
l = 1
for i in range(1, rows):
    for j in range(1, k):
        print(end=' ')
    k = k + 1
    while l <= (2 * (rows - i) - 1):
        print('*', end='')
        l = l + 1
    l = 1
    print()