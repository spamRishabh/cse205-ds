class MyQueue:

    def __init__(self):
        self.input_stack = []
        self.output_stack = []

    def push(self, x: int) -> None:
        self.input_stack.append(x)

    def pop(self) -> int:
        self.move_elements()
        if self.output_stack:
            return self.output_stack.pop()
        else:
            return -1  # Queue is empty

    def peek(self) -> int:
        self.move_elements()
        if self.output_stack:
            return self.output_stack[-1]
        else:
            return -1  # Queue is empty

    def empty(self) -> bool:
        return not self.input_stack and not self.output_stack

    def move_elements(self) -> None:
        if not self.output_stack:
            while self.input_stack:
                self.output_stack.append(self.input_stack.pop())
        


# Your MyQueue object will be instantiated and called as such:
# obj = MyQueue()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.peek()
# param_4 = obj.empty()