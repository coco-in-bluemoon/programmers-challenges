def solution(triangle):
    H = len(triangle)
    dp = [[0] * len(triangle[h]) for h in range(H)]

    for h in range(H):
        level = triangle[h]
        for idx in range(len(level)):
            if h < 1:
                dp[h][idx] = triangle[h][idx]
                continue
            if idx == 0:
                dp[h][idx] = dp[h-1][idx] + triangle[h][idx]
                continue
            if idx == len(level) - 1:
                dp[h][idx] = dp[h-1][idx-1] + triangle[h][idx]
                continue

            upper_left = dp[h-1][idx-1]
            upper_right = dp[h-1][idx]
            dp[h][idx] = max(upper_left, upper_right) + triangle[h][idx]

    return max(dp[-1])


if __name__ == "__main__":
    triangle = [[7], [3, 8], [8, 1, 0], [2, 7, 4, 4], [4, 5, 2, 6, 5]]
    assert solution(triangle) == 30
