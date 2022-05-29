class dictionary_iter:
    def __init__(self, dict):
        self.dict = dict
        self.size = len(dict) - 1
        self.start = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self.start > self.size:
            raise StopIteration
        temp = self.start
        self.start += 1
        return list(self.dict.items())[temp]


result = dictionary_iter({1: "1", 2: "2"})
for x in result:
    print(x)