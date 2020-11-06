import heapq


def solution(food_times, k):
    heap_food = list()
    for idx, food_time in enumerate(food_times):
        food_id = idx + 1
        heapq.heappush(heap_food, (food_time, food_id))

    time_elapsed = 0
    food_time_prev = 0
    while heap_food:
        food_time, _ = heap_food[0]
        n_food = len(heap_food)

        time_added = (food_time - food_time_prev) * n_food

        if time_elapsed + time_added > k:
            break

        heapq.heappop(heap_food)
        time_elapsed += time_added
        food_time_prev = food_time

    if not heap_food:
        return -1

    time_left = k - time_elapsed
    foods = [food_id for _, food_id in heap_food]
    foods = sorted(foods)
    index = time_left % len(foods)

    return foods[index]


if __name__ == "__main__":
    food_times = [3, 1, 2]
    k = 5
    assert solution(food_times, k) == 1
