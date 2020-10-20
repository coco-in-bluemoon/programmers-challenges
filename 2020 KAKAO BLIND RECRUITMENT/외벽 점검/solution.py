from itertools import permutations


def get_weak_comgination(n, weak):
    combinations = list()
    for idx in range(len(weak)):
        combination = weak[idx:] + [w+n for w in weak[:idx]]
        combinations.append(combination)
    return combinations


def check_all_weaks(weak, dist):
    weak_index = 0
    dist_index = 0

    while weak_index < len(weak) and dist_index < len(dist):
        w = weak[weak_index]
        d = dist[dist_index]

        while weak_index + 1 < len(weak):
            if w + d >= weak[weak_index + 1]:
                weak_index += 1
            else:
                break

        weak_index += 1
        dist_index += 1

    return weak_index == len(weak)


def solution(n, weak, dist):
    weak_combinations = get_weak_comgination(n, weak)
    for num_dist in range(1, len(dist) + 1):
        for dist_combination in permutations(dist, num_dist):
            for weak_combination in weak_combinations:
                if check_all_weaks(weak_combination, dist_combination):
                    return num_dist

    return -1


if __name__ == "__main__":
    n = 12
    weak = [1, 5, 6, 10]
    dist = [1, 2, 3, 4]
    my_answer = solution(n, weak, dist)
    answer = 2
    assert my_answer == answer
