def be_possible_to_delete(base_r, base_c, board):
    target_block = board[base_r][base_c]
    for dr in range(2):
        for dc in range(2):
            r, c = base_r + dr, base_c + dc
            if board[r][c] != target_block:
                return False
    return True


def delete_blocks(positions, board):
    counter = 0
    for base_r, base_c in positions:
        for dr in range(2):
            for dc in range(2):
                r, c = base_r + dr, base_c + dc
                counter += (1 if board[r][c] else 0)
                board[r][c] = ''
    return counter


def delete_block_if_possible(board):
    R = len(board)
    C = len(board[0])

    deleted_positions = set()
    for r in range(R-1):
        for c in range(C-1):
            if be_possible_to_delete(r, c, board):
                deleted_positions.add((r, c))

    counter = delete_blocks(deleted_positions, board)
    return counter


def fill_block_downward(board):
    R = len(board)
    C = len(board[0])

    for c in range(C):
        index_filled = R-1
        index_pointing = R-1

        while index_pointing >= 0:
            if board[index_pointing][c]:
                board[index_filled][c] = board[index_pointing][c]
                index_filled -= 1
                index_pointing -= 1
            else:
                index_pointing -= 1

        while index_filled >= 0:
            board[index_filled][c] = ''
            index_filled -= 1


def solution(m, n, board):
    answer = 0
    board = [list(row) for row in board]
    while True:
        counter_deleted = delete_block_if_possible(board)
        if not counter_deleted:
            break
        answer += counter_deleted
        fill_block_downward(board)
    return answer


if __name__ == '__main__':
    m, n = 4, 5
    board = ['CCBDE', 'AAADE', 'AAABF', 'CCBBF']
    assert solution(m, n, board) == 14

    m, n = 6, 6
    board = ['TTTANT', 'RRFACC', 'RRRFCC', 'TRRRAA', 'TTMMMF', 'TMMTTJ']
    assert solution(m, n, board) == 15
