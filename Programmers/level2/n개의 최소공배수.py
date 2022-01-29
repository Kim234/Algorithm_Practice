def solution(arr):
    mul = 1
    arr.sort()
    for i in arr:
        mul*=i

    for i in range(max(arr),mul+1):
        for j in arr:
            if i%j == 0:
                # arr요소 중 마지막 요소와 같은 요소가 있을 수 있다 ex)[10,17,10] --> 따라서 sort 필요
                if j==arr[-1]:
                    return i
            else:
                break
    # return answer