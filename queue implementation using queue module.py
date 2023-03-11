import queue
Q=queue.Queue(maxsize=5)
Q.put(4)
Q.put(6)
Q.put(8)
print(type(Q))
print(Q.get())
print(Q.get())
print(Q.empty())
