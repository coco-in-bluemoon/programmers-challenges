from collections import deque
import sys
sys.setrecursionlimit(10000)


class Node:
    def __init__(self, name, x, y):
        self.name = name
        self.coord = (x, y)
        self.left = None
        self.right = None

    def __str__(self):
        message = f'Node {self.name} @ {self.coord}'
        return message


class BinaryTree:
    def __init__(self):
        self.root = None

    def _traverse_preorder(self, node, visited):
        visited.append(node.name)
        if node.left:
            self._traverse_preorder(node.left, visited)
        if node.right:
            self._traverse_preorder(node.right, visited)

    def insert_node(self, name, x, y):
        node_new = Node(name, x, y)

        if not self.root:
            self.root = node_new
            return

        node = self.root
        while True:
            if node.coord[0] < node_new.coord[0]:
                if node.right:
                    node = node.right
                else:
                    node.right = node_new
                    break
            elif node.coord[0] > node_new.coord[0]:
                if node.left:
                    node = node.left
                else:
                    node.left = node_new
                    break

    def _traverse_postorder(self, node, visited):
        if node.left:
            self._traverse_postorder(node.left, visited)
        if node.right:
            self._traverse_postorder(node.right, visited)
        visited.append(node.name)

    def traverse_preorder(self):
        visited = list()
        self._traverse_preorder(self.root, visited)
        return visited

    def traverse_postorder(self):
        visited = list()
        self._traverse_postorder(self.root, visited)
        return visited

    def __str__(self):
        message = str()
        queue = deque([self.root])
        while queue:
            node = queue.popleft()
            if node:
                message += node.__str__()
                message += '\n'
            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)

        return message


def solution(nodeinfo):
    nodeinfo_with_name = list()
    tree = BinaryTree()
    for idx, (x, y) in enumerate(nodeinfo):
        nodeinfo_with_name.append([x, y, idx+1])
    nodeinfo_with_name =\
        sorted(nodeinfo_with_name, key=lambda x: (-x[1], x[0]))

    for x, y, name in nodeinfo_with_name:
        tree.insert_node(name, x, y)

    answer = list()
    answer.append(tree.traverse_preorder())
    answer.append(tree.traverse_postorder())
    return answer


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
