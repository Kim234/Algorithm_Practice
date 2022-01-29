import collections
def solution(n, lost, reserve):
    answer = n
    # 여벌 체육복을 가져온 사람이 도난당했을 경우 빼주기
    new_reserve = list(collections.Counter(reserve) - collections.Counter(lost))
    new_lost = list(collections.Counter(lost) - collections.Counter(reserve))
    
    # sort를 안해주면 최댓값을 못 구할 수 있음
    # i-1(앞 번호), i+1(뒷 번호) 순서로 확인하기 때문
    # ex) n=6, lost=[5,3] reserve=[4,6] --> 5(최댓값 x)
    # ex) n=6, lost.sort()=[3,5] reserve=[4,6] --> 6(최댓값)
    new_lost.sort()
    
    for i in new_lost:
        if i in new_reserve:
            new_reserve.remove(i)
        elif i-1 in new_reserve:
            new_reserve.remove(i-1)
        elif i+1 in new_reserve:
            new_reserve.remove(i+1)
        else:
            answer-=1
    return answer