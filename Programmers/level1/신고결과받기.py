def solution(id_list, report, k):
    answer = [0 for i in range(len(id_list))]
    report = list(set(report))
    report_list = []
    report_user = []
        
    for i in report:
        report_list.append(i.split(' '))
        report_user.append(i.split(' ')[1])
        
    for i in report_list:
        if report_user.count(i[1])>=k:
            answer[id_list.index(i[0])]+=1
            
    return answer