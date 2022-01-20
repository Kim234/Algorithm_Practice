import math

def solution(progresses, speeds):
    
    complete_list = [math.ceil((100-progress)/speed) for progress,speed in zip(progresses, speeds)]
    answer = [1]
    
    while len(complete_list)!=1:
        
        if complete_list[1]<=complete_list[0]:
            answer[len(answer)-1]+=1
            complete_list.pop(1)
        
        else:
            answer.append(1)
            complete_list.pop(0)
    return answer