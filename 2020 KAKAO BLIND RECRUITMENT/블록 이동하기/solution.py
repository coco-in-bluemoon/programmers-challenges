from collections import deque


def be_in_boundary(position, board):
    n = len(board)
    r, c = position

    return 0 <= r < n and 0 <= c < n


def be_blocked(position, board):
    r, c = position
    return board[r][c]


def shift(parameters):
    left = parameters['left']
    right = parameters['right']
    counter = parameters['counter']
    queue = parameters['queue']
    visited = parameters['visited']
    board = parameters['board']

    for dr, dc in zip([0, 0, 1, -1], [-1, 1, 0, 0]):
        next_left = (left[0]+dr, left[1]+dc)
        next_right = (right[0]+dr, right[1]+dc)
        next_left, next_right =\
            min(next_left, next_right), max(next_left, next_right)

        if not be_in_boundary(next_left, board):
            continue
        if not be_in_boundary(next_right, board):
            continue

        if be_blocked(next_left, board):
            continue
        if be_blocked(next_right, board):
            continue

        if (next_left + next_right) in visited:
            continue

        queue.append((next_left, next_right, counter+1))


def rotate(parameters, deltas):
    left = parameters['left']
    right = parameters['right']
    counter = parameters['counter']
    queue = parameters['queue']
    visited = parameters['visited']
    board = parameters['board']

    left_deltas = deltas['left']
    right_deltas = deltas['right']
    remain_deltas = deltas['remain']

    for left_delta, right_delta, remain_delta in\
            zip(left_deltas, right_deltas, remain_deltas):
        next_left = (left[0]+left_delta[0], left[1]+left_delta[1])
        next_right = (right[0]+right_delta[0], right[1]+right_delta[1])
        remain = (left[0]+remain_delta[0], left[1]+remain_delta[1])

        next_left, next_right =\
            min(next_left, next_right), max(next_left, next_right)

        if not be_in_boundary(next_left, board):
            continue
        if not be_in_boundary(next_right, board):
            continue
        if not be_in_boundary(remain, board):
            continue
        if be_blocked(next_left, board):
            continue
        if be_blocked(next_right, board):
            continue
        if be_blocked(remain, board):
            continue
        if (next_left+next_right) in visited:
            continue

        queue.append((next_left, next_right, counter+1))


def solution(board):
    n = len(board)
    queue = deque([((0, 0), (0, 1), 0)])
    visited = set()
    while queue:
        left, right, counter = queue.popleft()
        if (left + right) in visited:
            continue
        visited.add(left + right)

        if left == (n-1, n-1) or right == (n-1, n-1):
            return counter

        parameters = {
            'left': left,
            'right': right,
            'counter': counter,
            'queue': queue,
            'visited': visited,
            'board': board
        }

        # Shift Move
        shift(parameters)

        # Rotate Move
        deltas = {'left': list(), 'right': list(), 'remain': list()}
        if left[0] == right[0]:
            deltas = {
                'left': [(0, 0), (0, 0), (1, 1), (-1, 1)],
                'right': [(1, -1), (-1, -1), (0, 0), (0, 0)],
                'remain': [(1, 1), (-1, 1), (1, 0), (-1, 0)]
            }
        elif left[1] == right[1]:
            deltas = {
                'left': [(0, 0), (0, 0), (1, 1), (1, -1)],
                'right': [(-1, 1), (-1, -1), (0, 0), (0, 0)],
                'remain': [(1, 1), (1, -1), (0, 1), (0, -1)]
            }

        rotate(parameters, deltas)

    return -1


if __name__ == "__main__":
    board = [
        [0, 0, 0, 1, 1],
        [0, 0, 0, 1, 0],
        [0, 1, 0, 1, 1],
        [1, 1, 0, 0, 1],
        [0, 0, 0, 0, 0]
    ]
    my_answer = solution(board)
    answer = 7
    assert my_answer == answer
