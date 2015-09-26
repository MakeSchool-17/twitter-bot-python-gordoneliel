''' A HashTable implementation using closed and double hashing '''


class HashTable:
    def __init__(self):
        self.size = 11
        self.buckets = [None] * self.size
        self.value = [None] * self.size

    ''' Put a new key value pair in to the HashTable '''
    def put(self, key, value):
        bucket = self.hash(key, len(self.buckets))

        if self.buckets[bucket] is None:
            self.buckets[bucket] = key
            self.value[bucket] = value
        else:
            if self.buckets[bucket] == key:
                self.value[bucket] = value
            else:
                next_bucket = double_hash(key, len(self.buckets), bucket)
                while self.buckets[next_bucket] is not None and self.buckets[next_bucket] is not key:
                    next_bucket = double_hash(key, len(self.buckets),
                    next_bucket)

                    if self.buckets[next_bucket] is not None:
                        self.buckets[next_bucket] = key
                        self.value[next_bucket] = value
                    else:
                        self.value[next_bucket] = value

    ''' Get a key value pair from the HashTable '''
    def get(self, key, value):
        bucket = hash(key, len(self.buckets))

        if self.buckets[bucket] is None:
            bucket = double_hash(key, len(self.buckets), bucket)

        return self.buckets[key]

    def hash(self, key, size):
        return key % size

    def double_hash(self, key, size, old_bucket):
        return old_bucket * hash(self, key, size)

    def __setitem__(self, key, value):
            self.put(key, value)

    def __getitem__(self, key):
            return self.get(key)

    def __len__(self):
        return self.size

    def __str__(self):
            result = '{'
            for b in self.buckets:
                for e in b:
                    result = result + str(e) + ':' + str(e) + ','
            return result[:-1] + '}'

    def main():
        table = HashTable()
        table.put(1, 8)
        table.put(1, "one")
        table.put(4, "joe")
        table.put(3, "peter")
        table[3] = "Nancy"
        table[11] = "Fiona"
        print(table.value)
        print(table.buckets)
        print(len(table))
        print(table)

if __name__ == '__main__':
    HashTable.main()
