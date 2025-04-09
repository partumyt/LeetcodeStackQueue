from collections import Counter

class FreqStack(object):

    def __init__(self):
        self.freq = {}
        self.group = {}
        self.maxfreq = 0

    def push(self, val):
        """
        :type val: int
        :rtype: None
        """
        if val in self.freq:
            self.freq[val] += 1
        else:
            self.freq[val] = 1
        f = self.freq[val]
        if f > self.maxfreq:
            self.maxfreq = f
        if f not in self.group:
            self.group[f] = []
        self.group[f].append(val)

    def pop(self):
        """
        :rtype: int
        """
        val = self.group[self.maxfreq].pop()
        self.freq[val] -= 1
        if not self.group[self.maxfreq]:
            self.maxfreq -= 1
        return val
