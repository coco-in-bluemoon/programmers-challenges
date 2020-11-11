from collections import defaultdict
import heapq
import math


def solution(N, road, K):
    # consturct graph
    graph = {n: defaultdict(lambda: math.inf) for n in range(1, N+1)}
    for src, dst, cost in road:
        graph[src][dst] = min(graph[src][dst], cost)
        graph[dst][src] = min(graph[dst][src], cost)

    # initialize minimum cost from node 1
    distances = {n: math.inf for n in range(1, N+1)}
    distances[1] = 0

    heap_dist = [(cost, node) for node, cost in distances.items()]
    heapq.heapify(heap_dist)
    visited = set()

    while heap_dist:
        cost, node = heapq.heappop(heap_dist)
        visited.add(node)
        for connected_node in graph[node]:
            distances[connected_node] = min(
                distances[connected_node],
                cost + graph[node][connected_node]
            )

        heap_dist = list()
        for node, cost in distances.items():
            if node in visited:
                continue
            heap_dist.append((cost, node))
        heapq.heapify(heap_dist)

    counter = 0
    for dist in distances.values():
        if dist <= K:
            counter += 1

    return counter


if __name__ == "__main__":
    N = 6
    road = [
        [1, 2, 1], [1, 3, 2], [2, 3, 2],
        [3, 4, 3], [3, 5, 2], [3, 5, 3], [5, 6, 1]
    ]
    K = 4
    assert solution(N, road, K) == 4

    N = 5
    road = [[1, 2, 1], [2, 3, 3], [5, 2, 2], [1, 4, 2], [5, 3, 1], [5, 4, 2]]
    K = 3
    assert solution(N, road, K) == 4
