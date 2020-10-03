def compress_string(s, size):
    prev, current = s[:size], ''
    compressed = ''
    counter = 1
    idx = size

    while idx < len(s):
        current = s[idx:idx+size] if idx+size < len(s) else s[idx:]

        if prev == current:
            counter += 1
        else:
            pattern = prev if counter == 1 else f'{counter}{prev}'
            compressed += pattern
            prev = current
            counter = 1

        idx += size

    if counter == 1:
        compressed += current
    else:
        compressed += f'{counter}{prev}'

    return compressed


def solution(s):
    answer = len(s)
    for size in range(1, len(s) // 2 + 1):
        compressed = compress_string(s, size)
        answer = min(answer, len(compressed))
    return answer


if __name__ == "__main__":
    s = 'aabbaccc'
    assert solution(s) == 7

    s = 'ababcdcdababcdcd'
    assert solution(s) == 9

    s = 'abcabcdede'
    assert solution(s) == 8

    s = 'abcabcabcabcdededededede'
    assert solution(s) == 14

    s = 'xababcdcdababcdcd'
    assert solution(s) == 17
