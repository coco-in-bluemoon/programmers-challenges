import heapq
import math


def solution(a):
    N = len(a)
    heap = list()
    for idx, num in enumerate(a):
        heapq.heappush(heap, (num, idx))

    left_min = math.inf
    right_min, _ = heapq.heappop(heap)
    answer = 0

    for idx in range(N):
        target = a[idx]

        if target == right_min:
            right_index = idx
            while heap and right_index <= idx:
                right_min, right_index = heapq.heappop(heap)
            if right_index <= idx:
                right_min = math.inf

        if target != max(target, left_min, right_min):
            answer += 1

        if left_min > target:
            left_min = target

    return answer


if __name__ == "__main__":
    a = [9, -1, -5]
    assert solution(a) == 3

    a = [-16, 27, 65, -2, 58, -92, -71, -68, -61, -33]
    assert solution(a) == 6
