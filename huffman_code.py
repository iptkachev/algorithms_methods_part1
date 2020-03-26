from collections import Counter
from heapq import nsmallest


class Node:
    def __init__(self, frequency, binary_value=None, string_char=None, parent=None, left_child=None, right_child=None):
        self.frequency = frequency
        self.binary_value = binary_value
        self.string_char = string_char
        self.parent = parent
        self.left_child = left_child
        self.right_child = right_child
        self.used = False

    def __repr__(self):
        return f"Node(binary_value={self.binary_value}, string_char={self.string_char})"


class HuffmanEncoder:
    def __init__(self, string: str):
        self.string = string
        self.unique_len = len(set(self.string))
        self.counter = None
        self.binary_codes = dict()
        self._tree = []

    def make_huffman_tree(self):
        self.counter = Counter(self.string)
        self._tree = [Node(frequency=freq, string_char=char) for char, freq in self.counter.items()]

        for i in range(self.unique_len - 1):
            left_child, right_child = self._get_two_min_nodes()
            parent = Node(left_child.frequency + right_child.frequency,
                          left_child=left_child, right_child=right_child)
            self._set_nodes_as_children(left_child, right_child, parent)
            self._tree.append(parent)

        self._build_binary_codes()

    def _get_two_min_nodes(self):
        return nsmallest(2, self._tree, key=lambda node: node.frequency if not node.used else float('inf'))

    def _set_nodes_as_children(self, left_child: Node, right_child: Node, parent: Node):
        left_child.binary_value = '0'
        left_child.used = True
        left_child.parent = parent
        right_child.binary_value = '1'
        right_child.used = True
        right_child.parent = parent

    def _build_binary_codes(self):
        if len(self._tree) == 1:
            self.binary_codes[self._tree[0].string_char] = '0'
            return None

        for char_leaf in self._tree[:self.unique_len]:
            self.binary_codes[char_leaf.string_char] = self._get_code_for_char_leaf(char_leaf)

    def _get_code_for_char_leaf(self, node: Node) -> str:
        binary_code = node.binary_value
        while node.parent.parent:
            node = node.parent
            binary_code += node.binary_value

        return binary_code[::-1]

    def encode_string(self, string: str) -> str:
        binary_code = ''
        for char in string:
            binary_code += self.binary_codes[char]

        return binary_code

    def decode_binary_code(self, binary_code: str) -> str:
        decoded_string = ''
        node = self._tree[-1]  # root
        index_position = 0
        while index_position != len(binary_code):
            if binary_code[index_position] == '0':
                node = node.left_child
            elif binary_code[index_position] == '1':
                node = node.right_child
            if node.string_char:
                decoded_string += node.string_char
                node = self._tree[-1]
            index_position += 1

        return decoded_string


class HuffmanDecoder(HuffmanEncoder):
    def __init__(self, binary_codes: dict):
        self.binary_codes = binary_codes
        self.unique_len = len(self.binary_codes)
        self._tree = []

    def recover_huffman_tree(self):
        self._tree.append(Node(None))  # add root
        for char, binary_code in self.binary_codes.items():
            self._insert_in_tree(char, binary_code)
        self._tree = self._tree[::-1]

    def _insert_in_tree(self, char: str, binary_code: str):
        node = self._tree[0]  # root
        for bit in binary_code:
            if bit == '0':
                if not node.left_child:
                    self._tree.append(Node(None, binary_value='0', parent=node))
                    node.left_child = self._tree[-1]
                node = node.left_child
            elif bit == '1':
                if not node.right_child:
                    self._tree.append(Node(None, binary_value='1', parent=node))
                    node.right_child = self._tree[-1]
                node = node.right_child
        self._tree[-1].string_char = char


if __name__ == '__main__':
    # I
    # test_str = 'abacabad'
    #
    # huff_encoder = HuffmanEncoder(test_str)
    # huff_encoder.make_huffman_tree()
    #
    # print(huff_encoder.binary_codes)
    # print(huff_encoder.encode_string(test_str))
    # print(huff_encoder.decode_binary_code('01001100100111'))

    # II
    # test_binary_codes = {'a': '0', 'b': '10', 'c': '110', 'd': '111'}
    # binary_code = '01001100100111'
    # huff_decoder = HuffmanDecoder(test_binary_codes)
    # huff_decoder.recover_huffman_tree()
    #
    # print(huff_decoder.binary_codes)
    # print(huff_decoder.decode_binary_code(binary_code))
    # print(huff_decoder.encode_string(test_str))


    # first exercise
    # string = input()
    # huff = HuffmanEncoder(string)
    # huff.make_huffman_tree()
    # encoded_string = huff.encode_string(string)
    # print(huff.unique_len, len(encoded_string))
    # for key, value in huff.binary_codes.items():
    #     print(f'{key}: {value}')
    # print(encoded_string)

    # second exercise
    unique_len, _ = input().split()
    test_binary_codes = dict()
    for i in range(int(unique_len)):
        key, val = input().split(': ')
        test_binary_codes[key] = val
    binary_code = input()

    huff = HuffmanDecoder(test_binary_codes)
    huff.recover_huffman_tree()
    encoded_string = huff.decode_binary_code(binary_code)
    print(encoded_string)

