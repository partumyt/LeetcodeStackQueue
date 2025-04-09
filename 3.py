from collections import Counter

class FreqStack(object):

    def __init__(self):
        self.stack = []

    def push(self, val):
        """
        :type val: int
        :rtype: None
        """
        self.stack.append(val)

    def pop(self):
        """
        :rtype: int
        """
        freq = Counter(self.stack)
        max_freq = max(freq.values())
        for i in range(len(self.stack) - 1, -1, -1):
            if freq[self.stack[i]] == max_freq:
                return self.stack.pop(i)
