def possible_to_learn(skill, skill_tree):
    skill_index = 0
    for skill_character in skill_tree:
        if skill_character not in skill:
            continue
        if skill.find(skill_character) != skill_index:
            return False
        skill_index += 1
    return True


def solution(skill, skill_trees):
    counter = 0
    for skill_tree in skill_trees:
        if possible_to_learn(skill, skill_tree):
            counter += 1

    return counter


if __name__ == "__main__":
    skill = "CBD"
    skill_trees = ["BACDE", "CBADF", "AECB", "BDA"]
    assert solution(skill, skill_trees) == 2
