def bfs(begin, target, words, visited):
    stack = [(begin, 0)]
    while stack:
        # print(stack)
        cur, depth = stack.pop(0)
        # print(cur)
        
        # stack에서 꺼낸 원소가 target과 일치하는지 확인
        if cur == target:
            return depth
        
        for i in range(len(words)):
            if visited[i] == True:
                continue
            cnt = 0
            for a,b in zip(cur, words[i]):
                if a!=b:
                    cnt += 1
            if cnt == 1:
                # print(words[i])
                visited[i] = True
                stack.append((words[i], depth+1))
                
            

def solution(begin, target, words):
    answer = 0
    if target not in words:
        return 0

    visited = [False]*(len(words))

    answer = bfs(begin, target, words, visited)

    return answer