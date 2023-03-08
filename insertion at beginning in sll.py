class node:
    def __init__(self,data):
        self.data=data
        self.next=None
class SLL():
    def __init__(self):
        self.head=None
    def insertion(self,data):
        new_node=node(data)
        new_node.next=self.head
        self.head=new_node
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
print("before insertion")
obj.display()
print(" ")
print("after insertion")
obj.insertion(1)
obj.display()
