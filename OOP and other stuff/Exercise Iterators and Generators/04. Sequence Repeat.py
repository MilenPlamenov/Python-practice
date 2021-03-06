class sequence_repeat:
    def __init__(self, sequence, number):
        self.sequence = sequence
        self.number = number
        self.end = number
        self.index = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self.end == 0:
            raise StopIteration
        idx = self.index
        self.index += 1
        if self.index == len(self.sequence):
            self.index = 0
        self.end -= 1
        return self.sequence[idx]


result = sequence_repeat('abc', 5)
for item in result:
    print(item, end ='')