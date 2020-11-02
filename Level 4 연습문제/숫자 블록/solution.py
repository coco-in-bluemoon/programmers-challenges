def get_block_number(number):
    if number == 1:
        return 0

    for base in range(2, int(number ** 0.5) + 1):
        MAXIMUM_BLOCK = 10**7
        if number % base:
            continue
        
        block_number = number // base
        if block_number <= MAXIMUM_BLOCK:
            return block_number

    return 1


def solution(begin, end):
    answer = list()
    for num in range(begin, end+1):
        block_number = get_block_number(num)
        answer.append(block_number)

    return answer


if __name__ == "__main__":
    begin = 1
    end = 10
    answer = [0, 1, 1, 2, 1, 3, 1, 4, 3, 5]
    assert solution(begin, end) == answer
