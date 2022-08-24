class Queue:
    def __init__(self, n):
        self.size = n
        self.datas = [None] * n
        self.front = 0
        self.rear = -1

    def enQueue(self, data):
        if self.isFull():
            print('Queue is Full')
        else:
            self.rear += 1
            self.datas[self.rear] = data

    def deQueue(self):
        if self.isEmpty():
            print('Queue is Empty')
        else:
            result = self.datas[self.front]
            self.datas = self.datas[1:] + [None]
            self.rear -= 1
            return result

    def isEmpty(self):
        return self.rear < 0

    def isFull(self):
        return self.rear == self.size - 1

    def Qpeek(self):
        return self.datas[self.front]


queue = Queue(3)
queue.enQueue(1)
queue.enQueue(2)
queue.enQueue(3)

print(queue.deQueue())
print(queue.deQueue())
print(queue.deQueue())
