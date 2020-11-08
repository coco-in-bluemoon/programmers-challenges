from collections import deque


class Node:
    def __init__(self, label):
        self.label = label
        self.children = dict()
        self.counter = 0

    def __str__(self):
        node_str = f'{self.label}({self.counter}) '
        for child_node in self.children.values():
            node_str += (child_node.label + ' ')
        return node_str


class Trie:
    def __init__(self):
        self.root = Node(None)

    def insert_word(self, word):
        node = self.root
        for character in word:
            node.counter += 1
            if character not in node.children:
                node.children[character] = Node(character)
            node = node.children[character]
        node.counter += 1

    def get_prefix_of_word(self, word):
        FLAG_ONLY_WORD = 1
        node = self.root
        prefix = ''
        for character in word:
            prefix += character
            node = node.children[character]
            if node.counter == FLAG_ONLY_WORD:
                break
        return prefix

    def __str__(self):
        trie_str = ''
        queue = deque([self.root])
        while queue:
            item = queue.popleft()
            trie_str += item.__str__()
            trie_str += '\n'

            for child in item.children.values():
                queue.append(child)

        return trie_str


def solution(words):
    trie = Trie()
    for word in words:
        word = word.lower()
        trie.insert_word(word)

    answer = 0
    for word in words:
        word = word.lower()
        prefix = trie.get_prefix_of_word(word)
        answer += len(prefix)
    return answer


if __name__ == "__main__":
    words = ['go', 'gone', 'guild']
    assert solution(words) == 7
