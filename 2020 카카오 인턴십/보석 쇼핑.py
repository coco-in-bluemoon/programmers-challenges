from collections import defaultdict


def solution(gems):
    N = len(set(gems))
    shopping_cart = defaultdict(int)
    answer = [1, len(gems)]

    ldx = rdx = 0
    shopping_cart[gems[ldx]] = 1

    while rdx < len(gems):
        if len(shopping_cart) == N:
            if (rdx - ldx) < (answer[1] - answer[0]):
                answer = [ldx+1, rdx+1]

            gem = gems[ldx]

            shopping_cart[gem] -= 1
            if not shopping_cart[gem]:
                shopping_cart.pop(gem)

            ldx += 1
        else:
            rdx += 1
            if rdx < len(gems):
                gem = gems[rdx]
                shopping_cart[gem] += 1

    return answer


if __name__ == '__main__':
    gems = ['DIA', 'RUBY', 'RUBY', 'DIA', 'DIA', 'EMERALD', 'SAPPHIRE', 'DIA']
    assert solution(gems) == [3, 7]

    gems = ['AA', 'AB', 'AC', 'AA', 'AC']
    assert solution(gems) == [1, 3]

    gems = ['XYZ', 'XYZ', 'XYZ']
    assert solution(gems) == [1, 1]

    gems = ['ZZZ', 'YYY', 'NNNN', 'YYY', 'BBB']
    assert solution(gems) == [1, 5]
