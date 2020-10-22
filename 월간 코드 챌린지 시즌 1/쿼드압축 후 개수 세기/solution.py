def compress_recursive(base_r, base_c, size, arr):
    if size == 1:
        return (0, 1) if arr[base_r][base_c] else (1, 0)

    all_one = True
    all_zero = True
    for dr in range(size):
        for dc in range(size):
            if all_one and not arr[base_r+dr][base_c+dc]:
                all_one = False
            if all_zero and arr[base_r+dr][base_c+dc]:
                all_zero = False
        if not all_one and not all_zero:
            break

    if all_one:
        return (0, 1)
    elif all_zero:
        return (1, 0)

    half_size = size // 2
    counter = (0, 0)

    for dr, dc in\
            zip([0, half_size, 0, half_size], [0, 0, half_size, half_size]):
        temp = compress_recursive(base_r+dr, base_c+dc, half_size, arr)
        counter = (counter[0] + temp[0], counter[1] + temp[1])

    return counter


def solution(arr):
    size = len(arr)
    answer = compress_recursive(0, 0, size, arr)
    return list(answer)


if __name__ == "__main__":
    arr = [
        [1, 1, 0, 0],
        [1, 0, 0, 0],
        [1, 0, 0, 1],
        [1, 1, 1, 1]
    ]
    assert solution(arr) == [4, 9]
