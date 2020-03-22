from numbers import Number
from typing import Optional


class Node:
    def __init__(self, key: Number, value: Number):
        self.key = key
        self.value = value
        self.left_child = None
        self.right_child = None

    def __repr__(self) -> str:
        return f"Node({self.key, self.right_child})"


class BinarySearchTree:
    def __init__(self):
        self._root = None

    def push(self, key: Number, value: Number):
        if self._root:
            current_node = self._root
            while True:
                if current_node.key > key:
                    if current_node.left_child:
                        current_node = current_node.left_child
                    else:
                        new_node = Node(key, value)
                        current_node.left_child = new_node
                        break
                else:
                    if current_node.right_child:
                        current_node = current_node.right_child
                    else:
                        new_node = Node(key, value)
                        current_node.right_child = new_node
                        break
        else:
            self._root = Node(key, value)

    def search(self, key: Number) -> Optional[Number]:
        current_node = self._root
        while True:
            if current_node.key == key:
                return current_node.value
            elif current_node.key > key:
                if current_node.left_child:
                    current_node = current_node.left_child
                else:
                    return None
            else:
                if current_node.right_child:
                    current_node = current_node.right_child
                else:
                    return None

    def remove(self, key: Number):
        pass  # TODO
