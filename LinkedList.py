''' Simple LinkedList implementation
    Methods - Find, delete, insert, size
'''


class ListNode:
    def __init__(self, key, value, next_node=None):
        self.key = key
        self.value = value
        self.next_node = next_node

    def get_key(self):
        return self.key

    def get_value(self):
        return self.value

    def get_next(self):
        return self.next_node

    def set_next(self, new_next):
        self.next_node = new_next

    def __str__(self):
        return str(self.key)

    def __eq__(self, other):
        print("Called q")
        return self.data == other

''' Linked list for hashtable '''


class LinkedList:
    def __init__(self, head=None):
        self.head = head

    def insert(self, key, value):
        new_node = ListNode(key, value)
        new_node.set_next(self.head)
        self.head = new_node

    def size(self):
        size = 0
        current_p = self.head
        while current_p is not None:
            size += 1
            current_p = current_p.get_next()
        return size

    def find(self, data):
        current_p = self.head
        while current_p is not None:
            if current_p.get_key() == data:
                return current_p.get_value()
            current_p = current_p.get_next()
        return None

    def __str__(self):
        result = ""
        current_p = self.head
        while current_p is not None:
            result += str(current_p.get_key()) + " -> " + str(current_p.get_value())
            current_p = current_p.get_next()
        return result

    def __len__(self):
        return self.size()

    def delete(self, data):
        current_p = self.head
        previous_p = current_p

        while current_p is not None:
            if current_p.get_key() == data:
                previous_p.set_next(current_p.get_next())
                break
            previous_p = current_p
            current_p = current_p.get_next()

    ''' Iterator '''

    def __iter__(self):
        while True and self.head.get_next() is not None:
            yield self.head
            self.head = self.head.get_next()

    def main():
        linked_list = LinkedList()
        for i in range(10):
            linked_list.insert(i, i + 1)

        linked_list.delete(5)
        print(len(linked_list))
        linked_list.delete(8)
        for elem in iter(linked_list):
            print("List value: " + str(elem))
        print("Find 7: " + str(linked_list.find(4)))
        # print(linked_list)
if __name__ == '__main__':
    LinkedList.main()
