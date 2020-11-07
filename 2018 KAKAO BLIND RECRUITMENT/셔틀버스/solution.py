import heapq


def add_time(time_base, time_delta):
    hour, minute = time_base

    minute += time_delta
    if minute >= 60:
        minute -= 60
        hour += 1
    elif minute < 0:
        minute += 60
        hour -= 1

    return (hour, minute)


def get_last_bus_arrival_time(n, t, m, heap_time):
    bus_time = (9, 0)
    for _ in range(n-1):
        for _ in range(m):
            if not heap_time or heap_time[0] > bus_time:
                break
            heapq.heappop(heap_time)
        bus_time = add_time(bus_time, t)
    return bus_time


def solution(n, t, m, timetable):
    heap_time = list()
    for time in timetable:
        hour, minute = time.split(':')
        hour, minute = int(hour), int(minute)

        heapq.heappush(heap_time, (hour, minute))

    last_bus_time = get_last_bus_arrival_time(n, t, m, heap_time)

    if len(heap_time) < m:
        answer = f'{last_bus_time[0]:02}:{last_bus_time[1]:02}'
        return answer

    for _ in range(m-1):
        if not heap_time or heap_time[0] > last_bus_time:
            break
        heapq.heappop(heap_time)

    if heap_time and heap_time[0] <= last_bus_time:
        answer_time = add_time(heap_time[0], -1)
        answer = f'{answer_time[0]:02}:{answer_time[1]:02}'
        return answer

    answer = f'{last_bus_time[0]:02}:{last_bus_time[1]:02}'
    return answer


if __name__ == "__main__":
    n, t, m = 1, 1, 5
    timetable = ['08:00', '08:01', '08:02', '08:03']
    answer = '09:00'
    assert solution(n, t, m, timetable) == answer

    n, t, m = 2, 10, 2
    timetable = ['09:10', '09:09', '08:00']
    answer = '09:09'
    assert solution(n, t, m, timetable) == answer
