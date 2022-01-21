import heapq

def solution(operations):
    answer = []
    # 1. operations를 분리하여 리스트형태로 저장
    op_list = [op.split(" ") for op in operations]
    
    # 2. for문을 통해 operation 돌림
    # - 'I' 일때 :  큐에 삽입
    # - 'D' 일때 - '1'일때: 최대값 삭제 '2'일때: 최솟값 삭제
    for i in op_list:
        if i[0] == 'I':
            heapq.heappush(answer, int(i[1]))
        
        else:
            if len(answer)>0:
                if i[1] == '1':
                    # answer = max_heap(answer)
                    # 리스트처럼 간단히 max 값 찾아서 제거 가능
                    answer.remove(max(answer))     
                else:
                    heapq.heappop(answer)
    return [max(answer),min(answer)] if len(answer)>0 else [0,0]

# def max_heap(heap):
#     heap_outmax =[]
#     length = len(heap)
#     for i in range(length):
#         if i !=length-1:
#             heapq.heappush(heap_outmax,heapq.heappop(heap))
#     return heap_outmax