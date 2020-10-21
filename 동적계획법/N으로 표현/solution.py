from itertools import product


def solution(n, number):
    MAX_TRIAL = 8
    dp = {trial: set([int(str(n) * trial)]) for trial in range(1, MAX_TRIAL+1)}

    for trial in range(1, MAX_TRIAL+1):
        for src in range(1, trial):
            dst = trial - src

            src_set = dp[src]
            dst_set = dp[dst]

            for s, d in product(src_set, dst_set):
                dp[trial].add(s+d)
                dp[trial].add(s-d)
                dp[trial].add(s*d)
                if d:
                    dp[trial].add(s//d)

        if number in dp[trial]:
            return trial
    return -1


if __name__ == "__main__":
    assert solution(5, 12) == 4
    assert solution(2, 11) == 3
    assert solution(4, 4) == 1
