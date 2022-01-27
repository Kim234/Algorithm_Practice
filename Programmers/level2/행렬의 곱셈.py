def solution(arr1, arr2):
    answer = []
    
    # arr2 같은 열인 것끼리 묶기 ex)[[1,2],[3,4]] -->[[1,3],[2,4]]
    arr2_col = []
    for i in range(len(arr2[0])):
        tmp = []
        for j in range(len(arr2)):
            tmp.append(arr2[j][i])
        arr2_col.append(tmp)
        
    for a1 in arr1:
        tmp = []
        for a2 in arr2_col:
            tmp_add = 0
            for i in range(len(arr1[0])):
                tmp_add += a1[i]*a2[i]
            tmp.append(tmp_add)
        answer.append(tmp)
    return answer

# a=[[1,2],[3,4]]
# print(list(zip(*a))) --> [[1,3],[2,4]]
# * <<- unzip 함수: zip을 풀어주는 함수 아래 예시와 유사
# print(list(zip(*[('Alice', 'Bob'),('Anna', 'Jon')]))) 
# [('Alice', 'Anna'), ('Bob', 'Jon')]