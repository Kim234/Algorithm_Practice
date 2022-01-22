def solution(brown, yellow):
    answer = []
    length = 3
    
    # brown 갯수는 width*2+(length-2)*2
    # yellow 갯수는 (width-2)*(length-2)
    while True:
        width = int(brown/2)+2-length
        
        if (width-2)*(length-2)==yellow:
            answer.append(width)
            answer.append(length)
            break
        else:
            length+=1
            continue
        
    return answer