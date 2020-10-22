def calculate_beauty(start, end, s, ldi, rdi):
    if s[start] != s[end]:
        return end - start

    if start > ldi[end] or end < rdi[start]:
        return 0

    return max(ldi[end] - start, end - rdi[start])


def solution(s):
    n = len(s)
    ldi = [0] * n
    rdi = [0] * n

    for idx in range(n):
        ldx = idx - 1
        rdx = idx + 1

        if idx and s[idx-1] == s[idx]:
            ldx = ldi[idx-1]
            rdx = rdi[idx-1]

        while ldx >= 0 and s[ldx] == s[idx]:
            ldx -= 1
        while rdx < n and s[rdx] == s[idx]:
            rdx += 1

        ldi[idx] = ldx
        rdi[idx] = rdx

    answer = 0
    for idx in range(n):
        for jdx in range(idx+1, n):
            answer += calculate_beauty(idx, jdx, s, ldi, rdi)

    return answer


if __name__ == "__main__":
    assert solution('baby') == 9
    assert solution('oo') == 0
