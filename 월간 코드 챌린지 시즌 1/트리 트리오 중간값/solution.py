from collections import deque
import math
from math import dist


def bfs(start, distance, graph):
    queue = deque([(start, 0)])
    visited = set()
    while queue:
        node, dist = queue.popleft()
        distance[node] = dist
        visited.add(node)

        for children in graph[node]:
            if children in visited:
                continue
            queue.append((children, dist+1))


def solution(n, edges):
    graph = {node: set() for node in range(1, n+1)}

    for src, dst in edges:
        graph[src].add(dst)
        graph[dst].add(src)

    distance = {node: 0 for node in range(1, n+1)}
    start = 1
    bfs(start, distance, graph)
    for k, v in distance.items():
        if v > distance[start]:
            start = k

    bfs(start, distance, graph)
    max_distance = max(distance.values())
    counter = list(distance.values()).count(max_distance)
    if counter > 1:
        return max_distance

    for k, v in distance.items():
        if v == max_distance:
            start = k
            break
    bfs(start, distance, graph)
    max_distance = max(distance.values())
    counter = list(distance.values()).count(max_distance)
    if counter > 1:
        return max_distance

    return max_distance - 1


if __name__ == "__main__":
    n = 4
    edges = [[1, 2], [2, 3], [3, 4]]
    assert solution(n, edges) == 2

    n = 5
    edges = [[1, 5], [2, 5], [3, 5], [4, 5]]
    assert solution(n, edges) == 2

    n = 11
    edges = [
        [1, 2], [2, 3], [3, 4], [4, 5],
        [5, 6], [6, 7], [7, 8], [8, 9], [6, 10], [10, 11]
    ]
    assert solution(n, edges) == 7
