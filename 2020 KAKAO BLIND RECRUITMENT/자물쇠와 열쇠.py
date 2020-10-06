def zero_pad_lock(lock, M, N):
    size = 2 * (M - 1) + N
    padded = [[0] * size for _ in range(size)]

    for r in range(N):
        for c in range(N):
            padded[r+M-1][c+M-1] = lock[r][c]

    return padded


def rotate_key(key):
    M = len(key)
    rotated = [[0] * M for _ in range(M)]

    for r in range(M):
        for c in range(M):
            rotated[c][M-r-1] = key[r][c]

    return rotated


def key_xor_lock(key, lock, row, col):
    for r in range(len(key)):
        for c in range(len(key)):
            lock[r+row][c+col] = lock[r+row][c+col] ^ key[r][c]


def sum_lock(lock, M, N):
    counter = 0
    for r in range(N):
        for c in range(N):
            counter += lock[r+M-1][c+M-1]
    return counter


def match(key, lock, M, N):
    size = M + N - 1

    unlocked = False
    for r in range(size):
        for c in range(size):
            key_xor_lock(key, lock, r, c)

            counter = sum_lock(lock, M, N)
            if counter == (N * N):
                key_xor_lock(key, lock, r, c)
                unlocked = True
                break

            key_xor_lock(key, lock, r, c)

    return unlocked


def solution(key, lock):
    M = len(key)
    N = len(lock)

    lock = zero_pad_lock(lock, M, N)

    matched = False

    for _ in range(4):
        key = rotate_key(key)

        matched = match(key, lock, M, N)
        if matched:
            break

    return matched


if __name__ == "__main__":
    key = [
        [0, 0, 0],
        [1, 0, 0],
        [0, 1, 1]
    ]
    lock = [
        [1, 1, 1],
        [1, 1, 0],
        [1, 0, 1]
    ]

    assert solution(key, lock)
