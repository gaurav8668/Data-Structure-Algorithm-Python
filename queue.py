from collections import deque
import time
import threading

wmt_stock_price_queue = []
wmt_stock_price_queue.insert(0, 131.10)
wmt_stock_price_queue.insert(0, 132.12)
wmt_stock_price_queue.insert(0, 135)

# print(wmt_stock_price_queue)

q = deque()

q.appendleft(5)
q.appendleft(8)
q.appendleft(27)

# print(q.pop())
# print(q.pop())
# print(q)

class Queue:
    
    def __init__(self):
        self.buffer = deque()

    def enqueue(self, val):
        self.buffer.appendleft(val)
    
    def dequeue(self):
        return self.buffer.pop()
    
    def is_empty(self):
        return len(self.buffer) == 0
    
    def size(self):
        return len(self.buffer)
    

pq = Queue()
pq.enqueue({
    'company': 'Wall Mart',
    'timestamp': '15 apr, 11.01 AM',
    'price': 131.10
})
pq.enqueue({
    'company': 'Wall Mart',
    'timestamp': '15 apr, 11.02 AM',
    'price': 132
})
pq.enqueue({
    'company': 'Wall Mart',
    'timestamp': '15 apr, 11.03 AM',
    'price': 135
})

# print(pq.buffer)
# print('The size is: ', pq.size())
# print(pq.dequeue())
# print(pq.buffer)
# print("The size is: ", pq.size())   


class exercise:
    def __init__(self):
        self.buffer = deque()
    
    def enqueue(self, val):
        self.buffer.appendleft(val)
    
    def  place_order(self, item):
        print("Placing order for: ", item)
        self.enqueue(item)
        time.sleep(0.5)
        # self.buffer.appendleft(item)
    
    def dequeue(self):
        if len(self.buffer) == 0:
            print("Queue is empty")
            return
        else:
            return self.buffer.pop()
    
    def serve_order(self):
        time.sleep(2)
        while True:
            order = self.dequeue()
            print("Now serving:", order)
            time.sleep(2)
        # return self.buffer.pop()
        
    
if __name__ == '__main__':
    orders = ['pizza', 'samosa', 'pasta', 'biryani', 'burger']
    e =  exercise()
    t1 = threading.Thread(target=e.place_order, args=(orders,))
    t2 = threading.Thread(target=e.serve_order)

    # e = exercise()
    # e.place_order('pizza')
    # e.place_order('samosa')
    # e.place_order('psata')
    # e.place_order('biryani')
    # e.place_order('burger')
    # print(e.buffer)
    # print(e.serve_order())
    # print(e.serve_order())
    # print(e.serve_order())
    # print(e.serve_order())
    # print(e.serve_order())
    t1.start()
    t2.start()