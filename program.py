stack_1=[]
stack_2=[]
def push():
    for i in range(5):
        e=int(input("enter the element"))
        if e%2==0:
            stack_1.append(e)
        
        else:
            stack_2.append(e)
def pop():
    print("1.stack_1 2.stack_2")
    option=int(input())
    if option==1:
        element=stack_1.pop()
        print("removed element",element)
    elif option==2 :
         element=stack_2.pop()
         print("removed element",element)
        
    else:
        print("enter the correct option")
            
def display():
    print("1 or 2")
    choice=int(input())
    if choice==1:
        print(stack_1)
    elif choice==2 :
        print(stack_2)
    else:
        print("enter the correct choice")
while True:
    print("select the choice 1.push 2.pop 3.display 4.quit")
    choice=int(input())
    if choice==1:
        push()
    elif choice==2:
        pop()
    elif choice==3:
        display()
    elif choice==4:
        break
    else:
        print("enter the right choice")
