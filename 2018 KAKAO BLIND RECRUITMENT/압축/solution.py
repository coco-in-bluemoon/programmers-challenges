def solution(msg):
    ASCII_A = 97
    ASCII_Z = 122
    character2index = dict()
    for i, ascii in enumerate(range(ASCII_A, ASCII_Z + 1)):
        index = i + 1
        character = chr(ascii)
        character2index[character] = index

    msg = msg.lower()
    index = 0
    answer = list()
    character = ''
    while index < len(msg):
        if (character + msg[index]) not in character2index:
            answer.append(character2index[character])

            last_index = len(character2index) + 1
            character2index[character + msg[index]] = last_index
            character = ''

        character += msg[index]
        index += 1

    answer.append(character2index[character])
    return answer


if __name__ == "__main__":
    msg = 'KAKAO'
    answer = [11, 1, 27, 15]
    assert solution(msg) == answer
