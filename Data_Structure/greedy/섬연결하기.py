# kruskal algorithm 이용 - 네트워크 정점을 최소비용으로 연결
# 무조건 최소 간선 선택(사이클 형성만 안되게)
def solution(n, costs):
    ans = 0
    costs.sort(key = lambda x: x[2]) # cost 기준으로 오름차순 정렬
    routes = set([costs[0][0]]) # 집합
    while len(routes)!=n:
        for i, cost in enumerate(costs):
            if cost[0] in routes and cost[1] in routes:
                continue
            if cost[0] in routes or cost[1] in routes:
                routes.update([cost[0], cost[1]])
                ans += cost[2]
                costs[i] = [-1, -1, -1]
                break
    return ans


# dfs와 greedy 기법으로 풀려고 했지만 실패
# def solution(n, costs):
#     answer = 0
    
#     graph = {}
    
#     for i in range(n):
#         graph[i] = []
        
#     for i in costs:
#         graph[i[0]].append((i[1],i[2]))
#         graph[i[1]].append((i[0],i[2]))
        
#     for i in graph.keys():
#         graph[i].sort(key=lambda x:(x[1],x[0]))
        
#     while graph:
#         connected, need_connect = [],[]
#         need_connect.append(list(graph.keys())[0])
        
#         while need_connect:
#             node = need_connect.pop()
#             if node not in connected:
#                 connected.append(node)
#                 need_connect.append(graph[node][0][0])
#                 answer+=graph[node][0][1]                    
#                 del graph[node][0]
    
#     print(graph)
        
    
#     return answer