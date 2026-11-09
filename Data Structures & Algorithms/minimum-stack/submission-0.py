class MinStack:

    def __init__(self):
        self.stack = []
        self.minimum = []

    def push(self, val: int) -> None:
        self.stack.append(val)
        if len(self.minimum) == 0 or self.minimum[-1] >= val:
            self.minimum.append(val)
    
    def pop(self) -> None:
        val = self.stack.pop()
        if val == self.minimum[-1]:
            self.minimum.pop()
        

    def top(self) -> int:
        return self.stack[-1]
        

    def getMin(self) -> int:
        return self.minimum[-1]
        



[1, 2, 0]