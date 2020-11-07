import datetime


def count_number_of_traffic(base_time, times):
    counter = 0
    base_time_end = base_time + datetime.timedelta(seconds=0.999)

    for start_time, end_time in times:
        if end_time < base_time:
            continue
        elif base_time <= end_time <= base_time_end:
            counter += 1
        elif base_time <= start_time <= base_time_end:
            counter += 1
        elif base_time_end < start_time:
            break
    return counter


def solution(lines):
    times = list()
    for line in lines:
        date_str, time_str, duration_str = line.split()

        end_time = datetime.datetime.strptime(
            f'{date_str} {time_str}', '%Y-%m-%d %H:%M:%S.%f'
        )

        duration = float(duration_str.replace('s', '')) - 0.001
        start_time = end_time - datetime.timedelta(seconds=duration)

        times.append((start_time, end_time))

    answer = 0
    for start_time, end_time in times:
        counter_from_start = count_number_of_traffic(start_time, times)
        counter_from_end = count_number_of_traffic(end_time, times)

        answer = max(answer, counter_from_start, counter_from_end)

    return answer


if __name__ == "__main__":
    lines = ["2016-09-15 00:00:00.000 3s"]
    assert solution(lines) == 1

    lines = ["2016-09-15 23:59:59.999 0.001s"]
    assert solution(lines) == 1

    lines = ["2016-09-15 01:00:04.001 2.0s", "2016-09-15 01:00:07.000 2s"]
    assert solution(lines) == 1

    lines = ["2016-09-15 01:00:04.002 2.0s", "2016-09-15 01:00:07.000 2s"]
    assert solution(lines) == 2

    lines = [
        "2016-09-15 20:59:57.421 0.351s",
        "2016-09-15 20:59:58.233 1.181s",
        "2016-09-15 20:59:58.299 0.8s",
        "2016-09-15 20:59:58.688 1.041s",
        "2016-09-15 20:59:59.591 1.412s",
        "2016-09-15 21:00:00.464 1.466s",
        "2016-09-15 21:00:00.741 1.581s",
        "2016-09-15 21:00:00.748 2.31s",
        "2016-09-15 21:00:00.966 0.381s",
        "2016-09-15 21:00:02.066 2.62s"
    ]
    assert solution(lines) == 7

    lines = ["2016-09-15 00:00:00.000 2.3s", "2016-09-15 23:59:59.999 0.1s"]
    assert solution(lines) == 1

    lines = ["2016-09-15 03:10:33.020 0.011s"]
    assert solution(lines) == 1
