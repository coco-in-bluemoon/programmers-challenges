import heapq


def solution(food_times, k):
    heap_food = list()
    for idx, food_time in enumerate(food_times):
        heapq.heappush(heap_food, (food_time, idx+1))

    time = 0
    food_time_prev = 0
    while heap_food:
        number_of_food = len(heap_food)
        food_time, _ = heap_food[0]

        time_added = (number_of_food * (food_time - food_time_prev))

        if time + time_added > k:
            break

        heapq.heappop(heap_food)
        time += time_added
        food_time_prev = food_time

    if not heap_food:
        return -1

    foods = [food_id for _, food_id in heap_food]
    foods = sorted(foods)
    index = (k - time) % len(foods)
    return foods[index]


if __name__ == "__main__":
    food_times = [3, 1, 2]
    k = 5
    assert solution(food_times, k) == 1
