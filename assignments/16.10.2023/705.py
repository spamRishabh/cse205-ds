class MyHashSet:
    def __init__(self):
        self.buckets = [set() for _ in range(1000)]

    def _hash(self, key):
        return key % len(self.buckets)

    def add(self, key):
        bucket_index = self._hash(key)
        self.buckets[bucket_index].add(key)

    def remove(self, key):
        bucket_index = self._hash(key)
        if key in self.buckets[bucket_index]:
            self.buckets[bucket_index].remove(key)

    def contains(self, key):
        bucket_index = self._hash(key)
        return key in self.buckets[bucket_index]


# Your MyHashSet object will be instantiated and called as such:
# obj = MyHashSet()
# obj.add(key)
# obj.remove(key)
# param_3 = obj.contains(key)