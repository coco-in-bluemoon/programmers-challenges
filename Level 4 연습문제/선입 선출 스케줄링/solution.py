import math


def solution(n, cores):
    minimum_time = 0
    maximum_time = math.ceil(n / len(cores)) * max(cores)

    while minimum_time <= maximum_time:
        target_time = (minimum_time + maximum_time) // 2
        workload = 0
        for core in cores:
            workload += math.ceil(target_time / core)

        if workload >= n:
            maximum_time = target_time - 1
        elif workload < n:
            minimum_time = target_time + 1

    target_time = maximum_time
    workload = 0
    for core in cores:
        workload += math.ceil(target_time / core)

    index = 0
    while index < len(cores) and workload < n:
        core = cores[index]
        if (not target_time) or (target_time and not target_time % core):
            workload += 1
        index += 1

    return index


if __name__ == "__main__":
    n = 6
    cores = [1, 2, 3]
    assert solution(n, cores) == 2

    n = 1
    cores = [1, 2, 3]
    assert solution(n, cores) == 1

    n = 2
    cores = [1, 2, 3]
    assert solution(n, cores) == 2

    n = 3
    cores = [1, 2, 3]
    assert solution(n, cores) == 3

    n = 4
    cores = [1, 2, 3]
    assert solution(n, cores) == 1