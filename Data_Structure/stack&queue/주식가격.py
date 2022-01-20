def solution(prices):
    answer = []
    for i in range(len(prices)):
        remain_time = 0
        for j in range(i+1,len(prices)):
            remain_time+=1
            if prices[i]<=prices[j]:
                continue
            else:
                break
        answer.append(remain_time)
    return answer