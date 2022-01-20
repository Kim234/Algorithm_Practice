def solution(priorities, location):
    answer = 0
    prior_number = [(idx,p) for idx,p in enumerate(priorities)]

    while True:
        pop_one = prior_number.pop(0)
        if pop_one[1]==max(priorities):
            answer+=1
            priorities.remove(pop_one[1])
            if pop_one[0]==location:
                return answer
        else:
            prior_number.append(pop_one)
            # print(prior_number)

# def solution(priorities, location):
#     pop_list=[]
#     i=0
#     while len(pop_list)<=len(priorities):
#         # print(pop_list)
#         if priorities[i] == max(priorities):
#             pop_list.append(i)
#             priorities[i]=0
        
#         else:
#             i=priorities.index(max(priorities))
#             pop_list.append(i)
#             priorities[i]=0

#         if i==len(priorities)-1:
#             i=0
#         else:
#             i+=1    
#     return pop_list.index(location)+1

## pop_list에 max값듣 저장하는 방식
##찾아낸 반례
# ([1,3,9,3,2,3],1) return 4 --> 하지만 이 코드는 return 3
# max값 있던 인덱스 뒤로 max 값을 찾으러 가야하지만, 다시 index1부터 시작 -- ex)모범답안9-->index3인 3 <-->내 방식 9-->index1인 3