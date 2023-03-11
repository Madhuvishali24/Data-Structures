class node:
    def __init__(self,data):
        self.data=data
        self.next=None
class Queue:
    def __init__(self):
        self.head=None
        self.last=None
    def enqueue(self,data):
        if self.head is None:
            self.head=node(data)
            self.last=self.head
        else:
            self.last.next=node(data)
            self.last=self.last.next
    def dequeue(self):
        if self.head is None:
            return None
        else:
            to_return=self.head.data
            self.head=self.head.next
            return to_return
a_queue=Queue()
while True:
    print('enqueue<value>')
    print('dequeue')
    print('quit')
    do=input("what would you like to do ?").split()
    operation=do[0].strip().lower()
    if operation =='enqueue':
        a_queue.enqueue(int(do[1]))
    elif operation=='dequeue':
        dequeued=a_queue.dequeue()
        if dequeued is None:
            print("queue is empty")
        else:
            print("dequeued element : ",int(dequeued))
    elif operation=='quit':
        break