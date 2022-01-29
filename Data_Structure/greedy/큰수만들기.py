# 구글링.. 다시 풀어보기
def solution(number, k):
    answer = [] # Stack
    
    for num in number:
        while k > 0 and answer and answer[-1] < num:
            answer.pop()
            k -= 1
        answer.append(num)
        
    return ''.join(answer[:len(answer) - k])

# 두 번째 방식 -- 각 자릿수에 들어갈 최선의 숫자 정하기
# 1개 케이스 시간초과 -- number자릿수가 몇십만으로 예상 따라서, max 사용하면 X --> 탐욕법(하나씩 비교 필요)
# def solution(number, k):

#     stack = []
#     goal = len(number)-k
#     remain_len = len(number)-k-1
    
#     # 각 자릿수마다 최선의 선택 "4177252841"에서 십만자리의 최선: 7(4,1,7,7,2 중)
#     while True:
#         goal_len = remain_len - len(stack)
#         max_index = number.index(max(number[:len(number)-goal_len]))
#         stack.append(number[max_index])
        
#         if len(stack)==goal:
#             break
#         number = number[max_index+1:]
               
#     return "".join(stack)

# combinations 사용 --> 시간초과
# from itertools import combinations

# def solution(number, k):
#     answer = ''
#     num_arr = list(combinations(number,len(number)-k))
#     for i in max(num_arr):
#         answer+=i

#     return answer