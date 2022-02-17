# 2번문제와 유사

from collections import deque
from sys import stdin

n, m = map(int, stdin.readline().split())

graph = []
for _ in range(n):
    graph.append(list(map(int, stdin.readline().strip())))
# print("bfs 적용 전",visit)
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def bfs():
    queue = deque()
    queue.append([0, 0, 1])
    visit = [[[0] * 2 for _ in range(m)] for _ in range(n)]
    visit[0][0][1] = 1 # 벽을 한번 부술 수 있는 상태에서 시작
    
    while queue:
        x, y, w = queue.popleft()
        if x == n-1 and y == m-1:
            return visit[x][y][w]
        for i in range(4):
            xx = x + dx[i]
            yy = y + dy[i]
            if 0 <= xx < n and 0 <= yy < m:
                if graph[xx][yy] == 1 and w == 1: # 벽을 만나고 벽을 한번 부술 수 있는 경우
                    visit[xx][yy][0] = visit[x][y][w] + 1
                    queue.append([xx, yy, 0])
                elif graph[xx][yy] == 0 and visit[xx][yy][w] == 0: # 벽이 없고 방문한적이 없는 경우
                    visit[xx][yy][w] = visit[x][y][w] + 1
                    queue.append([xx, yy, w])
            # print(visit)
    return -1

print(bfs())