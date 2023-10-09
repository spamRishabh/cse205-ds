class MyCircularDeque:

    def __init__(self, k: int):
        self.capacity = k
        self.size = 0
        self.front = 0
        self.rear = k - 1
        self.circular_deque = [-1] * k

    def insertFront(self, value: int) -> bool:
        if not self.isFull():
            self.front = (self.front - 1) % self.capacity
            self.circular_deque[self.front] = value
            self.size += 1
            return True
        return False

    def insertLast(self, value: int) -> bool:
        if not self.isFull():
            self.rear = (self.rear + 1) % self.capacity
            self.circular_deque[self.rear] = value
            self.size += 1
            return True
        return False

    def deleteFront(self) -> bool:
        if not self.isEmpty():
            self.front = (self.front + 1) % self.capacity
            self.size -= 1
            return True
        return False

    def deleteLast(self) -> bool:
        if not self.isEmpty():
            self.rear = (self.rear - 1) % self.capacity
            self.size -= 1
            return True
        return False

    def getFront(self) -> int:
        if not self.isEmpty():
            return self.circular_deque[self.front]
        return -1

    def getRear(self) -> int:
        if not self.isEmpty():
            return self.circular_deque[self.rear]
        return -1

    def isEmpty(self) -> bool:
        return self.size == 0

    def isFull(self) -> bool:
        return self.size == self.capacity
        


# Your MyCircularDeque object will be instantiated and called as such:
# obj = MyCircularDeque(k)
# param_1 = obj.insertFront(value)
# param_2 = obj.insertLast(value)
# param_3 = obj.deleteFront()
# param_4 = obj.deleteLast()
# param_5 = obj.getFront()
# param_6 = obj.getRear()
# param_7 = obj.isEmpty()
# param_8 = obj.isFull()