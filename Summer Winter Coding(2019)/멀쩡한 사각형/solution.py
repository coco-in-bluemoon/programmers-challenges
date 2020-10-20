def get_gcd(a, b):
    while b:
        a, b = b, a % b
    return a


def solution(w, h):
    w, h = max(w, h), min(w, h)
    gcd = get_gcd(w, h)

    w_part = w // gcd
    h_part = h // gcd

    answer = (w * h) - gcd * (w_part + h_part - 1)
    return answer


if __name__ == "__main__":
    assert solution(8, 12) == 80
    assert solution(3, 3) == 6
