def solution(matrix_size):
    N = len(matrix_size)
    dp = [[0] * N for _ in range(N)]

    for interval in range(1, N):
        for start in range(N):
            end = start + interval
            if end >= N:
                continue

            for k in range(start, end):
                counter_left = dp[start][k]
                counter_right = dp[k+1][end]
                counter_middle =\
                    matrix_size[start][0] *\
                    matrix_size[k][1] *\
                    matrix_size[end][1]

                counter_multiplication =\
                    counter_left + counter_middle + counter_right

                if not dp[start][end]:
                    dp[start][end] =\
                        counter_multiplication
                else:
                    dp[start][end] =\
                        min(dp[start][end], counter_multiplication)

    return dp[0][-1]


if __name__ == "__main__":
    matrix_size = [[5, 3],[3, 10],[10, 6]]
    assert solution(matrix_size) == 270
