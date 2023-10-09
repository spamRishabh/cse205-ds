from collections import deque

class MyStack:
    def __init__(self):
        self.main_queue = deque()
        self.temp_queue = deque()

    def push(self, x: int) -> None:
        # Push elements from the main_queue to the temp_queue
        while self.main_queue:
            self.temp_queue.append(self.main_queue.popleft())
        # Add the new element to the main_queue
        self.main_queue.append(x)
        # Push elements back from the temp_queue to the main_queue
        while self.temp_queue:
            self.main_queue.append(self.temp_queue.popleft())

    def pop(self) -> int:
        if self.main_queue:
            return self.main_queue.popleft()
        else:
            return -1  # Stack is empty

    def top(self) -> int:
        if self.main_queue:
            return self.main_queue[0]
        else:
            return -1  # Stack is empty

    def empty(self) -> bool:
        return not bool(self.main_queue)


# Your MyStack object will be instantiated and called as such:
# obj = MyStack()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.top()
# param_4 = obj.empty()