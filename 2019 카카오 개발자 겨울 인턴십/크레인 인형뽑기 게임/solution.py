from collections import deque


def pop_item(board, move):
    N = len(board)
    c = move - 1

    r = 0
    while r < N and not board[r][c]:
        r += 1

    item = 0
    if r < N:
        item = board[r][c]
        board[r][c] = 0

    return item


def solution(board, moves):
    stack = deque([])

    counter = 0
    for move in moves:
        item = pop_item(board, move)

        if stack and item and stack[-1] == item:
            stack.pop()
            counter += 2
        elif item:
            stack.append(item)

    return counter


if __name__ == "__main__":
    board = [
        [0, 0, 0, 0, 0],
        [0, 0, 1, 0, 3],
        [0, 2, 5, 0, 1],
        [4, 2, 4, 4, 2],
        [3, 5, 1, 3, 1]
    ]
    moves = [1, 5, 3, 5, 1, 2, 1, 4]
    assert solution(board, moves) == 4
