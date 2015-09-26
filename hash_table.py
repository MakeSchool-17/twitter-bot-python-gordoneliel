''' A HashTable implementation using closed and double hashing '''


class HashTable:
    def __init__(self):
        self.size = 11
        self.buckets = [None] * self.size
        self.value = [None] * self.size

    ''' set a key value pair in to the HashTable  or replace existing '''
    def set(self, key, value):
        key_str = hash(key)
        print(key_str)
        bucket = self.hash(key_str, len(self.buckets))

        if self.buckets[bucket] is None:
            self.buckets[bucket] = key
            self.value[bucket] = value
        else:
            if self.buckets[bucket] == key:
                self.value[bucket] = value
            else:
                next_bucket = double_hash(key_str, len(self.buckets), bucket)
                while self.buckets[next_bucket] is not None and self.buckets[next_bucket] is not key:
                    next_bucket = double_hash(key_str, len(self.buckets),
                    next_bucket)

                    if self.buckets[next_bucket] is not None:
                        self.buckets[next_bucket] = key
                        self.value[next_bucket] = value
                    else:
                        self.value[next_bucket] = value

    ''' Get a key value pair from the HashTable '''
    def get(self, key):
        key_str = hash(key)
        initial_bucket = self.hash(key_str, len(self.buckets))
        next_bucket = 0

        found = False

        while self.buckets[initial_bucket] is not None and not found and next_bucket != initial_bucket:
            next_bucket = initial_bucket
            if self.buckets[next_bucket] == key:
                found = True
                return self.value[next_bucket]
            else:
                next_bucket = double_hash(key_str, len(self.buckets), initial_bucket)

        return self.value[initial_bucket] if found else None

    ''' A hash function for hashing the key '''
    def hash(self, key, size):
        return key % size

    ''' Second hash function for double hashing '''
    def double_hash(self, key, size, old_bucket):
        return old_bucket * hash(self, key, size)

    ''' Setters and Getters '''
    def __setitem__(self, key, value):
            self.set(key, value)

    def __getitem__(self, key):
            return self.get(key)

    def __len__(self):
        return self.size

    def __str__(self):
            result = '{'
            for b, v in zip(self.buckets, self.value):
                if b is not None and v is not None:
                    result = result + str(b) + ':' + str(v) + ','
            return result[:-1] + '}'

    def main():
        # value = int(inset("Enter a value"))
        table = HashTable()
        # table.set(1, 8)
        table.set("Bitonic", 5)
        table.set("Lambda", 90)
        # table.set(1, "one")
        # table.set(4, "joe")
        # table.set(3, "peter")
        # table[3] = "Nancy"
        # table[11] = "Fiona"
        print(table.value)
        print(table.buckets)
        print(len(table))
        print(table)
        print(table.get("Lambda"))

if __name__ == '__main__':
    HashTable.main()
