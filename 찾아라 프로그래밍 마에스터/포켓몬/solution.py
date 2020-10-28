def solution(nums):
    n = len(nums)
    unique_counter = len(set(nums))
    answer = unique_counter if unique_counter < (n // 2) else (n // 2)
    return answer


if __name__ == "__main__":
    nums = [3, 1, 2, 3]
    assert solution(nums) == 2

    nums = [3, 3, 3, 2, 2, 4]
    assert solution(nums) == 3

    nums = [3, 3, 3, 2, 2, 2]
    assert solution(nums) == 2
