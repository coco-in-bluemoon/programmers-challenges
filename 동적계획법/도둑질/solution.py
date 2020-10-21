def solution(money):
    N = len(money)

    dp_first = [0] * (N-1)
    dp_first[0] = money[0]
    dp_first[1] = max(money[0], money[1])
    for idx in range(2, N-1):
        dp_first[idx] =\
            max(dp_first[idx-1], dp_first[idx-2] + money[idx])

    dp_last = [0] * (N-1)
    dp_last[0] = money[-1]
    dp_last[1] = max(money[-1], money[0])
    for idx in range(2, N-1):
        dp_last[idx] = \
            max(dp_last[idx-1], dp_last[idx-2] + money[idx-1])

    return max(dp_first[-1], dp_last[-1])


if __name__ == "__main__":
    money = [1, 2, 3, 1]
    assert solution(money) == 4
