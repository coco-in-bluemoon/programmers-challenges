def be_in_boundary(position, board):
    N = len(board)
    r, c = position
    return 0 <= r < N and 0 <= c < N


def fill_black_block(board):
    N = len(board)
    for c in range(N):
        for r in range(N):
            if board[r][c] <= 0:
                board[r][c] = -1
            else:
                break


def possible_to_delete(position, shape, board):
    base_r, base_c = position
    target_block = board[base_r][base_c]
    counter = 0

    for dr in range(shape[0]):
        for dc in range(shape[1]):
            r, c = base_r + dr, base_c + dc
            if not be_in_boundary((r, c), board):
                return False
            if board[r][c] == 0:
                return False

            if target_block <= 0 and board[r][c] > 0:
                target_block = board[r][c]

            if target_block > 0 and board[r][c] > 0:
                if target_block != board[r][c]:
                    return False
                counter += 1

    return counter == 4


def delete_block(position, shape, board):
    base_r, base_c = position
    for dr in range(shape[0]):
        for dc in range(shape[1]):
            r, c = base_r + dr, base_c + dc
            board[r][c] = 0


def delete_if_possible(board):
    N = len(board)
    SHAPE_VER_REC = (3, 2)
    SHAPE_HOR_REC = (2, 3)
    counter = 0
    for r in range(N):
        for c in range(N):
            if possible_to_delete((r, c), SHAPE_VER_REC, board):
                delete_block((r, c), SHAPE_VER_REC, board)
                counter += 1
            elif possible_to_delete((r, c), SHAPE_HOR_REC, board):
                delete_block((r, c), SHAPE_HOR_REC, board)
                counter += 1

    return counter


def solution(board):
    answer = 0
    while True:
        fill_black_block(board)
        counter_deleted = delete_if_possible(board)
        if not counter_deleted:
            break
        answer += counter_deleted
    return answer


if __name__ == "__main__":
    board = [
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 4, 0, 0, 0],
        [0, 0, 0, 0, 0, 4, 4, 0, 0, 0],
        [0, 0, 0, 0, 3, 0, 4, 0, 0, 0],
        [0, 0, 0, 2, 3, 0, 0, 0, 5, 5],
        [1, 2, 2, 2, 3, 3, 0, 0, 0, 5],
        [1, 1, 1, 0, 0, 0, 0, 0, 0, 5]
    ]
    assert solution(board) == 2

    board = [
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 2, 2, 0, 0, 0, 0, 0],
        [0, 0, 0, 2, 1, 0, 0, 0, 0, 0],
        [0, 0, 0, 2, 1, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 1, 1, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
    ]
    assert solution(board) == 1

    board = [
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 1, 2, 0, 0, 0, 0],
        [0, 0, 0, 0, 1, 2, 2, 2, 0, 0],
        [0, 0, 0, 0, 1, 1, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
    ]
    assert solution(board) == 2

    board = [
        [0, 0, 0, 0, 0],
        [1, 0, 0, 2, 0],
        [1, 2, 2, 2, 0],
        [1, 1, 0, 0, 0],
        [0, 0, 0, 0, 0]
    ]
    assert solution(board) == 2

    board = [
        [0, 2, 0, 0],
        [1, 2, 0, 4],
        [1, 2, 2, 4],
        [1, 1, 4, 4]
    ]
    assert solution(board) == 3
