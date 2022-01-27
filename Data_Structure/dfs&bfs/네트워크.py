def solution(n, computers):
    answer = 0
    
    #그래프 만들기
    graph = {}
    
    for i in range(len(computers)):
        graph[i]=[]
        for j in range(0,n):
            if i!=j:
                if computers[i][j]==1:
                    graph[i].append(j)
    
    # print(list(graph.keys())[0])
    
    while graph:
        connected, need_connect = [], []
        need_connect.append(list(graph.keys())[0])

        while need_connect:
            node = need_connect.pop()
            if node not in connected:
                connected.append(node)
                need_connect.extend(graph[node])
                del graph[node]
        answer+=1
        
    return answer