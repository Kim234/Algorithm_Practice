def solution(arr):
    mul = 1
    arr.sort()
    for i in arr:
        mul*=i

    for i in range(max(arr),mul+1):
        for j in arr:
            if i%j == 0:
                if j==arr[-1]:
                    return i
            else:
                break
    # return answer