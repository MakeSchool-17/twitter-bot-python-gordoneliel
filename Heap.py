''' Heap '''


class MaxHeap:
    def __init__(self):
        self.list = []
        self.size = 0

    def insert(self, node):
        # Insert node in the next available slot
        self.list.append(node)
        self.size += 1
        self._percolate_up(self.size - 1)

    def delete_max(self):
        # Replace the first item which is max with the furthes elem in array
        self.list[0] = self.list[self.size - 1]
        self.size -= 1
        self.list.pop()  # Remove the last element from the list
        self._percolate_down()

    def peek(self):
        pass

    def _percolate_up(self, node):
        # Compare the node with its parent, if it is greater, swap with parent
        # Continue until heap order is restored
        parent_index = (node - 1) // 2
        print(node, parent_index)

        parent_node = self.list[parent_index]
        child_node = self.list[node]

        print("parent_node: " + str(parent_node) + " child_node: " + str(child_node))
        if parent_node < child_node:
            self._swap_nodes(parent_index, node)

        # Base case for recursion
        if parent_index <= 0:
            return
        else:
            self._percolate_up(parent_index)

    def _percolate_down(self, node):
        # left child is 2k
        # right child is 2k + 1

        parent_index = (node - 1) // 2

        parent_node = self.list[parent_index]
        child_node = self.list[node]



    def _swap_nodes(self, parent, child):
        self.list[parent], self.list[child] = self.list[child], self.list[parent]

    def __str__(self):
        result = "{"
        for elem in self.list:
            result += str(elem) + ", "
        return result[: -2] + "}"

    def main():
        heap = MaxHeap()

        # heap.insert(11)
        # heap.insert(5)
        # heap.insert(2)
        # heap.insert(8)
        # heap.insert(9)
        # heap.insert(1)
        # heap.insert(12)
        # heap.insert(16)
        # heap.insert(0)
        # heap.insert(22)
        # heap.delete_max()
        heap.insert(18)
        heap.insert(5)
        heap.insert(21)
        heap.insert(9)
        heap.insert(11)
        heap.insert(27)
        heap.insert(14)
        heap.insert(33)
        heap.insert(19)
        heap.insert(17)

        print(heap)

if __name__ == '__main__':
    MaxHeap.main()
