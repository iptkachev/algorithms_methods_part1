from math import floor


class Node:
    def __init__(self, value: float):
        self.value = value

    def __repr__(self):
        return f"Node({self.value})"


class Heap:
    def __init__(self):
        self._tree = []

    def insert(self, x):
        new_node = Node(x)
        self._tree.append(new_node)
        self._siftup()

    def _siftup(self):
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
        self._siftdown()
        return root

    def _siftdown(self):
        if self._tree:
            key_element = self._tree.pop()
            index_key_element = 0
            self._tree.insert(index_key_element, key_element)
            child_left_index, child_right_index = 1, 2
            child_left, child_right = self._get_node_from_tree(child_left_index), self._get_node_from_tree(child_right_index)

            while key_element.value < child_left.value or key_element.value < child_right.value:
                index_max_child, max_child = max([(child_left_index, child_left), (child_right_index, child_right)],
                                                 key=lambda x: x[1].value)
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
            node = Node(-float('inf'))
        return node


def pass_interface(heap: Heap, command: str):
    if command[:6] == 'Insert':
        method, number = command.split()
        heap.insert(int(number))
    elif command == 'ExtractMax':
        print(heap.extract_max().value)

    return heap


heapq = Heap()
# commands = int(input())
# for _ in range(commands):
#     heapq = pass_interface(heapq, input())

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
heapq = pass_interface(heapq, 'ExtractMax')
543
944
930
246
364
746
797
692
669
526
668
344
341
368
968
904
324
660
465
860
831
304
985
997
860
740
350
983
948
921
911
786
782
633
763
967
588
536
459
281
277
255
766
772
168
157