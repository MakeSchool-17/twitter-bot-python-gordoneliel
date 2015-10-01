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
        pass

    def peek(self):
        pass

    def _percolate_up(self, node):
        # Compare the node with its parent, if it is greater, swap with parent
        # Continue until heap order is restored
        parent_index = (node) // 2
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
        pass

    def _swap_nodes(self, parent, child):
        self.list[parent], self.list[child] = self.list[child], self.list[parent]

    def __str__(self):
        result = "{"
        for elem in self.list:
            result += str(elem) + ", "
        return result[: -2] + "}"

    def main():
        heap = MaxHeap()
        # for i in range(1, 6):
        #     heap.insert(i)
        # "1, 2, 3, 4, 5"
        # "[5, 4, 3, 1, 2]"
        heap.insert(5)
        heap.insert(2)
        heap.insert(8)
        heap.insert(9)
        heap.insert(1)

        print(heap)

if __name__ == '__main__':
    MaxHeap.main()
