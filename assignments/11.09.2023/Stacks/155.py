class MinStack:

    def __init__(self):
        self.stack= []
        self.min= None
        

    def push(self, val: int) -> None:
        if len(self.stack)==0:
            self.stack.append(val)
            self.min = val
        else:
            if val>self.min:
                self.stack.append(val)
            else:
                self.stack.append(2*val-self.min)
                self.min = val
                

    def pop(self) -> None:

        x=self.stack.pop() 
        if x<self.min:
            self.min=2*self.min-x
        

    def top(self) -> int:
        temp = self.stack[-1]
        if temp>=self.min:
            return temp
        return self.min
        

    def getMin(self) -> int:
        return self.min
        


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()