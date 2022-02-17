# 내 풀이 - 하나하나 다 쪼개서 만듬
def solution(s):
    answer = []
    
    s = s[1:-1]
    s = s.split("},{")
    s_list = []
    new_s_list = []
    
    for i in s:
        s_list.append(i.replace("{","").replace("}",""))
        
    
    for i in s_list:
        new_s_list.append(i.split(","))
        
    
    new_s_list.sort(key=lambda s:(len(s)))
    
    for i in new_s_list:
        for j in i:
            if int(j) not in answer:
                answer.append(int(j))
        
    return answer

# 다른 사람 풀이 - Counter와 정규식 이용
# \d: 숫자 [0-9]와 같다    +:반복을 의미 ex) 111: 111이 1개 // 없다면, 111: 1이 3개
import re
from collections import Counter
def solution(s):

    s = Counter(re.findall('\d+', s))
    return list(map(int, [k for k, v in sorted(s.items(), key=lambda x: x[1], reverse=True)]))



# 다른 사람 풀이 2 - 내 풀이와 유사하지만, 파싱을 잘함
# lstrip, rstrip 왼쪽,오른쪽 문자열 끝에 해당하는 문자 지워줌
def solution(s):
    answer = []

    s1 = s.lstrip('{').rstrip('}').split('},{')

    new_s = []
    for i in s1:
        new_s.append(i.split(','))

    new_s.sort(key = len)

    for i in new_s:
        for j in range(len(i)):
            if int(i[j]) not in answer:
                answer.append(int(i[j]))

    return answer