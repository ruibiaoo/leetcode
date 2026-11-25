class MyQueue:

    def __init__(self):
        self.stack1 = []
        self.stack2 = []
        
    def push(self, x: int) -> None:
        if len(self.stack1) == 0:
            self.stack1.append(x)
        else:
            while len(self.stack1) != 0:
                curr = self.stack1.pop(-1)
                self.stack2.append(curr)
            self.stack1.append(x)

            while len(self.stack2) != 0:
                curr = self.stack2.pop(-1)
                self.stack1.append(curr)

    def pop(self) -> int:
        return self.stack1.pop(-1)

    def peek(self) -> int:
        return self.stack1[-1]

    def empty(self) -> bool:
        return len(self.stack1) == 0
        


# Your MyQueue object will be instantiated and called as such:
# obj = MyQueue()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.peek()
# param_4 = obj.empty()