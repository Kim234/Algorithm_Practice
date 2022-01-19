#그냥 값으로만 정렬해도 됨.
def solution(phone_book):
    
    phone_book.sort(key=lambda b:(b,len(b)))
    # print(phone_book)
    # phone_list = {idx:num for idx,num in enumerate(phone_book)}
    
    for i in range(0,len(phone_book)-1):
        if phone_book[i+1].find(phone_book[i])==0:
            return False
    return True

#해시 이용 답안
# def solution(phone_book):
# answer = True
# hash_map = {}
# for phone_number in phone_book:
#     hash_map[phone_number] = 0
# for phone_number in phone_book:
#     temp = ""
#     for number in phone_number:
#         temp += number
#         if temp in hash_map and temp != phone_number:
#             answer = False
# return answer