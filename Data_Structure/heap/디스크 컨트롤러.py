import heapq

def solution(jobs):
    answer,now,i = 0,0,0
    start = -1
    heap = []
    
    while i < len(jobs):
        for j in jobs:
            #태스크 처리 도중에 들어온 태스크들을 소요 시간 기준으로 정렬
            if start < j[0] <= now:
                heapq.heappush(heap, [j[1], j[0]])
        #태스크 처리        
        if len(heap) > 0:
            current = heapq.heappop(heap)
            start = now
            now += current[0]
            answer += (now - current[1])
            i+=1
        else:
            now+=1
    
    return int(answer/len(jobs))

#못풀었다..
# 현재 시점에서 처리할 수 있는 작업들을 힙에 넣는다.
# 하나를 뽑아 현재 시점과 총 대기시간을 구해주는 것을 모든 작업이 끝날때까지 반복
#출처 : https://velog.io/@younge/Python-%ED%94%84%EB%A1%9C%EA%B7%B8%EB%9E%98%EB%A8%B8%EC%8A%A4-%EB%94%94%EC%8A%A4%ED%81%AC-%EC%BB%A8%ED%8A%B8%EB%A1%A4%EB%9F%AC-%ED%9E%99