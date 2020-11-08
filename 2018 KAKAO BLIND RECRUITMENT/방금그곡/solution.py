import math
import re


def get_time_diff_minute(before, after):
    MINUTE_PER_HOUR = 60

    before_hour, before_minute = before
    after_hour, after_minute = after

    before_minute += (before_hour * MINUTE_PER_HOUR)
    after_minute += (after_hour * MINUTE_PER_HOUR)

    return after_minute - before_minute


def get_full_melody(begin, end, melody):
    begin_hour, begin_minute = begin.split(':')
    end_hour, end_minute = end.split(':')

    minute_diff = get_time_diff_minute(
        (int(begin_hour), int(begin_minute)),
        (int(end_hour), int(end_minute))
    )

    melody_size = len(melody)

    num_cycle = math.floor(minute_diff / melody_size)
    num_left = minute_diff % melody_size

    full_melody = melody * num_cycle + melody[:num_left]
    return full_melody


def abbreviate_sharp_in_melody(melody):
    pattern = r'([A-G]#)'
    while re.search(pattern, melody):
        sharp_code = re.search(pattern, melody).group()
        symbol = sharp_code[0].lower()
        melody = melody.replace(sharp_code, symbol)
    return melody


def solution(m, musicinfos):
    NOT_FOUND = -1
    m = abbreviate_sharp_in_melody(m)
    answer = '(None)'
    duration = 0
    for musicinfo in musicinfos:
        begin_time, end_time, title, melody = musicinfo.split(',')
        melody = abbreviate_sharp_in_melody(melody)
        full_melody = get_full_melody(begin_time, end_time, melody)

        if full_melody.find(m) != NOT_FOUND:
            if len(full_melody) > duration:
                answer = title
                duration = len(full_melody)

    return answer


if __name__ == "__main__":
    m = 'ABCDEFG'
    musicinfos = [
        '12:00,12:14,HELLO,CDEFGAB',
        '13:00,13:05,WORLD,ABCDEF'
    ]
    assert solution(m, musicinfos) == 'HELLO'

    m = 'CC#BCC#BCC#BCC#B'
    musicinfos = [
        '03:00,03:30,FOO,CC#B',
        '04:00,04:08,BAR,CC#BCC#BCC#B'
    ]
    assert solution(m, musicinfos) == 'FOO'

    m = 'ABC'
    musicinfos = [
        '12:00,12:14,HELLO,C#DEFGAB',
        '13:00,13:05,WORLD,ABCDEF'
    ]
    assert solution(m, musicinfos) == 'WORLD'
