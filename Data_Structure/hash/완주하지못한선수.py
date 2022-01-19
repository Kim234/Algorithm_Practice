import operator

def solution(participant, completion):

    part_dict ={i:participant.count(i) for i in participant}
    for i in completion:
        if i in part_dict:
            part_dict[i]-=1

    return sorted(part_dict.items(),key=operator.itemgetter(1),reverse=True)[0][0]


# counter사용 간단한 방법
# import collections


# def solution(participant, completion):
#     answer = collections.Counter(participant) - collections.Counter(completion)
#     return list(answer.keys())[0]