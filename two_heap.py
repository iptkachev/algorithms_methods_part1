from math import floor
import sys


class Heap:
    def __init__(self):
        self._tree = []

    def insert(self, x):
        self._tree.append(x)
        self._siftup()

    def _siftup(self):
        if not len(self._tree) == 1:
            index_added_element = len(self._tree) - 1
            added_element = self._tree[index_added_element]
            index_parent = floor((index_added_element + 1) / 2) - 1
            parent = self._tree[index_parent]
            while added_element > parent and index_parent >= 0:
                self._tree.insert(index_parent, added_element)
                self._tree.pop(index_parent + 1)
                self._tree.insert(index_added_element, parent)
                self._tree.pop(index_added_element + 1)

                # start new iteration
                index_added_element = index_parent
                index_parent = floor((index_added_element + 1) / 2) - 1
                parent = self._tree[index_parent]

    def extract_max(self):
        root = self._tree.pop(0)
        self._siftdown()
        return root

    def _siftdown(self):
        if self._tree:
            key_element = self._tree.pop()
            index_key_element = 0
            self._tree.insert(index_key_element, key_element)
            child_left_index, child_right_index = 2 * index_key_element + 1, 2 * index_key_element + 2
            child_left, child_right = self._get_node_from_tree(child_left_index), self._get_node_from_tree(child_right_index)

            while key_element < child_left or key_element < child_right:
                index_max_child, max_child = max([(child_left_index, child_left), (child_right_index, child_right)],
                                                 key=lambda x: x[1])
                self._tree.insert(index_key_element, max_child)
                key_element = self._tree.pop(index_key_element + 1)
                self._tree.insert(index_max_child, key_element)
                self._tree.pop(index_max_child + 1)
                index_key_element = index_max_child
                child_left_index, child_right_index = 2 * index_key_element + 1, 2 * index_key_element + 2
                child_left, child_right = self._get_node_from_tree(child_left_index), self._get_node_from_tree(child_right_index)

    def _get_node_from_tree(self, index: int):
        try:
            node = self._tree[index]
        except IndexError:
            node = -float('inf')
        return node


def pass_interface(heap: Heap, command: str):
    if command[:6] == 'Insert':
        method, number = command.split()
        heap.insert(int(number))
    elif command == 'ExtractMax':
        print(heap.extract_max())

    return heap


heapq = Heap()
# commands = int(sys.stdin.readline())
# for _ in range(commands):
#     heapq = pass_interface(heapq, sys.stdin.readline().strip())

# raise Exception
heapq = pass_interface(heapq, 'Insert 2')
heapq = pass_interface(heapq, 'Insert 3')
heapq = pass_interface(heapq, 'Insert 18')
heapq = pass_interface(heapq, 'Insert 15')
heapq = pass_interface(heapq, 'Insert 14')
heapq = pass_interface(heapq, 'Insert 12')
heapq = pass_interface(heapq, 'Insert 13')
heapq = pass_interface(heapq, 'Insert 12')
heapq = pass_interface(heapq, 'ExtractMax')
heapq = pass_interface(heapq, 'ExtractMax')
heapq = pass_interface(heapq, 'ExtractMax')
heapq = pass_interface(heapq, 'ExtractMax')
heapq = pass_interface(heapq, 'ExtractMax')
heapq = pass_interface(heapq, 'ExtractMax')
heapq = pass_interface(heapq, 'ExtractMax')
heapq = pass_interface(heapq, 'ExtractMax')
