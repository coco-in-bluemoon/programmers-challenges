def transform_decimal_number_to_nary(number, n):
    DIGITS = '0123456789ABCDEF'
    nary = ''
    while number > 0:
        remain = number % n
        nary += DIGITS[remain]
        number //= n
    return nary[::-1] if nary else '0'


def solution(n, t, m, p):
    answer = str()
    number = 0
    turn = 1

    while len(answer) < t:
        number_in_nary = transform_decimal_number_to_nary(number, n)

        for digit in number_in_nary:
            if turn == p:
                answer += digit
            if len(answer) == t:
                break
            turn = (turn + 1 if turn < m else 1)

        number += 1
    return answer


if __name__ == "__main__":
    n, t, m, p = 2, 4, 2, 1
    assert solution(n, t, m, p) == '0111'

    n, t, m, p = 16, 16, 2, 1
    assert solution(n, t, m, p) == '02468ACE11111111'
