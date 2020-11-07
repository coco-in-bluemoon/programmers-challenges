def solution(n, arr1, arr2):
    board = list()
    for num1, num2 in zip(arr1, arr2):
        binary_num = bin(num1 | num2)
        row = str(binary_num)[2:]
        if len(row) < n:
            row = '0' * (n - len(row)) + row

        row = row.replace('0', ' ')
        row = row.replace('1', '#')
        board.append(row)

    return board


if __name__ == "__main__":
    n = 5
    arr1 = [9, 20, 28, 18, 11]
    arr2 = [30, 1, 21, 17, 28]
    answer = ["#####", "# # #", "### #", "#  ##", "#####"]
    assert solution(n, arr1, arr2) == answer
