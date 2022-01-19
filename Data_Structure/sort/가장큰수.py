# 모범답안
# 숫자의 길이를 3배로 늘려 정렬
# ex) 9,991 --> 999 991991 
# 문자열 비교연산의 경우, 첫번째 인덱스-다음인덱스 순으로 아스키코드 비교 "999">"991991"
def solution(numbers):
    numbers = list(map(str, numbers))
    numbers.sort(key=lambda x: x*3, reverse=True)
    return str(int(''.join(numbers)))

# 내 풀이 방식 --> 숫자의 맨 앞 자리수, 숫자의 맨 뒤 자리수, 길이의 역수 순으로 정렬
# ex) 1,10,100 -->> 110100
# 하지만 반례로, 28,298이 리스트라면 29828>28298임에도 28298을 출력
# def solution(numbers):
#     answer = ''
#     numbers_str=[str(i) for i in numbers]
#     numbers_list=sorted(numbers_str, key=lambda num:(num[0],num[len(num)-1],1/len(num)),reverse=True)
#     for i in numbers_list:
#         answer+=i
#     return answer