''' A HashTable implementation using closed and double hashing '''


class HashTable:
    def __init__(self):
        self.size = 15
        self.length = 0
        self.buckets = [None] * self.size
        self.value = [None] * self.size
        self.LOAD_FACTOR_THRESHOLD = 0.6

    ''' set a key value pair in to the HashTable  or replace existing '''
    def set(self, key, value):

        load = self.load_factor()
        print("Load is: " + str(load))
        # Check load factor to determine whether to grow the table
        if load > self.LOAD_FACTOR_THRESHOLD:
            # Grow the hashtable
            self.grow()

        tries = 1

        bucket = self.base_hash(key, len(self.buckets), tries)
        print(key, value, bucket)
        if self.buckets[bucket] is None:
            self.buckets[bucket] = key
            self.value[bucket] = value
            self.length += 1
        else:
            if self.buckets[bucket] == key:
                self.value[bucket] = value
            else:
                tries += 1
                next_bucket = self.base_hash(key, len(self.buckets), tries)
                while self.buckets[next_bucket] is not None and self.buckets[next_bucket] != key:
                    tries += 1
                    next_bucket = self.base_hash(key, len(self.buckets), tries)
                if self.buckets[next_bucket] is None:
                    self.value[next_bucket] = value
                    self.buckets[next_bucket] = key
                    self.length += 1

    ''' Get a key value pair from the HashTable '''
    def get(self, key):
        tries = 1
        bucket = self.base_hash(key, len(self.buckets), tries)

        if self.buckets[bucket] is None:
            return None
        elif self.buckets[bucket] == key:
            return self.value[bucket]
        else:
            tries += 1
            bucket = self.base_hash(key, len(self.buckets), tries)

            while self.buckets[bucket] is not None and self.buckets[bucket] != key:
                tries += 1
                bucket = self.base_hash(key, len(self.buckets), tries)

        # next_bucket = 0
        #
        # found = False
        #
        # while self.buckets[initial_bucket] is not None and not found and next_bucket != initial_bucket:
        #     next_bucket = initial_bucket
        #     if self.buckets[next_bucket] == key:
        #         found = True
        #         return self.value[next_bucket]
        #     else:
        #         next_bucket = self.double_hash(key, len(self.buckets), initial_bucket)
        #
        # return self.value[initial_bucket] if found else None

    ''' A hash function for hashing the key
        About double hashing: https://en.wikipedia.org/wiki/Double_hashing
    '''
    def base_hash(self, key, size, tries):
        hashValue = hash(key)
        return (hashValue * tries ** 2 + tries) % size

    # ''' Second hash function for double hashing '''
    # def double_hash(self, key, size, tries):
    #     return (tries * self.base_hash(key, size)) % len(self.buckets)

    ''' Grow buckets
        Double the size of the hashtable each time the load factor exceeds
        LOAD_FACTOR_THRESHOLD
    '''
    def grow(self):
        new_bucket = [None] * (self.size * 2)

    ''' Determines the load factor on the hash table
        Load factor = N / M
        Where:
        - N is number of filled buckets
        - M is size of the HashTable
    '''
    def load_factor(self):
        return self.length / self.size

    ''' Setters and Getters '''
    def __setitem__(self, key, value):
            self.set(key, value)

    def __getitem__(self, key):
            return self.get(key)

    def __len__(self):
        return self.length

    def __str__(self):
            result = '{'
            for b, v in zip(self.buckets, self.value):
                if b is not None and v is not None:
                    result = result + str(b) + ' : ' + str(v) + ', '
            return result[:-2] + '}'

    def main():
        # value = int(inset("Enter a value"))
        table = HashTable()
        # table.set(1, 8)
        table.set("Bitonic", 5)
        table.set("Lambda", 90)
        table.set("Joey", 90)
        table.set("34", 78)
        table.set("Molly", 90)
        table.set("654", 18)
        table["4"] = 99
        # print(table.get("Bi"))
        print(table.value)
        print(table.buckets)
        print("Size of table: " + str(len(table)))
        print(table)
        getKey = input("Enter value to get")
        print(table.get(getKey))

if __name__ == '__main__':
    HashTable.main()
