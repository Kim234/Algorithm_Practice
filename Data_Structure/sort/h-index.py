def solution(citations):
    answer_list = []
    citations.sort(reverse=True)
    for i in range(0,len(citations)):
        if citations[i] >= i+1:
            answer_list.append(i+1)
        else:
            if citations[i]==0: answer_list.append(0)
            break
    return max(answer_list)