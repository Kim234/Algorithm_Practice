# 🌲 Algorithm - Heap
![heap](https://user-images.githubusercontent.com/28242121/150344710-440e3a86-4a5e-4a07-b245-fb4adaa7d3b5.png)

## 힙이란?
힙은 특정한 규칙을 가지는 트리로, 최댓값과 최솟값을 찾는 연산을 빠르게 하기위해 고안된 트리 --> 시간복잡도 O(nlogn) best,avg도 같음<br>
힙에서는 가장 우선순위가 높은(가장 작거나 큰) 노드가 항상 루트에 오게 된다 <br>
(우선순위 큐를 위하여 만들어진 자료구조라고도 한다. - 가장 우선순위가 높은 데이터 삭제 용도) <br>

* 최소 힙: 부모 노드의 키값이 자식 노드의 키값보다 항상 작은 힙
* 최대 힙: 부모 노드의 키값이 자식 노드의 키값보다 항상 큰 힙

<br>


## 파이썬 heap 자료구조
파이썬은 heapq 모듈 알고리즘을 제공 <br>

### 힙 함수 활용
- heapq.heappush(heap, item): item을 heap에 추가
- heapq.heappop(heap) : heap에서 가장 작은 원소를 pop&리턴. 비어있는경우 indexerror
- heapq.heapify(list) : list를 즉각적으로 heap으로 변환
<br>


#### 힙 생성 & 원소 추가 - heappush/heapify
heapq 모듈은 리스트를 최소 힙처럼 다룸 <br>
아래 코드는 heap이라는 빈 리스트를 생성하고 각 원소를 추가하는 예시이다.
```sh
import heapq
heap = []
heapq.heappush(heap,2)
heapq.heappush(heap,1)
heapq.heappush(heap,3)
heapq.heappush(heap,9)
heapq.heappush(heap,10)
heapq.heappush(heap,12)

print(heap)
```

이미 생성해둔 리스트가 있다면 heapify 함수를 통해 힙 자료형으로 변환 (시간복잡도 O(N))
```sh
import heapq
heap = [2,1,3,9,10,12]
heapq.heapify(heap)

print(heap)
```

```sh
* 출력결과
[1,2,3,9,10,12]
```


#### 힙 원소 삭제 - heappop

heappop함수는 가장 작은 원소를 힙에서 제거함과 동시에 그 결과값을 리턴한다.
```sh
result = heapq.heappop(heap)

print(result)
```

원소를 삭제하지 않고 가져오고 싶으면 [0] 인덱싱을 통해 접근
```sh
result = heap[0]

print(result)
```

```sh
* 출력결과
1
```

#### <<응용>> 최대 힙 만들기
```sh
import heapq

nums = [4,1,7,3,8,5]
heap = []

for num in nums:
  heapq.heappush(heap, (-num,num)) #(우선순위, 값)

while heap:
  print(heapq.heappop(heap)[1]) # index 1
```

```sh
* 출력결과
8
7
6
5
4
3
2
1
```

#### <<응용>> K번째 최소값/최대값
```sh
import heapq

def kth_smallest(nums,k):
  heap = []
  for num in nums:
    heapq.heappush(heap, num)
   
  kth)min = None
  for _ in range(k):
    kth_min = heapq.heappop(heap)
  return kth_min
  
print(kth_smallest(([4,1,7,3,8,5],3))
```

```sh
* 출력결과
4
```
<br>

## 출처
https://littlefoxdiary.tistory.com/3 , https://www.daleseo.com/python-heapq/
