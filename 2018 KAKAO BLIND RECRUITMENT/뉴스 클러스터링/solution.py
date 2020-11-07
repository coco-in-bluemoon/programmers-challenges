import re


def get_bigram_subset(str):
    str = str.lower()
    pattern = r'[a-z][a-z]'
    bigrams = list()
    for idx in range(len(str)):
        bigram = str[idx:idx+2]
        if re.match(pattern, bigram):
            bigrams.append(bigram)
    return bigrams


def calculate_jaccard_similarity(bigram1, bigram2):
    bigram1 = sorted(bigram1)
    bigram2 = sorted(bigram2)

    idx = 0
    jdx = 0
    counter_intersect = 0
    while idx < len(bigram1) and jdx < len(bigram2):
        if bigram1[idx] == bigram2[jdx]:
            counter_intersect += 1
            idx += 1
            jdx += 1
        elif bigram1[idx] > bigram2[jdx]:
            jdx += 1
        elif bigram1[idx] < bigram2[jdx]:
            idx += 1

    counter_union = len(bigram1) + len(bigram2) - counter_intersect

    return counter_intersect / counter_union if counter_union else 1


def solution(str1, str2):
    bigram_set_for_str1 = get_bigram_subset(str1)
    bigram_set_for_str2 = get_bigram_subset(str2)

    similarity = calculate_jaccard_similarity(
        bigram_set_for_str1,
        bigram_set_for_str2
    )
    return int(similarity * 65536)


if __name__ == "__main__":
    str1 = 'FRANCE'
    str2 = 'french'
    assert solution(str1, str2) == 16384

    str1 = 'handshake'
    str2 = 'shake hands'
    assert solution(str1, str2) == 65536

    str1 = 'aa1+aa2'
    str2 = 'AAAA12'
    assert solution(str1, str2) == 43690

    str1 = 'E=M*C^2'
    str2 = 'e=m*c^2'
    assert solution(str1, str2) == 65536
