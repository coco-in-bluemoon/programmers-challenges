from collections import defaultdict
import sys
sys.setrecursionlimit(10**9)


def dfs(u, graph, conditions, delayed, visited):
    if u in visited:
        return

    if u in conditions.keys() and conditions[u] not in visited:
        delayed[conditions[u]].add(u)
        return

    visited.add(u)

    for v in delayed[u]:
        dfs(v, graph, conditions, delayed, visited)
    delayed.pop(u)

    for v in graph[u]:
        dfs(v, graph, conditions, delayed, visited)


def solution(n, path, order):
    graph = defaultdict(set)
    for u, v in path:
        graph[u].add(v)
        graph[v].add(u)

    conditions = defaultdict(str)
    for prev, next in order:
        conditions[next] = prev

    visited = set()
    delayed = defaultdict(set)
    dfs(0, graph, conditions, delayed, visited)

    return len(visited) == n


if __name__ == "__main__":
    n = 9
    path = [[0, 1], [0, 3], [0, 7],
            [8, 1], [3, 6], [1, 2],
            [4, 7], [7, 5]]
    order = [[8, 5], [6, 7], [4, 1]]
    assert solution(n, path, order)

    n = 9
    path = [[8, 1], [0, 1], [1, 2],
            [0, 7], [4, 7], [0, 3],
            [7, 5], [3, 6]]
    order = [[4, 1], [5, 2]]
    assert solution(n, path, order)

    n = 9
    path = [[0, 1], [0, 3], [0, 7],
            [8, 1], [3, 6], [1, 2],
            [4, 7], [7, 5]]
    order = [[4, 1], [8, 7], [6, 5]]
    assert not solution(n, path, order)
