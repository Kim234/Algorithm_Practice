def solution(p):

    # 1번 수행
    if not p:
        return ""
            
    # 2번 수행
    u, v = separate_str(p)[0], separate_str(p)[1]
    
    # 3번 수행
    if check_str(u) == True:
        return u + solution(v)
    
    # 4번 수행
    else:
        answer = '('
        answer += solution(v)
        answer += ')'
        # 과정 4-4
        for p in u[1:len(u) - 1]:
            if p == '(':
                answer += ')'
            else:
                answer += '('
        
        return answer

# 올바른 괄호인지 체크
def check_str(p):
    
    check_arr = []
    
    for i in p:
        if i=="(":
            check_arr.append(i)
        else:
            if len(check_arr)<1: return False
            
            if check_arr.pop()=='(':
                continue
            else:
                return False
    return True

# 분리
def separate_str(p):

    separate_arr = []
    answer = ''
    
    for i in range(2,len(p)+1):
        if p[:i].count('(')==p[:i].count(')'):
            separate_arr.append(p[:i])
            separate_arr.append(p[i:])
            break
    
    return separate_arr

    