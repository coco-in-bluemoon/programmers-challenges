import sys
sys.setrecursionlimit(10**9)


def find_empty_room(room, room_occupation):
    if room not in room_occupation:
        room_occupation[room] = room + 1
        return room

    empty_room = find_empty_room(room_occupation[room], room_occupation)
    room_occupation[room] = empty_room + 1
    return empty_room


def solution(k, room_number):
    answer = list()
    room_occupation = dict()
    for room in room_number:
        empty_room = find_empty_room(room, room_occupation)
        answer.append(empty_room)

    return answer


if __name__ == "__main__":
    k = 10
    room_number = [1, 3, 4, 1, 3, 1]
    assert solution(k, room_number) == [1, 3, 4, 2, 5, 6]
