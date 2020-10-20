from collections import defaultdict
from collections import deque


class Node:
    def __init__(self, name):
        self.name = name
        self.children = defaultdict()
        self.counter = 0

    def __str__(self):
        return f'{self.name}\t{self.children.keys()}\t{self.counter}'


class Trie:
    def __init__(self):
        self.root = Node('ROOT')

    def insert_word(self, word):
        node = self.root
        for name in word:
            if name not in node.children.keys():
                node.children[name] = Node(name)
            node.counter += 1
            node = node.children[name]
        node.counter += 1

    def search_query(self, query):
        node = self.root
        for name in query:
            if name == '?':
                break
            if name not in node.children.keys():
                return 0
            node = node.children[name]

        return node.counter

    def __str__(self):
        node = self.root
        queue = deque([node])
        message = ''
        while queue:
            node = queue.popleft()
            message += (str(node) + '\n')

            for child in node.children.values():
                queue.append(child)
        return message


def solution(words, queries):
    prefix_tries = defaultdict(lambda: Trie())
    suffix_tries = defaultdict(lambda: Trie())

    memo = defaultdict(int)
    for word in words:
        length = len(word)

        prefix_tries[length].insert_word(word)
        suffix_tries[length].insert_word(word[::-1])

        memo['?'*len(word)] += 1

    answer = list()
    for query in queries:
        if query in memo:
            answer.append(memo[query])
            continue

        length = len(query)
        trie = suffix_tries[length]\
            if query.startswith('?') else prefix_tries[length]
        query_orig = query
        query = query[::-1] if query.startswith('?') else query

        counter = trie.search_query(query)
        answer.append(counter)
        memo[query_orig] = counter
    return answer


if __name__ == "__main__":
    words = [
        'frodo', 'front', 'frost',
        'frozen', 'frame', 'kakao'
    ]
    queries = [
        'fro??', '????o', '?????',
        'fr???', 'fro???', 'pro?',
    ]

    assert solution(words, queries) == [3, 2, 5, 4, 1, 0]
