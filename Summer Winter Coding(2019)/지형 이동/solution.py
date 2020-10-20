from collections import defaultdict
from collections import deque
import math


def be_in_boundray(position, board):
    r, c = position
    n = len(board)

    return 0 <= r < n and 0 <= c < n


def separate_color(land, height, colormap):
    N = len(land)
    color = 1

    for base_r in range(N):
        for base_c in range(N):
            if colormap[base_r][base_c]:
                continue

            queue = deque([(base_r, base_c)])
            visited = set()
            while queue:
                r, c = queue.popleft()
                if (r, c) in visited:
                    continue
                visited.add((r, c))
                colormap[r][c] = color
                for dr, dc in zip([0, 0, 1, -1], [1, -1, 0, 0]):
                    if not be_in_boundray((r+dr, c+dc), colormap):
                        continue

                    if (r+dr, c+dc) in visited:
                        continue

                    source_height = land[r][c]
                    target_height = land[r+dr][c+dc]

                    if abs(target_height - source_height) > height:
                        continue

                    queue.append((r+dr, c+dc))
            color += 1


def get_cost_graph(land, colormap):
    N = len(colormap)
    graph = defaultdict(lambda: defaultdict(lambda: math.inf))

    for r in range(N):
        for c in range(N):
            for dr, dc in zip([0, 0, 1, -1], [1, -1, 0, 0]):
                if not be_in_boundray((r+dr, c+dc), colormap):
                    continue
                if colormap[r][c] == colormap[r+dr][c+dc]:
                    continue
                src = colormap[r][c]
                dst = colormap[r+dr][c+dc]

                src_height = land[r][c]
                dst_height = land[r+dr][c+dc]

                height = abs(src_height - dst_height)
                height = min(height, graph[src][dst], graph[dst][src])
                graph[src][dst] = height
                graph[dst][src] = height

    return graph


def get_parent(node, parent):
    while node != parent[node]:
        node = parent[node]
    return node


def do_kruskal_algorithm(graph):
    graph_info = set()
    for src, dst_info in graph.items():
        for dst, cost in dst_info.items():
            graph_info.add((cost, min(src, dst), max(src, dst)))

    graph_info = sorted(graph_info)

    answer = 0
    parents = {node: node for node in graph.keys()}
    visited = set()

    for cost, u, v in graph_info:
        u_parent = get_parent(u, parents)
        v_parent = get_parent(v, parents)

        if u_parent == v_parent:
            continue

        visited.add(u)
        visited.add(v)
        answer += cost

        u_parent, v_parent = min(u_parent, v_parent), max(u_parent, v_parent)
        parents[v_parent] = u_parent

        if parents.values() == [1] * len(parents):
            break

    return answer


def solution(land, height):
    N = len(land)
    colormap = [[0] * N for _ in range(N)]
    separate_color(land, height, colormap)
    graph = get_cost_graph(land, colormap)
    answer = do_kruskal_algorithm(graph)
    return answer


if __name__ == "__main__":
    land = [[1, 4, 8, 10], [5, 5, 5, 5], [10, 10, 10, 10], [10, 10, 10, 20]]
    height = 3
    assert solution(land, height) == 15

    land = [[10, 11, 10, 11], [2, 21, 20, 10], [1, 20, 21, 11], [2, 1, 2, 1]]
    height = 1
    assert solution(land, height) == 18
