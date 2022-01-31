# while 문 제거와, s=s[i+1:] 제거로 시간 단축
def solution(s):

    stack = []

    for i in range(0,len(s)):
        if len(stack)<1:
            stack.append(s[i])
            
        else:
            if stack[-1]==s[i]:
                stack.pop()
            else:
                stack.append(s[i])
        
    return 0 if len(stack)>0 else 1

# def solution(s):

#     stack = []
    
#     # stack에 있는 값과 s[idx]에 해당하는 값이 같으면 없애주는 방식 
#     # --> stack의 길이가 남아있으면 짝지어 제거되지 않은 것이다.
#     # 시간 초과
#     # 22번줄에 잘라주는 것과, 12번 라인에 if문 계속 돌려주는 것이 문제인듯
#     for i in range(0,len(s)):
#         if len(stack)<1:
#             stack.append(s[i])
            
#         else:
#             if stack[-1]==s[i]:
#                 stack.pop()
#                 break
#             else:
#                 stack.append(s[i])
        
#     return 0 if len(stack)>0 else 1