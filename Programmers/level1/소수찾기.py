def solution(n):
    num=set(range(2,n+1))
    for i in range(2,n+1):
        if i in num:
            num-=set(range(2*i,n+1,i))
    return len(num)

#에라토스테네스의 체 구현
#어떤 숫자의 배수이면 빼는 공식