class MyStack:

    def __init__(self):
        self.queue = []

    def push(self, x: int) -> None:
        if len(self.queue) == 0:
            self.queue.append(x)
        else:
            curr = len(self.queue)
            self.queue.append(x)
            counter = 0
            while counter < curr:
                item = self.queue.pop(0)
                self.queue.append(item)
                counter += 1

    def pop(self) -> int:
        return self.queue.pop(0)
        
    def top(self) -> int:
        return self.queue[0]

    def empty(self) -> bool:
        return len(self.queue) == 0


        

# Your MyStack object will be instantiated and called as such:
# obj = MyStack()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.top()
# param_4 = obj.empty()