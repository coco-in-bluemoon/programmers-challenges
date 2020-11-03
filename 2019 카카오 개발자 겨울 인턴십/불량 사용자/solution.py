from itertools import product
import re


def solution(user_id, banned_id):
    bad_users = dict()

    for pattern in banned_id:
        if pattern in bad_users:
            continue

        pattern_regex = r'^' + pattern.replace('*', '.') + '$'
        bad_users[pattern] = list()

        for user in user_id:
            if re.match(pattern_regex, user):
                bad_users[pattern].append(user)

    bad_user_combinations = set()
    candidates = [bad_users[key] for key in banned_id]
    for candidate in product(*candidates):
        if len(candidate) != len(set(candidate)):
            continue
        bad_user_combination = ' '.join(sorted(candidate))
        bad_user_combinations.add(bad_user_combination)

    counter = len(bad_user_combinations)
    return counter


if __name__ == "__main__":
    user_id = [
        "frodo", "fradi", "crodo",
        "abc123", "frodoc"
    ]
    banned_id = ["fr*d*", "abc1**"]	
    assert solution(user_id, banned_id) == 2

    user_id = [
        "frodo", "fradi",
        "crodo", "abc123", "frodoc"
    ]
    banned_id = ["*rodo", "*rodo", "******"]
    assert solution(user_id, banned_id) == 2

    user_id = [
        "frodo", "fradi",
        "crodo", "abc123", "frodoc"
    ]
    banned_id = ["fr*d*", "*rodo", "******", "******"]
    assert solution(user_id, banned_id) == 3
