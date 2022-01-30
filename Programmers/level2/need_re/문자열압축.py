def solution(s):

    L = []
    
    # 문자열 길이가 1개인건 1개만 그냥 1
    if len(s) == 1:
        return 1
    
   # 반복이 되는 것이기 때문에 절반만 검증
    for i in range(1, len(s)//2 + 1):
        arr = ""
        cnt = 1
        tmp = s[:i]

        # 1개부터 절반까지 반복되는 값을 검증
        for j in range(i, len(s), i):
            # print(s[j:i+j])
            if s[j:i+j] == tmp:
                cnt += 1
            else:
                # 반복과 다른 값을 만났을 때
                if cnt == 1:
                    arr += tmp
                    tmp = s[j:i+j]
                else:
                    arr += str(cnt) + tmp
                    tmp = s[j:i+j]
                    cnt = 1
        # 마지막까지 같은 경우를 검증하기 위함
        if cnt == 1:
            arr += tmp
        else:
            arr += str(cnt) + tmp
            
        print(arr)
        L.append(len(arr))


    return min(L)