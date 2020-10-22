def transform_and_reverse_to_nary(n, digit):
    num = n
    nary = ''
    while num:
        q, r = num // digit, num % digit
        nary += str(r)
        num = q

    return int(nary)


def caluclate_to_base_ten(n, digit):
    n = str(n)[::-1]
    answer = 0
    for idx, num in enumerate(n):
        answer += ((digit ** idx) * int(num))
    return answer


def solution(n):
    reversed_nary = transform_and_reverse_to_nary(n, 3)
    base_ten = caluclate_to_base_ten(reversed_nary, 3)
    return base_ten


if __name__ == "__main__":
    assert solution(45) == 7
    assert solution(125) == 229
