def solution(n,a,b):
    answer = 1
    
    if a<b:
        tmp = a
        a = b
        b = tmp

    while True:
        if a%2==0 and b%2!=0 and a-b==1:
            break

        if a%2==0:
            a=a//2
        else:
            a=(a+1)//2

        if b%2==0:
            b=b//2
        else:
            b=(b+1)//2
            
        answer+=1
        
    return answer

# a,b 중 큰 수가 짝수여야 맞붙게 됨 ex) 1,2는 맞붙고/ 4,5는 맞붙지 않는다.
# def solution(n,a,b):
#     answer = 1

#     while abs(a-b) !=1:
#         if a%2==0:
#             a=a//2
        
#         else:
#             a=(a+1)//2
        
#         if b%2==0:
#             b=b//2
            
#         else:
#             b=(b+1)//2
            
#         answer+=1

#     return answer

# 다른 사람 풀이 - 내 방식과 똑같은데 쉽게 품 (큰 수가 짝수, 작은 수가 홀수여야하고, 둘이 1차이 나야 함)
# def solution(n,a,b):
#     answer = 0
#     while a != b:
#         answer += 1
#         a, b = (a+1)//2, (b+1)//2

#     return answer