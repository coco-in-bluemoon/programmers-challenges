from itertools import combinations


def solution(numbers):
    answer = set()
    for a, b in combinations(numbers, 2):
        answer.add(a+b)

    return list(sorted(answer))


if __name__ == "__main__":
    numbers = [2, 1, 3, 4, 1]
    answer = [2, 3, 4, 5, 6, 7]
    my_answer = solution(numbers)
    assert my_answer == answer
