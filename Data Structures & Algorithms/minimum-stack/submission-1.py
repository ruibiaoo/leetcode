class MinStack:

    def __init__(self):
        self.stack = []
        self.minimum = []
        
    def push(self, val: int) -> None:
        if len(self.stack) == 0:
            self.stack.append(val)
            self.minimum.append(val)
        else:
            self.stack.append(val)
            if len(self.minimum) > 0:
                curr = self.minimum[-1]
                if val <= curr:
                    self.minimum.append(val)

    def pop(self) -> None:
        if self.stack[-1] == self.minimum[-1]:
            self.minimum.pop(-1)
        self.stack.pop(-1)

    def top(self) -> int:
        return self.stack[-1]
        
    def getMin(self) -> int:
        if len(self.minimum) > 0:
            return self.minimum[-1]