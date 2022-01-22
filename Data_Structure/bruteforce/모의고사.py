import collections

def solution(answers):
    answer=[]
    answer_num=[0,0,0]
    one_p = [1,2,3,4,5]
    two_p = [2,1,2,3,2,4,2,5]
    three_p = [3,3,1,1,2,2,4,4,5,5]
    
    for i in range(len(answers)):
        if answers[i] == one_p[i%5]:
            answer_num[0]+=1
        if answers[i] == two_p[i%8]:
            answer_num[1]+=1
        if answers[i] == three_p[i%10]:
            answer_num[2]+=1

    for i in range(len(answer_num)):
        if answer_num[i]==max(answer_num):
            answer.append(i+1)
        
    return answer