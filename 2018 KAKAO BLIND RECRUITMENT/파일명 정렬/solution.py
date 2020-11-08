import re


def solution(files):
    file_composition = list()
    pattern = r'^([^\d]+)([\d]+)(.*)$'
    for idx, file in enumerate(files):
        head, number, tail = re.match(pattern, file).groups()
        head = head.lower()
        number = int(number)
        file_composition.append((head, number, idx, tail))

    answer = list()
    for file in sorted(file_composition):
        file_index = file[2]
        answer.append(files[file_index])
    return answer


if __name__ == "__main__":
    files = [
        'img12.png', 'img10.png', 'img02.png',
        'img1.png', 'IMG01.GIF', 'img2.JPG'
    ]
    answer = [
        'img1.png', 'IMG01.GIF', 'img02.png',
        'img2.JPG', 'img10.png', 'img12.png'
    ]
    assert solution(files) == answer

    files = [
        'F-5 Freedom Fighter', 'B-50 Superfortress',
        'A-10 Thunderbolt II', 'F-14 Tomcat'
    ]
    answer = [
        'A-10 Thunderbolt II', 'B-50 Superfortress',
        'F-5 Freedom Fighter', 'F-14 Tomcat'
    ]
    assert solution(files) == answer
