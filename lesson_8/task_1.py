from collections import Counter
from operator import attrgetter


class Node:
    def __init__(self, value, freq, left=None, right=None):
        self.right = right
        self.left = left
        self.freq = freq
        self.value = value
        self.coding = ""

    def __repr__(self):
        return f"Node {self.value}: {self.freq}"


LEFT = 0
RIGHT = 1
val_codes = dict()


def h_coding(data, code=""):
    value = code + str(data.coding)
    # print(value)
    # print(data)
    if data.left:
        # print(f"Left -> {data.left}, Node coding -> {data.left.coding}\n")
        h_coding(data.left, value)
    if data.right:
        # print(f"Right -> {data.right}, Node coding -> {data.right.coding}\n")
        h_coding(data.right, value)
    if not data.left and not data.right:
        val_codes[data.value] = value
        return


def h_output(string, data):
    res = ""
    for symbol in string:
        res += data[symbol] + " "
    return res


def huffman(data):
    data_for_huffman = dict(sorted(sorted(dict(Counter(data)).items(), key=lambda x: x[0], reverse=True),
                                     key=lambda x: x[1]))
    values = data_for_huffman.keys()
    nodes = []

    for value in values:
        nodes.append(Node(value, data_for_huffman.get(value)))

    while len(nodes) > 1:
        nodes = sorted(nodes, key=attrgetter("value"), reverse=True)
        nodes = sorted(nodes, key=attrgetter("freq"))
        left = nodes[LEFT]
        right = nodes[RIGHT]
        left.coding = LEFT
        right.coding = RIGHT

        new_node = Node(freq=left.freq + right.freq, left=left, right=right, value=left.value + right.value)
        nodes.remove(left)
        nodes.remove(right)
        nodes.append(new_node)

    h_coding(nodes[0])
    print(f"Input data: {data}")
    print(f"Output code: {h_output(data, val_codes)}")


user_string = "beep boop beer!"

huffman(user_string)
