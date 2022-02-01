# 문제 접근을 잘못한 문제
from itertools import combinations
from collections import Counter

def solution(orders, course):
    answer = []
    
    orders_arrange = []
    for i in orders:
        orders_arrange.append("".join(sorted(list(i))))
        
    orders_arrange.sort()
        
    
    for i in course:
        temp = []
        for j in orders:
            combi = combinations(sorted(j), i)
            temp += combi
        counter = Counter(temp)
        print(counter)
        if len(counter) != 0 and max(counter.values()) != 1:
            answer += [''.join(f) for f in counter if counter[f] == max(counter.values())]

    return sorted(answer)

# from itertools import combinations

# def solution(orders, course):
#     answer = []
    
#     orders_arrange = []
#     for i in orders:
#         orders_arrange.append("".join(sorted(list(i))))
        
#     orders_arrange.sort()
        
    
#     for i in course:
#         for j in orders_arrange:
#             if len(j)>i:
#                 order_tmp = list(combinations(j,i))
                
#                 for k in order_tmp:
#                     # print(k)
#                     if k in orders:
#                         print("hi")
#                         answer.append(k)
                
    
#     return sorted(answer)