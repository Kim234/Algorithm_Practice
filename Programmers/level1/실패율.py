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


#1번째 방법 for문과 enumerate를 통해 각 stage별 실패율을 구했지만, 시간에러
#2번째 방법 collections.counter 이용 실패
#마지막 - count와 len으로 단순하게 구함
#이전 시도한 코드 지우지말자..