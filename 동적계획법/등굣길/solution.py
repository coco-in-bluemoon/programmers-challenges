def solution(m, n, puddles):
    board = [[0] * (n+1) for _ in range(m+1)]

    # initialize
    for c in range(1, n+1):
        if [1, c] in puddles:
            break
        board[1][c] = 1

    for r in range(1, m+1):
        if [r, 1] in puddles:
            break
        board[r][1] = 1

    for r in range(2, m+1):
        for c in range(2, n+1):
            if [r, c] in puddles:
                continue
            board[r][c] = (board[r-1][c] + board[r][c-1]) % 1000000007

    return board[m][n]


if __name__ == "__main__":
    m, n = 4, 3
    puddles = [[2, 2]]
    assert solution(m, n, puddles) == 4

    m, n = 5, 4
    puddles = [[2, 1], [2, 2], [2, 3], [4, 2], [4, 3], [4, 4]]
    assert solution(m, n, puddles) == 0
