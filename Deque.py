class Deque:
    def __init__(self, size):
        self.q = [0] * size
        self.front = -1
        self.rear = -1
        self.size = size

    def pushFront(self, x):
        if self.isFull():
            return False
        if self.isEmpty():
            self.front = 0
            self.rear = 0
        else:
            self.front = (self.front - 1) % self.size
        self.q[self.front] = x
        return True

    def pushRear(self, x):
        if self.isFull():
            return False
        if self.isEmpty():
            self.front = 0
        self.rear = (self.rear + 1) % self.size
        self.q[self.rear] = x
        return True

    def popFront(self):
        if self.isEmpty():
            return -1
        x = self.q[self.front]
        if self.front == self.rear:
            self.front = -1
            self.rear = -1
        else:
            self.front = (self.front + 1) % self.size
        return x

    def popRear(self):
        if self.isEmpty():
            return -1
        x = self.q[self.rear]
        if self.front == self.rear:
            self.front = -1
            self.rear = -1
        else:
            self.rear = (self.rear - 1) % self.size
        return x

    def getFront(self):
        if self.isEmpty():
            return -1
        return self.q[self.front]

    def getRear(self):
        if self.isEmpty():
            return -1
        return self.q[self.rear]

    def isEmpty(self):
        #return self.front == -1
        if self.front==-1:
            return True
        return False

    def isFull(self):
        #return (self.rear + 1) % self.size == self.front
        if (self.rear + 1) % self.size == self.front:
            return True
        return False
