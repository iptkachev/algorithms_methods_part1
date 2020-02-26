from math import floor


class Node:
    def __init__(self, value: int):
        self.value = value

    def __repr__(self):
        return f"Node({self.value})"


class Heap:
    def __init__(self):
        self._tree = []

    def insert(self, x):
        new_node = Node(x)
        self._tree.append(new_node)
        self._recover_heap_after_insert()

    def _recover_heap_after_insert(self):
        if not len(self._tree) == 1:
            index_added_element = len(self._tree) - 1
            added_element = self._tree[index_added_element]
            index_parent = floor(index_added_element / 2)
            parent = self._tree[index_parent]
            while added_element.value > parent.value:
                self._tree.insert(index_parent, added_element)
                self._tree.pop(index_parent + 1)
                self._tree.insert(index_added_element, parent)
                self._tree.pop(index_added_element + 1)

                # start new iteration
                index_added_element = index_parent
                index_parent = floor(index_added_element / 2)
                parent = self._tree[index_parent]

    def extract_max(self):
        root = self._tree.pop(0)
        self._recover_heap_after_extracting()
        return root

    def _recover_heap_after_extracting(self):
        last_element = self._tree.pop()
        self._tree.insert(0, last_element)
        child_left_index, child_right_index = 1, 2
        child_left, child_right = self._tree[child_left_index], self._tree[child_right_index]

        while last_element.value < child_left.value or last_element.value < child_right.value:
            pass

heapq = Heap()
heapq.insert(20)
heapq.insert(30)
heapq.insert(5)
heapq.insert(10)
heapq.insert(11)
heapq.insert(50)
print(heapq._tree)