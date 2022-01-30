def solution(record):
    answer = []
    name_dict = {}

    for i in record:
        i_list = i.split(" ")
        
        if i_list[0] == 'Enter' or i_list[0] == 'Change':
            name_dict[i_list[1]] = i_list[2]
        
    
    for i in record:
        i_list = i.split(" ")
        if i_list[0]=="Enter":
            answer.append("%s님이 들어왔습니다."%name_dict[i_list[1]])
        elif i_list[0]=="Leave":
            answer.append("%s님이 나갔습니다."%name_dict[i_list[1]])
            
    
    return answer
