class node:
    def __init__(self,data):
        self.data=data
        self.next=None
class stack():
    def __init__(self):
        self.head=None
    def isempty(self):
        if self.head==None:
            return True
        else:
            return False
    def push(self,data):
        if self.head==None:
            self.head=node(data)
        else:
            newnode=node(data)
            newnode.next=self.head
            self.head=newnode
    def pop(self):
        if self.isempty():
            return None

        else:
            poppednode=self.head
            self.head=self.head.next
            poppednode.next=None
            return poppednode.data
    def peek(self):
        if self.isempty():
            return None
        else:
            return self.head.data
    def display(self):
        temp=self.head
        if self.isempty():
            print("stack is underflow")
        else:
            while(temp != None):
                print(temp.data, end = " ")
                temp=temp.next
                if(temp != None):
                    print("-->",end =" ")
            return
s=stack()
s.push(5)
s.push(10)
s.push(15)
s.push(20)
s.display()
print("")
print("peek :",s.peek())
s.pop()
s.display()
print("")
s.pop()
s.display()
print("")
print("peek :",s.peek())
        
    

    
    
