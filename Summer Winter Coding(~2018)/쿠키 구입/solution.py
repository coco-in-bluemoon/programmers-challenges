def solution(cookie):
    answer = 0
    num_cookie = len(cookie)

    for index_front in range(num_cookie-1):
        index_rear = index_front + 1

        value_front = cookie[index_front]
        value_rear = cookie[index_rear]

        while True:
            if value_front == value_rear:
                answer = max(answer, value_front)

            if index_front > 0 and value_front <= value_rear:
                index_front -= 1
                value_front += cookie[index_front]
            elif index_rear < num_cookie - 1 and value_front >= value_rear:
                index_rear += 1
                value_rear += cookie[index_rear]
            else:
                break

    return answer


if __name__ == "__main__":
    cookie = [1, 1, 2, 3]
    assert solution(cookie) == 3

    cookie = [1, 2, 4, 5]
    assert solution(cookie) == 0
