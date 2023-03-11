stack=[]
def push():
    
        element=int(input("enter the element"))
    stack.append(element)
    print(stack)
def pop():
    if not stack:
        print("stack is empty")
    else:
        element=stack.pop()
        print("removed element",element)
        print(stack)
while True:
    print("select the choice 1.push 2.pop 3.quit")
    choice=int(input())
    if choice==1:
        push()
    elif choice==2:
        pop()
    elif choice==3:
        break
    else:
        print("enter the right choice")
