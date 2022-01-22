from itertools import permutations

def solution(numbers):
    
    number_list=[]
    permu_list=[]
    pn_search = []
    # string 분리한 리스트 만들기
    for i in numbers:
        number_list.append(i)
    
    # 숫자의 순열리스트 만들기
    for i in range(1,len(number_list)+1):
        permu_list.append(list(permutations(number_list,i)))
    
    # 순열리스트에 있는 스트링 붙이고 int형으로 바꿔주기
    for i in permu_list:
        for j in range(len(i)):
            number="".join(i[j])
            pn_search.append(int(number))
    
    # 중복 제거
    pn_search = list(set(pn_search))
    
    # 제거할 리스트
    remove_list = []
    
    # 소수가 아니거나, 2보다 작으면 제거 대상
    for i in pn_search:
        if i<2:
            remove_list.append(i)
        else:
            for j in range(2,int((i)**(1/2))+1):
                if i%j==0:
                    remove_list.append(i)
                    break
    for i in remove_list:
        pn_search.remove(i)
        
    return len(pn_search)

# 내 풀이 훨씬 간단하게
# from itertools import permutations

# def solution(n):
#     a = set()
#     for i in range(len(n)):
#         a |= set(map(int, map("".join, permutations(list(n), i + 1))))
#     a -= set(range(0, 2))
#     for i in range(2, int(max(a) ** 0.5) + 1):
#         a -= set(range(i * 2, max(a) + 1, i))
#     return len(a)