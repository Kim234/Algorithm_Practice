# 🔍 Algorithm - DFS/BFS
![dfs](https://user-images.githubusercontent.com/28242121/150627600-e7035fef-12f8-47e8-b083-b2576135d082.png)
![bfs](https://user-images.githubusercontent.com/28242121/150627592-bfdab901-4f32-4a62-8ed6-2c3e9021039f.png)

## DFS/BFS란?
그래프를 탐색하는 방법은 대표적으로 DFS(깊이 우선 탐색)와 BFS(너비 우선 탐색)가 있다.<br>

### 1. 깊이 우선 탐색(DFS, Depth-First Search)
임의의 노드에서 시작해서 다음 브랜치로 넘어가기 전에 해당 브랜치를 완벽하게 탐색하며 모든 노드를 탐색하는 방법 <br>

- stack 자료 구조를 사용한다.
- 탐색을 할 때, 시작 노드를 스택에 쌓는다.
- 이렇게 하면, 모든 노드를 방문하기 전까지 계속해서 스택이 쌓인다.
- 방문하지 않은 자손 노드가 없으면 스택에서 최상단 노드를 꺼낸다.

### 2. 너비 우선 탐색(BFS, Breadth-First Search)
임의의 노드에서 시작해서 인접한 노드를 먼저 탐색하며 모든 노드를 탐색하는 방법<br>

- queue 자료구조를 사용한다. (python deque 사용 가능)
- 탐색을 시작하면, 시작노드를 큐에 넣고 방문 처리를 한다.
- 큐에 더이상 노드가 없을 때까지 큐에서 가장 먼저 들어온 노드를 빼고, 그 노드의 인접 노드를 탐색한다.
- 모든 노드가 방문 처리될 때까지 3번과정을 반복한다.

<br>

## 파이썬 DFS/BFS
예시 코드는 위의 사진의 그래프를 파이썬의 딕셔너리 형태로 표현한 것이다. 
```sh
graph = {
    'A': ['B', 'C'],
    'B': ['A', 'D'],
    'C': ['A', 'G', 'H', 'I'],
    'D': ['B', 'E', 'F'],
    'E': ['D'],
    'F': ['D'],
    'G': ['C'],
    'H': ['C'],
    'I': ['C', 'J'],
    'J': ['I']
}
```

### DFS(깊이 우선 탐색) 구현
```sh
def dfs(graph, start):
  visited, need_visit = [], []

  need_visit.append(start)

  while need_visit:
    node = need_visit.pop()
    if node not in visited:
      visited.append(node)
      if node in graph: # 사실 node는 무조건 graph에 있으니 IF문 필요 X
        need_visit.extend(graph[node])

  return visited
```

우선 방문한 노드(visited)와 방문해야 할 노드들(need_visit)을 나타낼 리스트 두 개를 초기화해준다.<br>
그리고 탐색을 시작할 노드를 need_visit에 append해준다.<br>
이후에 while문을 반복하면서 탐색을 반복한다.<br>
need_visit.pop()을 통해 node를 할당 받고, 해당 node가 visited에 존재하지 않으면 visited에 추가해준다 <br>
그 후 need_visit에 추가로 탐색해야 될 node를 need_visit.extend(graph[node])이 구문으로 추가해준다.

```sh
# 탐색결과
['A','C','I','J','H','G','B','D','F','E']
```

```sh
# append와 extend 차이점
x = ['Tick','Tock']
y = ['Ping','Pong']
x.append(y) # ['Tick','Tock','['Ping','Pong']]
x.extend(y) # ['Tick','Tock','Ping','Pong']
```

### BFS(너비 우선 탐색) 구현
```sh
def dfs(graph, start):
  visited, need_visit = [], []

  need_visit.append(start)

  while need_visit:
    node = need_visit.pop(0)
    if node not in visited:
      visited.append(node)
      if node in graph:
        need_visit.extend(graph[node])

  return visited
```
DFS의 코드와 비교하여 다른 점은 pop()이 pop(0)으로 바뀐 점 밖에 없다. (dfs - stack // bfs - queue)

```sh
# 탐색결과
['A','B','C','D','G','H','I','E','F','J']
```
<br>

## 출처
https://honggom.tistory.com/60
