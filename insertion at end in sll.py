class node():
    def __init__(self,data):
        self.data=data
        self.next=None
class SLL():
    def __init__(self):
        self.head=None
    def insertion_end(self,data):
        new_node=node(data)
        temp=self.head
        while temp.next:
            temp=temp.next
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
n1=node(2)
obj.head=n1
n2=node(6)
n1.next=n2
print("before insertion")
obj.display()
print(" ")
print("after insertion")
obj.insertion_end(10)
obj.display()
