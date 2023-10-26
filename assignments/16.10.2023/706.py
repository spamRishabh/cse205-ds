class MyHashMap:
    def __init__(self):
        self.hash_map = [None] * 1001

    def _hash(self, key):
        return key % 1001

    def put(self, key, value):
        index = self._hash(key)
        
        if self.hash_map[index] is None:
            self.hash_map[index] = []
        

        for i, (k, v) in enumerate(self.hash_map[index]):
            if k == key:
                self.hash_map[index][i] = (key, value)
                return
    
        self.hash_map[index].append((key, value))

    def get(self, key):

        index = self._hash(key)
        
        if self.hash_map[index] is None:
            return -1
        
        for k, v in self.hash_map[index]:
            if k == key:
                return v
        return -1

    def remove(self, key):
        index = self._hash(key)
        
        if self.hash_map[index] is None:
            return
        
        for i, (k, v) in enumerate(self.hash_map[index]):
            if k == key:
                del self.hash_map[index][i]
                return