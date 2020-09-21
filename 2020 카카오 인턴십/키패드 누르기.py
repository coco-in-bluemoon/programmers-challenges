def calculate_distance(current, target):
    left_numbers = '147*'
    right_numbers = '369#'
    middle_numbers = '2580'

    target_index = middle_numbers.find(target)
    distance = 0

    if current in left_numbers:
        current_index = left_numbers.find(current)
        distance += 1
    elif current in right_numbers:
        current_index = right_numbers.find(current)
        distance += 1
    else:
        current_index = middle_numbers.find(current)

    distance += abs(target_index - current_index)
    return distance


def solution(numbers, hand):
    numbers = [str(number) for number in numbers]

    left = '*'
    right = '#'

    left_numbers = '147*'
    right_numbers = '369#'

    answer = ''
    for number in numbers:
        if number in left_numbers:
            left = number
            answer += 'L'
        elif number in right_numbers:
            right = number
            answer += 'R'
        else:
            left_d = calculate_distance(left, number)
            right_d = calculate_distance(right, number)

            if left_d < right_d:
                left = number
                answer += 'L'
            elif left_d > right_d:
                right = number
                answer += 'R'
            else:
                if hand == 'left':
                    left = number
                    answer += 'L'
                elif hand == 'right':
                    right = number
                    answer += 'R'

    return answer


if __name__ == '__main__':
    numbers = [1, 3, 4, 5, 8, 2, 1, 4, 5, 9, 5]
    hand = 'right'
    assert solution(numbers, hand) == 'LRLLLRLLRRL'

    numbers = [7, 0, 8, 2, 8, 3, 1, 5, 7, 6, 2]
    hand = 'left'
    assert solution(numbers, hand) == 'LRLLRRLLLRR'

    numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 0]
    hand = 'right'
    assert solution(numbers, hand) == 'LLRLLRLLRL'
