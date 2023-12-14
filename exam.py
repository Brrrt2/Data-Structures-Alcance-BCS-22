class Node:
    def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None

def traverse_left_to_right(root, column, nodes_dict):
    if root is None:
        return

    try:
        nodes_dict[column].append(root.key)
    except KeyError:
        nodes_dict[column] = [root.key]

    traverse_left_to_right(root.left, column - 1, nodes_dict)
    traverse_left_to_right(root.right, column + 1, nodes_dict)

def traverse_right_to_left(root, column, nodes_dict):
    if root is None:
        return

    try:
        nodes_dict[column].append(root.key)
    except KeyError:
        nodes_dict[column] = [root.key]

    traverse_right_to_left(root.right, column - 1, nodes_dict)
    traverse_right_to_left(root.left, column + 1, nodes_dict)

def print_reverse_right_to_left(root):
    nodes_dict = {}
    reversed_result = []
    distance = 0
    traverse_left_to_right(root, distance, nodes_dict)

    for index, value in enumerate(sorted(nodes_dict)):
        for i in nodes_dict[value]:
            reversed_result.append(i)

    print(str(reversed_result[::-1]))

def print_tree_result(root):
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

    print_tree_result(root)

main()
