import math

def solution(n, words):
    answer = [0,0]
    
    game_arr = [] 
    game_arr.append(words[0])
    
    for i in range(1,len(words)):
        
        # 끝말잇기가 되지 않은 경우와 이미 말했던 단어인 경우
        if game_arr[-1][-1] != words[i][0] or words[i] in game_arr:
            
            if (i+1)%n==0: 
                answer[0] = n
            else:
                answer[0] = (i+1)%n
            
            answer[1] = math.ceil((i+1)/n)
            break
        
        else:
            game_arr.append(words[i])
                
    return answer