import re
from typing import AnyStr


def solution(s):
    items = re.findall(r'{([0-9,]+)}', s)
    items = sorted(items, key=lambda x: len(x))

    answer = list()
    for item in items:
        for number in item.split(','):
            if int(number) in answer:
                continue
            answer.append(int(number))

    return answer


if __name__ == "__main__":
    s = '{{2},{2,1},{2,1,3},{2,1,3,4}}'
    assert solution(s) == [2, 1, 3, 4]

    s = '{{1,2,3},{2,1},{1,2,4,3},{2}}'
    assert solution(s) == [2, 1, 3, 4]

    s = '{{20,111},{111}}'
    assert solution(s) == [111, 20]

    s = '{{123}}'
    assert solution(s) == [123]

    s = '{{4,2,3},{3},{2,3,4,1},{2,3}}'
    assert solution(s) == [3, 2, 4, 1]
