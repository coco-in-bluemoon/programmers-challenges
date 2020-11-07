import re


def solution(dartResult):
    pattern = r'(([0-9]+)([SDT])([*#]?))'
    trials = re.findall(pattern, dartResult)

    scores = list()
    for trial in trials:
        _, base_score, bonus, option = trial

        score = int(base_score)
        if bonus == 'D':
            score = int(base_score) ** 2
        elif bonus == 'T':
            score = int(base_score) ** 3

        if option == '*':
            if scores:
                scores[-1] = scores[-1] * 2
            score *= 2
        elif option == '#':
            score *= -1

        scores.append(score)

    answer = sum(scores)
    return answer


if __name__ == "__main__":
    dartResult = '1S2D*3T'
    assert solution(dartResult) == 37

    dartResult = '1D2S#10S'
    assert solution(dartResult) == 9

    dartResult = '1D2S0T'
    assert solution(dartResult) == 3

    dartResult = '1S*2T*3S'
    assert solution(dartResult) == 23

    dartResult = '1D#2S*3S'
    assert solution(dartResult) == 5

    dartResult = '1T2D3D#'
    assert solution(dartResult) == -4

    dartResult = '1D2S3T*'
    assert solution(dartResult) == 59
