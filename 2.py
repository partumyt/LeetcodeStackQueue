from collections import deque

class MyStack(object):
    def __init__(self):
        self.q1 = deque()
        self.q2 = deque()

    def push(self, x):
        self.q2.append(x)
        while self.q1:
            self.q2.append(self.q1.popleft())
        self.q1, self.q2 = self.q2, self.q1

    def pop(self):
        if self.empty():
            raise IndexError
        return self.q1.popleft()

    def top(self):
        if self.empty():
            raise IndexError
        return self.q1[0]

    def empty(self):
        return len(self.q1) == 0
