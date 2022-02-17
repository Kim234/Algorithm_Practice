# 3번문제와 유시
import sys
input=sys.stdin.readline

t=int(input())
for _ in range(t):
    n=int(input())
    match=[6, 2, 5, 5, 4, 5, 6, 3, 7, 6]
    ans=[0, 0, 1, 7, 4, 2, 6, 8, 10, 18, 22]
    ansMax='7'*(n%2)+'1'*(n//2-(n%2))
    if n<=10: 
        print(ans[n], ansMax)
        continue

    ansMin=''
    while n>0:
        n-=7
        if n>=0: ansMin+='8'
        else: n+=7; break

    small={6:6, 2:1, 5:2}
    if n in small: ansMin=str(small[n])+ansMin
    else: 
        if n==1: ansMin='10'+ansMin[1:]
        elif n==3: ansMin='200'+ansMin[2:]
        elif n==4: ansMin='20'+ansMin[1:]

    print(ansMin, ansMax)