def solution(new_id):
    #1단계
    answer = new_id.lower()
    #2단계
    char = "-_."
    answer = ''.join(i for i in answer if i in char or i.isnumeric()==True or i.isalpha()==True)
    #3단계
    while answer.find('..')!=-1:
        answer = answer.replace('..','.')
    
    #4단계
    answer = answer[1:len(answer)] if answer.find('.')==0 and len(answer) > 1 else answer
    answer = answer[:-1] if answer[-1] == '.' else answer
    # len(answer) > 1
    # index는 가장 처음에 .이 나타난 위치
    # answer = answer[0:len(answer)-1] if answer.find('.')==len(answer)-1 else answer
    
    #5단계
    answer = answer+'a' if len(answer)==0 else answer
    
    #6단계
    answer = answer[:15] if len(answer)>15 else answer
    answer = answer[0:len(answer)-1] if answer[-1]=='.' else answer
    
    #7단계
    while len(answer)<3:
        answer+=answer[len(answer)-1]
    return answer