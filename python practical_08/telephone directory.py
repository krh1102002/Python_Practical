# Telephone Directory

def find_num():
    key=input("Enter the name whose number you want to find: ")
    print("Number of ",key,"is",d[key])
def replace_val():
    k=input("Enter the name whose number is to be updated")
    v=int(input("Enter the new number: "))
    d[k]=v
def save():
    k=input("Enter the name: ")
    v=int(input("Enter the number: "))
    d[k]=v
def delete():
    k=input("Enter the name whose number you want to delete: ")
    try:
        d.pop(k)
    except:
        print("Entered key doesn't exist")
def help():
    print('''Choose the function you want to perform
                1. Find number
                2. Update a number
                3. Save a new number
                4. Delete existing number
                5. Display directory\n
                Enter any other key for this help
                Enter x to exit''')
def display():
    print(d)
d={"Kunal":9356569973,"Aryan":9527254842,"Prathamesh":9665130307,"Sid":9529081242,"Prajwal":9284064551,"Mokshada":7774099312,"Aditya":7744847083,"Riddhish":8237732809,"Ruddhi":9604983716,"Hemangi":8668741113}

if __name__=='__main__':
    help()
    while(True):
        key=str(input("Enter your choice: "))
        if key=='1':
            find_num()
        elif key=='2':
            replace_val()
        elif key=='3':
            save()
        elif key=='4':
            delete()
        elif key=='5':
            display()
        elif key in "xX":
            print("Thank-you")
            break
        else:
            help()