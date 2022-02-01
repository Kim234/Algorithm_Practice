from collections import Counter

def solution(str1, str2):
    answer = 0
    
    # 두 글자씩 나누기
    str1_list,str2_list = [],[]
    
    for i in range(1,len(str1)):
        if str1[i-1].isalpha() and str1[i].isalpha():
            str1_list.append(str1[i-1].upper()+str1[i].upper())
        
    for i in range(1,len(str2)):
        if str2[i-1].isalpha() and str2[i].isalpha():
            str2_list.append(str2[i-1].upper()+str2[i].upper())
            
    # 2번째 풀이 Counter 연산이용
    # |: 합집합 &: 교집합
    str1_counter = Counter(str1_list)
    str2_counter = Counter(str2_list)
    intersection = str1_counter&str2_counter
    union = str1_counter|str2_counter

# # 1번째 풀이 차집합 통해 교집합,합집합 구하기
#     difference = Counter(str1_list) - Counter(str2_list)
#     intersection = Counter(str1_list) - Counter(difference)
#     all_str = []
    
#     for i in str1_list:
#         all_str.append(i)
#     for i in str2_list:
#         all_str.append(i)
        
#     union = Counter(all_str) - Counter(intersection)
    
    
    # list(Counter) ==> 키 값만 리스트 항목으로 변환
    # list(Counter.elements()) ==> 카운터 된 요소만큼 나옴
    # cnt = Counter({'a':2,'b':2})라 가정
    # list(cnt) = ['a','b'] // list(cnt.elements()) = ['a','a','b','b']
    if len(list(intersection.elements())) == 0 and len(list(union.elements())) == 0:
        answer = 1
    
    else:
        answer = len(list(intersection.elements()))/len(list(union.elements()))
    
    return int(answer*65536)