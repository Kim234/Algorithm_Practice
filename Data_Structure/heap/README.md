# π² Algorithm - Heap
![heap](https://user-images.githubusercontent.com/28242121/150344710-440e3a86-4a5e-4a07-b245-fb4adaa7d3b5.png)

## νμ΄λ?
νμ νΉμ ν κ·μΉμ κ°μ§λ νΈλ¦¬λ‘, μ΅λκ°κ³Ό μ΅μκ°μ μ°Ύλ μ°μ°μ λΉ λ₯΄κ² νκΈ°μν΄ κ³ μλ νΈλ¦¬ --> μκ°λ³΅μ‘λ O(nlogn) best,avgλ κ°μ<br>
νμμλ κ°μ₯ μ°μ μμκ° λμ(κ°μ₯ μκ±°λ ν°) λΈλκ° ν­μ λ£¨νΈμ μ€κ² λλ€ <br>
μ΄ λ ν€κ°μ λμκ΄κ³λ λΆλͺ¨/μμκ°μλ§ μ±λ¦½λκ³ , νμ λΈλ κ°μλ μ±λ¦½λμ§ μλλ€ <br>
(μ°μ μμ νλ₯Ό μνμ¬ λ§λ€μ΄μ§ μλ£κ΅¬μ‘°λΌκ³ λ νλ€. - κ°μ₯ μ°μ μμκ° λμ λ°μ΄ν° μ­μ  μ©λ) <br>

* μ΅μ ν: λΆλͺ¨ λΈλμ ν€κ°μ΄ μμ λΈλμ ν€κ°λ³΄λ€ ν­μ μμ ν
* μ΅λ ν: λΆλͺ¨ λΈλμ ν€κ°μ΄ μμ λΈλμ ν€κ°λ³΄λ€ ν­μ ν° ν

<br>


## νμ΄μ¬ heap μλ£κ΅¬μ‘°
νμ΄μ¬μ heapq λͺ¨λ μκ³ λ¦¬μ¦μ μ κ³΅ <br>

### ν ν¨μ νμ©
- heapq.heappush(heap, item): itemμ heapμ μΆκ°
- heapq.heappop(heap) : heapμμ κ°μ₯ μμ μμλ₯Ό pop&λ¦¬ν΄. λΉμ΄μλκ²½μ° indexerror
- heapq.heapify(list) : listλ₯Ό μ¦κ°μ μΌλ‘ heapμΌλ‘ λ³ν
<br>


#### ν μμ± & μμ μΆκ° - heappush/heapify
heapq λͺ¨λμ λ¦¬μ€νΈλ₯Ό μ΅μ νμ²λΌ λ€λ£Έ <br>
μλ μ½λλ heapμ΄λΌλ λΉ λ¦¬μ€νΈλ₯Ό μμ±νκ³  κ° μμλ₯Ό μΆκ°νλ μμμ΄λ€.
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

μ΄λ―Έ μμ±ν΄λ λ¦¬μ€νΈκ° μλ€λ©΄ heapify ν¨μλ₯Ό ν΅ν΄ ν μλ£νμΌλ‘ λ³ν (μκ°λ³΅μ‘λ O(N))
```sh
import heapq
heap = [2,1,3,9,10,12]
heapq.heapify(heap)

print(heap)
```

```sh
* μΆλ ₯κ²°κ³Ό
[1,2,3,9,10,12]
```


#### ν μμ μ­μ  - heappop

heappopν¨μλ κ°μ₯ μμ μμλ₯Ό νμμ μ κ±°ν¨κ³Ό λμμ κ·Έ κ²°κ³Όκ°μ λ¦¬ν΄νλ€.
```sh
result = heapq.heappop(heap)

print(result)
```

μμλ₯Ό μ­μ νμ§ μκ³  κ°μ Έμ€κ³  μΆμΌλ©΄ [0] μΈλ±μ±μ ν΅ν΄ μ κ·Ό
```sh
result = heap[0]

print(result)
```

```sh
* μΆλ ₯κ²°κ³Ό
1
```

#### <<μμ©>> μ΅λ ν λ§λ€κΈ°
```sh
import heapq

nums = [4,1,7,3,8,5]
heap = []

for num in nums:
  heapq.heappush(heap, (-num,num)) #(μ°μ μμ, κ°)

while heap:
  print(heapq.heappop(heap)[1]) # index 1
```

```sh
* μΆλ ₯κ²°κ³Ό
8
7
6
5
4
3
2
1
```

#### <<μμ©>> Kλ²μ§Έ μ΅μκ°/μ΅λκ°
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
* μΆλ ₯κ²°κ³Ό
4
```
<br>

## μΆμ²
https://littlefoxdiary.tistory.com/3 , https://www.daleseo.com/python-heapq/
