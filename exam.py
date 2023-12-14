class Node:
    def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None

def vertical_order_left_to_right(root, column, nodes):
    if root is None:
        return
    nodes.setdefault(column, []).append(root.key)

    vertical_order_left_to_right(root.left, column - 1, nodes)
    vertical_order_left_to_right(root.right, column + 1, nodes)

def vertical_order_right_to_left(root, column, nodes):
    if root is None:
        return
    nodes.setdefault(column, []).append(root.key)

    vertical_order_right_to_left(root.right, column - 1, nodes)
    vertical_order_right_to_left(root.left, column + 1, nodes)

def print_reverse_right_to_left(root):
    reversed_nodes = {}
    reversed_result = []
    distance = 0
    vertical_order_left_to_right(root, distance, reversed_nodes)

    print("Output:")
    for value in sorted(reversed_nodes, reverse=True):
        reversed_result.extend(reversed_nodes[value])

    print(str(reversed_result))

def print_result(root):
    print_reverse_right_to_left(root)

def main():
    root = Node(1)
    root.left = Node(2)
    root.right = Node(3)
    root.left.left = Node(4)
    root.left.right = Node(5)
    root.right.left = Node(6)
    root.right.right = Node(7)
    root.right.left.right = Node(8)
    root.right.right.right = Node(9)

    print_result(root)

main()
