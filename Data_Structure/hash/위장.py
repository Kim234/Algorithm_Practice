# 나올 수 있는 조합 수
# 각 옷의 종류에 해당되는 옷의 개수+1를 곱한 후, 마지막 -1
def solution(clothes):
    answer = 1
    cloth_comb={i[1]:[] for i in clothes}
    for i in clothes:
        cloth_comb[i[1]].append(i[0])
        
    for i in cloth_comb:
        answer*=len(cloth_comb[i])+1
    answer-=1
    return answer