def solution(n):
    answer = 1
    for i in range(1,int(n/2)+1):
        sum_num = 0 
        for j in range(i,int(n/2)+2):
            sum_num+=j
            if sum_num==n:
                answer+=1
                break
            elif sum_num>n:
                break
    return answer