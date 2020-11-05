def solution(N, stages):
    stage_played = {stage: 0 for stage in range(1, N+1)}
    stage_failed = {stage: 0 for stage in range(1, N+1)}

    for stage in stages:
        for s in range(1, stage):
            stage_played[s] += 1

        if stage in stage_played:
            stage_played[stage] += 1
            stage_failed[stage] += 1

    stage_failure_rate = dict()
    for stage in range(1, N+1):
        counter_stage_failed = stage_failed[stage]
        counter_stage_played = stage_played[stage]

        if not counter_stage_played:
            stage_failure_rate[stage] = 0
            continue

        failure_rate = counter_stage_failed / counter_stage_played
        stage_failure_rate[stage] = failure_rate

    answer = list()
    for stage, _ in\
            sorted(stage_failure_rate.items(), key=lambda x: (-x[1], x[0])):
        answer.append(stage)

    return answer


if __name__ == "__main__":
    N = 5
    stages = [2, 1, 2, 6, 2, 4, 3, 3]
    answer = [3, 4, 2, 1, 5]
    my_answer = solution(N, stages)

    assert my_answer == answer
