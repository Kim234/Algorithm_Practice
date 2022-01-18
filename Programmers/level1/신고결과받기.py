def solution(id_list, report, k):
    answer = [0 for i in range(len(id_list))]
    #report 중복제거
    report = list(set(report))
    
    #신고를 한 사람/받은사람 다 있는 리스트, 신고를 받은사람 - 신고 당한 횟수 카운트
    report_list = []
    report_pp = {i:0 for i in id_list}
        
    for i in report:
        report_list.append(i.split(' '))
        report_pp[i.split(' ')[1]]+=1
        
    for i in report_list:
        if report_pp[i[1]]>=k:
            answer[id_list.index(i[0])]+=1
            
    return answer

# dictionary 사용 전 효율성 통과 x -- list 자료형은 삽입, 삭제 등에 시간복잡도 O(N)//set과 dictionary는 시간복잡도 O(1)

# def solution(id_list, report, k):
#     answer = [0 for i in range(len(id_list))]
#     report = list(set(report))
#     report_list = []
#     report_user = []
        
#     for i in report:
#         report_list.append(i.split(' '))
#         report_user.append(i.split(' ')[1])
        
#     for i in report_list:
#         if report_user.count(i[1])>=k:
#             answer[id_list.index(i[0])]+=1
            
#     return answer