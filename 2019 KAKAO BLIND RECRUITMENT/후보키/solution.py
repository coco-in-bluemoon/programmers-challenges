from itertools import combinations


def check_uniqueness(candidate, relation):
    unique_values = set()

    for row in relation:
        value = ''
        for field in candidate:
            value += row[field]

        if value in unique_values:
            return False
        unique_values.add(value)

    return True


def check_minimality(key, uniqueness_key):
    key = set(key)
    for item in uniqueness_key:
        item = set(item)
        if item.issubset(key) and not key.issubset(item):
            return False
    return True


def solution(relation):
    n_field = len(relation[0])
    uniqueness_key = set()
    for size in range(1, n_field + 1):
        for candidate in combinations(range(n_field), size):
            if check_uniqueness(candidate, relation):
                uniqueness_key.add(candidate)

    candidate_key = set()
    for key in uniqueness_key:
        if check_minimality(key, uniqueness_key):
            candidate_key.add(key)

    return len(candidate_key)


if __name__ == "__main__":
    relation = [
        ["100", "ryan", "music", "2"],
        ["200", "apeach", "math", "2"],
        ["300", "tube", "computer", "3"],
        ["400", "con", "computer", "4"],
        ["500", "muzi", "music", "3"],
        ["600", "apeach", "music", "2"]
    ]
    assert solution(relation) == 2
