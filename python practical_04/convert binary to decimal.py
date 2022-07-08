# Program to convert binary to decimal

def btod(b):
    l = len(b)
    d = 0
    a = -1
    counter = 0
    while (counter < l):
        if (b[a] != '0' and b[a] != '1'):
            print('This is not binary')
            break;
        else:
            d1 = int(b[a]) * (2 ** counter)
            d += d1
        a -= 1
        counter += 1
    return (d)

n=int(input("Enter a binary number: "))
print("The decimal equivalent of binary number",n,"is ",btod(str(n)))