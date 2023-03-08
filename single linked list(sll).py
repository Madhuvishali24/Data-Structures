class node():
    def __init__(self,data):
        self.data=data
        self.next=None
class SLL():
    def __init__(self):
        self.head=None
    def display(self):
        if self.head is None:
            print("linked list is empty")
        else:
            temp=self.head
            while(temp):
                print(temp.data,"==>",end=" ")
                temp=temp.next
obj =SLL()
n1=node(100)
obj.head=n1
n2=node(40)
n1.next=n2
n3=node(65)
n2.next=n3
obj.display()
