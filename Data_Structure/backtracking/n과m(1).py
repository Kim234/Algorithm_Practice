# 백트래킹 방식 풀이
# (길을 가다가 이 길이 아닌 것 같으면 왔던 길로 되돌아가 다른 경로로 진행)

n,m = list(map(int,input().split()))
 
s = [] # 재귀함수를 이용하여 m개의 수열을 저장하기 위한 리스트
 
def dfs():

    if len(s)==m:   #리스트에 들어간 수열들이 m개가 되면 리스트에 들어있는 숫자들을 모두 출력하고 함수를 나온다.
        print(' '.join(map(str,s))) 
        return
    
    for i in range(1,n+1): #for문을 이용하여 1부터 n까지 숫자들을 모두 확인
        if i not in s: #리스트 s 중복 여부 확인
            s.append(i) #중복이 아니면 숫자 i를 리스트 s에 넣기
            # print(s)
            dfs() # 현재 s=[1]인 상태에서 다음 숫자를 넣기위하여 가지치기하기(재귀함수)
                  # ex) 만약 n=4, m=2라면 밑과 같은 형태로 진행될 것이다.
                  # s: [1]-> [1,2] -> [1] -> [1,3] -> [1] ->  [1,4]

            s.pop() # 맨 마지막에 있는거빼고 다시
 
dfs()




# 내 풀이
# from itertools import permutations

# n,m = map(int, input().split())

# n_list = [i for i in range(1,n+1)]

# permu = list(permutations(n_list,m))

# for i in permu:
#     tmp =""
#     for j in i:
#         tmp+=str(j)
#         tmp+=" "
#     print(tmp)