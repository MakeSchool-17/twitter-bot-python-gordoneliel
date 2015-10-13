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
        self.list.pop()  # Remove the last element from the list
        self.size -= 1
        self._percolate_down()

    def peek(self):
        pass

    def _percolate_up(self, child_index):
        # Compare the node with its parent, if it is greater, swap with parent
        # Continue until heap order is restored
        parent_index = (child_index - 1) // 2

        parent_node = self.list[parent_index]
        child_node = self.list[child_index]

        if parent_node < child_node:
            self._swap_nodes(parent_index, child_index)

        # Base case for recursion
        if parent_index <= 0:
            return
        else:
            self._percolate_up(parent_index)

    def _percolate_down(self, parent_index=0):
        # left child is 2k
        # right child is 2k + 1
        left_child_index = 2 * parent_index + 1
        right_child_index = left_child_index + 1
        if parent_index == 0:
            left_child_index = 1
            right_child_index = 2

        # Base Case
        if left_child_index >= self.size - 1 or right_child_index >= self.size - 1:
            return

        left_child = self.list[left_child_index]
        right_child = self.list[right_child_index]
        parent_node = self.list[parent_index]

        # print(parent_index, left_child_index, right_child_index)
        # print(parent_node, left_child, right_child)
        if parent_node < left_child:
            self._swap_nodes(parent_index, left_child_index)
            # print("Parent index < left_child " + str(left_child_index))
            self._percolate_down(left_child_index)
        else:
            self._swap_nodes(parent_index, right_child_index)
            # print("Parent index < right_child " + str(right_child_index))
            self._percolate_down(right_child_index)

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

        heap.delete_max()

        print(heap)

if __name__ == '__main__':
    MaxHeap.main()
