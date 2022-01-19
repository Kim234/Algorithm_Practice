import operator

def solution(genres, plays):
    answer = []
    idx=0
    #각 장르별 재생횟수를 저장하는 hash
    genres_hash = {g:[] for g in genres}
    #각 장르별 재생횟수의 총합을 저장하는 hash
    sum_hash = {g:0 for g in genres}
    
    #각 장르별 재생횟수를 저장하는 hash를 만들고, 각 장르 배열 안 요소를 재생횟수 내림차순, 인덱스 오름차순
    for g,p in zip(genres,plays):
        genres_hash[g].append([p,idx])
        sum_hash[g]+=p
        idx+=1
    
    for i in genres_hash.keys():
        genres_hash[i].sort(key=lambda x:(-x[0],x[1]))

    #각 장르별 재생횟수의 총합 hash 또한 내림차순 정렬
    sum_hash_order= sorted(sum_hash.items(),key=operator.itemgetter(1),reverse=True)
    
    #총합 저장한 hash를 기준으로 각 장르별 재생횟수를 확인
    #가장 큰 2개의 인덱스 출력//노래가 하나일 때는 1개의 인덱스
    for g in sum_hash_order:
        if len(genres_hash[g[0]])>1:
            for i in range(0,2):
                answer.append(genres_hash[g[0]][i][1])

        else:
            answer.append(genres_hash[g[0]][0][1])
    return answer

