import heapq

def solution(scoville, K):
    answer = 0
    heapq.heapify(scoville)
    while len(scoville)>=2:
        min_spicy = heapq.heappop(scoville)
        
        if min_spicy<K:
            answer+=1
            heapq.heappush(scoville,min_spicy+heapq.heappop(scoville)*2)
            
        else:
            return answer
    
    if scoville[0]>K:
        return answer
            
    else: return -1

# 효율성 테스트 실패 
# def solution(scoville, K):
#     answer = 0
#     while min(scoville)<K:
#         if len(scoville)>=2:
#             scoville.sort()
#             scoville.append(scoville.pop(0)+(scoville.pop(0)*2))
#             answer+=1
            
#         else:
#             return -1
        
#     return answer