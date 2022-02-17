# 3번문제와 유사

T=int(input())
k=int(input())
L=[[0,0]] #[금액,동전가지수]
for i in range(k):
    L.append(list(map(int,input().split())))
L.sort()
# print(L)
dp=[[0 for j in range(T+1)] for i in range(k+1)]
for i in range(k+1):
    dp[i][0]=1

# print(L)
# i번째 동전까지 사용
for i in range(1,k+1):
    # print(L[i],"금액,가용개수")
    # i번째 동전을 num번 사용
    for num in range(L[i][1]+1):
        # print(num,"번사용했을때")
        for j in range(T+1):
            temp=j+num*L[i][0]
            if temp==0:
                continue
            if temp<T+1:
                dp[i][temp]+=dp[i-1][j]
            else:
                break

print(dp[k][T])