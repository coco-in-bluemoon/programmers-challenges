def be_in_boundary(position, board):
    N = len(board)
    r, c = position

    return 0 <= r < N and 0 <= c < N


def be_possible_to_delete(position, shape, board):
    base_r, base_c = position
    target_block = board[base_r][base_c]
    block_counter = 0
    for dr in range(shape[0]):
        for dc in range(shape[1]):
            r, c = base_r + dr, base_c + dc

            if not be_in_boundary((r, c), board):
                return False
            if not board[r][c]:
                return False

            if target_block == -1 and board[r][c] > 0:
                target_block = board[r][c]

            if target_block > 0:
                if board[r][c] > 0 and board[r][c] != target_block:
                    return False
                elif board[r][c] == target_block:
                    block_counter += 1

    return block_counter == 4


def delete_block(position, shape, board):
    base_r, base_c = position
    for dr in range(shape[0]):
        for dc in range(shape[1]):
            r, c = base_r + dr, base_c + dc
            board[r][c] = 0


def get_number_of_deleted_blocks(board):
    N = len(board)
    HORIZONTAL_REC_SHAPE = (2, 3)
    VERTICAL_REC_SHAPE = (3, 2)

    counter = 0
    for r in range(N):
        for c in range(N):
            if be_possible_to_delete((r, c), HORIZONTAL_REC_SHAPE, board):
                delete_block((r, c), HORIZONTAL_REC_SHAPE, board)
                counter += 1
            elif be_possible_to_delete((r, c), VERTICAL_REC_SHAPE, board):
                delete_block((r, c), VERTICAL_REC_SHAPE, board)
                counter += 1
    return counter


def fill_board(board):
    N = len(board)

    for c in range(N):
        for r in range(N):
            if board[r][c] <= 0:
                board[r][c] = -1
            else:
                break


def solution(board):
    answer = 0
    while True:
        # for row in board:
        #     print('\t'.join([str(item) for item in row]))
        # print()
        fill_board(board)
        # for row in board:
        #     print('\t'.join([str(item) for item in row]))
        # print()
        num_deleted = get_number_of_deleted_blocks(board)
        if not num_deleted:
            break
        answer += num_deleted
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
