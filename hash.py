def get_hash(key):
    h = 0
    for char in key:
        h += ord(char)
    return h % 100

# print(ord('m'))
# a = get_hash('march 6')
# print(a)

class HashTable:
    def __init__(self):
        self.MAX = 100
        self.arr = [None for i in range(self.MAX)]
    
    def get_hash(self, key):
        h = 0
        for char in key:
            h += ord(char)
        return h % self.MAX 
    
    def __setitem__(self, key, value):
        h = self.get_hash(key)
        self.arr[h] = value
    
    def __getitem__(self, key):
        h = self.get_hash(key)
        return self.arr[h]
    
    def __delitem__(self, key):
        h = self.get_hash(key)
        self.arr[h] = None


t = HashTable()
# t.add('march 6', 120)
# x = t.get('march 6', 120)
# print(x)
t['march 6'] = 130
t['march 1'] = 20
t['dec 17'] = 20

print(t.arr)

del t['march 6'] 
print(t.arr)