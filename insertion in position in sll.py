class node:
    def __init__(self,data):
        self.data=data
        self.next=None
class SLL():
    def __init__(self):
        self.head=None
    def insertion(self,pos,data):
        new_node=node(data)
        temp=self.head
        for i in range(pos-1):
            temp=temp.next
        new_node.next=temp.next
        temp.next=new_node
    def display(self):
        if self.head is None:
            print("list is empty")
        else:
            temp=self.head
            while(temp):
                print(temp.data,"==>",end=" ")
                temp=temp.next
obj=SLL()
n1=node(56)
obj.head=n1
n2=node(58)
n1.next=n2
n3=node(59)
n2.next=n3
print("before insertion")
obj.display()
print(" ")
print("after insertion")
obj.insertion(2,30)
obj.display()
