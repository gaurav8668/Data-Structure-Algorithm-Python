class HashTable:

    def __init__(self):
        self.Max = 10
        self.arr = [[] for i in range(self.Max)]
    def get_hash(self, key):
        h = 0
        for char in keys:
            h += ord(char)
        return h % self.Max

    def __setitem__(self, key, val):
        h = self.get_hash(key)
        if h == []:
            self.arr[h].append((key, value))
        else:
            for idx, element in enumerate(self.arr[h]):
                if 