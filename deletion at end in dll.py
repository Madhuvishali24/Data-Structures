class node():
    def __init__(self,data):
        self.data=data
        self.prev=None
        self.next=None
class DLL():
    def __init__(self):
        self.head=None
    def insert(self):
        new_node=node(67)
        temp=self.head
        
        while temp.next is not None:
            temp=temp.next
        temp.next=new_node
        new_node.prev=temp

    def display(self):
        if self.head is None:
            print("linked list is empty")
        else:
            temp=self.head
            while(temp):
                print(temp.data,"<-->",end=" ")
                temp=temp.next
obj =DLL()
n1=node(100)
obj.head=n1
n2=node(40)
n1.next=n2
n2.prev=n1
n3=node(65)
n2.next=n3
n3.prev=n2
print("before insertion")
obj.display()
print(" ")
print("after insertion" )
obj.insert()
obj.display()

