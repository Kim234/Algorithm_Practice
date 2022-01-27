def solution(s):
    s_list = list(map(int,s.split(" ")))
    return str(min(s_list))+" "+str(max(s_list))