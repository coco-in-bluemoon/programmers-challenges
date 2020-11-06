from collections import deque
import sys
sys.setrecursionlimit(10**5)


class Node:
    def __init__(self, x, y, label):
        self.coord = (x, y)
        self.label = label
        self.left = None
        self.right = None

    def __str__(self):
        left_child = self.left.label if self.left else None
        right_child = self.right.label if self.right else None
        return f'{self.label}  @{self.coord}\tL:{left_child}\tR:{right_child}'


class BinaryTree:
    def __init__(self):
        self.root = None

    def insert(self, x, y, label):
        new_node = Node(x, y, label)
        if not self.root:
            self.root = new_node
            return

        node = self.root
        while True:
            if node.coord[0] > new_node.coord[0]:
                if node.left:
                    node = node.left
                else:
                    node.left = new_node
                    break
            elif node.coord[0] < new_node.coord[0]:
                if node.right:
                    node = node.right
                else:
                    node.right = new_node
                    break

    def _traverse_preorder(self, node, visited):
        visited.append(node.label)
        if node.left:
            self._traverse_preorder(node.left, visited)
        if node.right:
            self._traverse_preorder(node.right, visited)

    def traverse_preorder(self):
        visited = list()
        self._traverse_preorder(self.root, visited)
        return visited

    def _traverse_postorder(self, node, visited):
        if node.left:
            self._traverse_postorder(node.left, visited)
        if node.right:
            self._traverse_postorder(node.right, visited)
        visited.append(node.label)

    def traverse_postorder(self):
        visited = list()
        self._traverse_postorder(self.root, visited)
        return visited

    def __str__(self):
        binary_tree_str = ''
        queue = deque([])
        if self.root:
            queue.append(self.root)
        while queue:
            node = queue.popleft()
            binary_tree_str += node.__str__()
            binary_tree_str += '\n'

            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)

        return binary_tree_str


def solution(nodeinfo):
    nodeinfo_with_label = list()
    for idx, (x, y) in enumerate(nodeinfo):
        label = idx + 1
        nodeinfo_with_label.append([x, y, label])
    nodeinfo_with_label = sorted(
        nodeinfo_with_label,
        key=lambda x: (-x[1], x[0])
    )

    tree = BinaryTree()
    for x, y, label in nodeinfo_with_label:
        tree.insert(x, y, label)

    visited_preorder = tree.traverse_preorder()
    visited_postorder = tree.traverse_postorder()

    return [visited_preorder, visited_postorder]


if __name__ == "__main__":
    nodeinfo = [
        [5, 3], [11, 5], [13, 3], [3, 5],
        [6, 1], [1, 3], [8, 6], [7, 2], [2, 2]
    ]
    answer = [
        [7, 4, 6, 9, 1, 8, 5, 2, 3],
        [9, 6, 5, 8, 1, 4, 3, 2, 7]
    ]
    assert solution(nodeinfo) == answer
