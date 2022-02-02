def solution(s):
    
    numbers_zero = 0
    cnt = 0
    
    while s !="1":
        numbers_zero += s.count("0")
        len_one = s.count("1")
        s = ''
        
        while True:
            if len_one==1:
                s+='1'
                break
            s += str(len_one%2)
            len_one = len_one//2
                
        s = s[::-1]
        cnt +=1
            
    return [cnt,numbers_zero]
