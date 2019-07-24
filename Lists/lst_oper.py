"""Menu driven program for list operation"""
lst = [ ]
def add(ele):
    lst.append(ele)
def pop():
    if len(lst)==0:
        print("Empty list!!")
    else:
        x=0
        x=lst.pop()
        print(f"{x} is popped out!!")

def search(ele):
    if len(lst)==0:
        print("Empty list!!")
    else:
        if ele in lst:
            index=lst.index(ele)
            print(f"{ele} is found in {index}")
        else:
            print("Element not found!!")
            
def display( ):
    if len(lst)==0:
        print("Empty list!!")
    else:
        print(lst)

while True:
    print("1.Add 2.Pop 3.Search 4.Display 5.Exit")
    choice=int(input("Enter your choice:"))
    if choice==1:
        ele=int(input("Enter the element to be added:"))
        add(ele)
    elif choice==2:
        pop()
    elif choice==3:
        ele=int(input("Enter the search element:"))
        search(ele)
    elif choice==4:
        display()
    else:
        break
print("THANK YOU. HAVE A NICE DAY!!")