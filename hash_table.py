''' A HashTable implementation using closed and double hashing '''
import timeit


class HashTable:
    def __init__(self):
        self.size = 15
        self.length = 0
        self.buckets = [None] * self.size
        self.LOAD_FACTOR_THRESHOLD = 0.6

    ''' set a key value pair in to the HashTable  or replace existing '''
    def set(self, key, value):
        load = self._load_factor()
        print("Load is: " + str(load))
        # Check load factor to determine whether to grow the table
        if load > self.LOAD_FACTOR_THRESHOLD:
            # Grow the hashtable
            print("Growing hash table")
            self._grow()
            print("Grown Size:" + str(self.size))

        self._set_internal(self.buckets, key, value)

    ''' Get a key value pair from the HashTable '''
    def get(self, key):
        tries = 1
        index = self._base_hash(key, self.size, tries)
        initial_index = index
        found = False

        if self.buckets[index] is None:
            return None
        elif self.buckets[index][0] == key:
            return self.buckets[index][1]
        else:
            while self.buckets[index] is not None and not found and initial_index != index:
                print("Get indices: " + str(index))
                if self.buckets[index][0] == key:
                    found = True
                else:
                    tries += 1
                    index = self._base_hash(key, self.size, tries)
            if found:
                return self.buckets[index][1]
            else:
                return None

    def contains(self, key):
        return True if self.get(key) is not None else False

    def _set_internal(self, bucket, key, value):
        tries = 1
        index = self._base_hash(key, self.size, tries)
        if bucket[index] is None:
            bucket[index] = (key, value)
            self.length += 1
        elif bucket[index][0] == key:
            bucket[index] = (key, value)
        else:
            while bucket[index] is not None and bucket[index][0] != key:
                print("Set indices: " + str(index))
                tries += 1
                index = self._base_hash(key, self.size, tries)

            if bucket[index] is None:
                self.length += 1

            bucket[index] = (key, value)

    ''' Grow buckets
        Double the size of the hashtable each time the load factor exceeds
        LOAD_FACTOR_THRESHOLD
    '''
    def _grow(self):
        new_size = (self.size * 2) + 1
        self.length = 0
        self.size = new_size
        new_buckets = [None] * new_size
        for key_value_pair in self.buckets:
            if key_value_pair is not None:
                key = key_value_pair[0]
                value = key_value_pair[1]
                self._set_internal(new_buckets, key, value)
        self.buckets = new_buckets

    ''' A hash function for hashing the key
        About double hashing: https://en.wikipedia.org/wiki/Double_hashing
    '''
    def _base_hash(self, key, size, tries):
        hashValue = hash(key)
        return (hashValue * tries ** 2 + tries) % size

    # ''' Second hash function for double hashing '''
    # def double_hash(self, key, size, tries):
    #     return (tries * self.base_hash(key, size)) % len(bucket)

    ''' Determines the load factor on the hash table
        Load factor = N / M
        Where:
        - N is number of filled buckets
        - M is size of the HashTable
    '''
    def _load_factor(self):
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
            for key_value_pair in self.buckets:
                if key_value_pair is not None:
                    result = result + str(key_value_pair[0]) + ' : ' + str(key_value_pair[1]) + ', '
            return result[:-2] + '}'

    def main():
        # value = int(inset("Enter a value"))
        table = HashTable()
        # table.set(1, 8)
        table.set("Bitonic", 5)
        table.set("Lambda", 90)
        table.set("Joey", 90)
        table.set("34", 78)
        table.set("Molly", 34)
        table.set("654", 18)
        table["4"] = 99

        print("Get Bitonic: " + str(table["Bitonic"]))
        print("Get Joey: " + str(table["Joey"]))
        print("Get Molly: " + str(table["Molly"]))

        print("Number of items: " + str(len(table)))
        table["Peter"] = 49
        table["Joseph"] = 3
        table["Noah"] = 92
        table["Hugh"] = 1
        print(table["Hugh"])
        table["Hugh"] += 2
        # for i in range(9):
        #     table[str(i)] = 9

        print("Number of items: " + str(table.length))
        print(table)
        getValue = input("Enter value to get \n")
        print(table.get(getValue))

if __name__ == '__main__':
    HashTable.main()
