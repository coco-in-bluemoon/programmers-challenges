def solution(record):
    userid2name = dict()
    for log in record:
        parameters = log.split()
        if len(parameters) == 2:
            continue
        userid, name = parameters[1], parameters[2]
        userid2name[userid] = name

    messages = list()
    for log in record:
        parameters = log.split()
        if parameters[0].lower() == 'change':
            continue
        action = '들어왔습니다.' if parameters[0].lower() == 'enter' else '나갔습니다.'
        userid = parameters[1]
        message = f'{userid2name[userid]}님이 {action}'
        messages.append(message)
    return messages


if __name__ == "__main__":
    record = [
        "Enter uid1234 Muzi",
        "Enter uid4567 Prodo",
        "Leave uid1234",
        "Enter uid1234 Prodo",
        "Change uid4567 Ryan"
    ]

    answer = [
        "Prodo님이 들어왔습니다.",
        "Ryan님이 들어왔습니다.",
        "Prodo님이 나갔습니다.",
        "Prodo님이 들어왔습니다."
    ]

    my_answer = solution(record)
    assert my_answer == answer
