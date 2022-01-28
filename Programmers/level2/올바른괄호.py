def solution(s):

    open_list = []
    
    for i in s:
        if i =='(':
            open_list.append(i)
        
        else:
            if len(open_list)==0:
                return False
        
            else:
                open_list.pop()
            
    return True if len(open_list)==0 else False