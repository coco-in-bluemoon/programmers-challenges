def solution(sticker):
    sticker_size = len(sticker)
    if sticker_size <= 2:
        return max(sticker)

    dp_from_first = [0] * (sticker_size - 1)
    dp_from_first[0] = sticker[0]
    dp_from_first[1] = max(dp_from_first[0], sticker[1])

    for idx in range(2, sticker_size - 1):
        dp_from_first[idx] =\
            max(dp_from_first[idx-1], dp_from_first[idx-2] + sticker[idx])

    dp_from_last = [0] * (sticker_size - 1)
    dp_from_last[0] = sticker[-1]
    dp_from_last[1] = max(dp_from_last[0], sticker[0])

    for idx in range(2, sticker_size - 1):
        dp_from_last[idx] =\
            max(dp_from_last[idx-1], dp_from_last[idx-2] + sticker[idx-1])

    return max(max(dp_from_first), max(dp_from_last))


if __name__ == "__main__":
    sticker = [14, 6, 5, 11, 3, 9, 2, 10]
    assert solution(sticker) == 36

    sticker = [1, 3, 2, 5, 4]
    assert solution(sticker) == 8
