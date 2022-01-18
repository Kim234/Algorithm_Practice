def solution(N, stages):
    user_status = {}
    users = len(stages)
    for stage in range(1, N + 1):
        if users == 0:
            user_status[stage] = 0
            continue
        count = stages.count(stage)
        user_status[stage] = count / users
        print(user_status)
        users -= count
    return sorted(user_status, key=lambda stage: user_status[stage], reverse=True)