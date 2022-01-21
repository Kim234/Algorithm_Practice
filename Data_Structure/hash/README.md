# 🔑 Algorithm - Hash
![hash](https://user-images.githubusercontent.com/28242121/150476347-5ff21647-2f03-4b1b-8044-d2a04332e7ec.png)

## 해시란?
해시(Hash)란 데이터를 다루는 기법 중 하나 <br>
해시 함수(Hash Function)는 데이터를 효율적으로 관리하기 위해서 임의의 길이의 데이터를 고정된 길이의 데이터로 매핑하는 함수 <br>

## 해시테이블이란?
해시 테이블(Hash Table)은 키(key)와 값(value)이 하나의 쌍을 이루는 데이터 구조 <br>
해시 테이블은 각각의 key 값에 해시함수를 적용해 배열의 고유한 index를 생성하고, 이 index를 활용해 값을 저장하거나 검색 <br>
key 값으로 데이터를 찾을 때 해시 함수를 1번만 수행하면 되므로 매우 빠르게 데이터를 저장/삭제/조회할 수 있다.<u>평균 시간복잡도 O(1)</u> <br>

## 파이썬 hash 자료구조
파이썬은 Dictionary라는 자료구조를 통해 해시를 제공 <br>
### 언제 사용?
- 리스트를 쓸 수 없을 때
리스트는 숫자인덱스를 이용하여 접근한다. (ex)list[1]은 가능하지만, list['a']는 불가능) <br>
인덱스 값을 숫자가 아닌 다른 값 '문자열,튜플'을 사용하려고 할 때 딕셔너리를 사용하면 좋다.<br>

- 빠른 접근/탐색이 필요할 때
딕셔너리 함수의 시간복잡도는 대부분 O(1)이므로 아주 빠른 자료구조이다. <br>

- 집계가 필요할 때
원소의 개수를 세는 문제는 코딩테스트에서 많이 출제되는 문제이다. <br>
이때 해시와, collection 모듈의 Counter 클래스를 사용하면 빠르게 문제 해결이 가능하다. <br>

### Dictionary 활용

#### 🔑Init
{}를 사용하거나 dict함수 호출 시 빈 딕셔너리를 선언할 수 있다 <br>
```sh
# 빈딕셔너리 생성
dict1 ={}
dict2 = dict()

```

```sh
Dog = {
  'name':'동동이',
  'weight':4,
  'height':100,
}

# {'height':100, 'name':'동동이', 'weight':4}
```


#### 🔑Get
Dictionary에서 원소를 가져오는 방법은 두 가지
- [] 사용하기
- get 메소드 이용하기 
<br>

```sh
# [] 기호 사용해 원소 가져오기
dict = {'하이':300, '헬로':180}
dict['헬로'] #180
dict['바이'] #key error

```
get 메소드는 get(key,x)로 사용할 수 있다. 이는 '딕셔너리에 key가 없는 경우, x를 리턴해줘라'라는 뜻이다.

```sh
# get 메소드를 아용해 원소 가져오기 1
# 딕셔너리에 해당 key가 없을때 Key Error 를 내는 대신, 특정한 값을 가져온다.

dict = {'하이': 300, '헬로': 180}
dict.get('동동', 0) # 0
dict.get('헬로',0) #180
```

#### 🔑Set
딕셔너리에 값을 집어넣거나, 값을 업데이트 할 때 []를 사용
<br>

```sh
# 값 집어넣기

dict = {'김철수': 300, 'Anna': 180}
dict['홍길동'] = 100
dict # {'Anna': 180, '김철수': 300, '홍길동': 100}

# 값 수정하기

dict = {'김철수': 300, 'Anna': 180}
dict['김철수'] = 500
dict # {'Anna': 180, '김철수': 500}
```

#### 🔑Delete
특정 key 값을 지울 때에 두 가지 방법을 사용한다.
- del dict_obj[key]
del은 키워드로써, 만약 딕셔너리에 key가 없다면 keyError가 발생
- pop(key[,default])
pop은 메소드로써, pop메소드는 key 값에 해당하는 value를 리턴한다. key가 없다면 두번째 파라미터인 default를 리턴 <br>
만약 default를 설정하지 않았다면 keyError가 발생한다.

<br>

```sh
# del 이용하기 
dict = {'김철수': 300, 'Anna': 180}
del dict['김철수']

dict #{'Anna': 180}
```

```sh
# pop 이용하기 - 키가 있는 경우 대응하는 value 리턴
my_dict = {'김철수': 300, 'Anna': 180}
my_dict.pop('김철수', 180) # 300

# pop 이용하기 2 - 키가 없는 경우 default 리턴
my_dict = {'김철수': 300, 'Anna': 180}
my_dict.pop('홍길동', 180) # 180
```

#### 🔑Iterate
for문을 이용하여 조회할 때 두 가지 방법을 사용한다.
- key로만 순회하기
- key,value 동시 순회하기 (items() 사용)
```sh
# key로만 순회
dict = {'김철수': 300, 'Anna': 180}
for key in dict:
    print(key)
    # 이 경우 value를 찾고 싶으면 dict[key] 와 같이 접근을 따로 해주어야.

'''
김철수
Anna
'''
```

```sh
# key-value 동시 순회

dict = {'김철수': 300, 'Anna': 180}
for key, value in dict.items():
    print(key, value)

'''
김철수 300
Anna 180
'''
```

#### 🔑그 밖에 유용한 팁
- 특정 key가 딕셔너리에 있는지 없는 지 조회 : in 사용
```sh
dict = {'김철수': 300, 'Anna': 180}
print("김철수" in dict) #True
print("김철수" not in dict) # False
```

- key 또는 values만 뽑아내는 방법 : keys(), values()
```sh
# key를 extract - keys 사용

my_dict = {'김철수': 300, 'Anna': 180}
my_dict.keys() # dict_keys(['김철수', 'Anna'])
```

```sh
# value를 extract - values 사용

my_dict = {'김철수': 300, 'Anna': 180}
my_dict.values() # dict_values([300, 180])
```

```sh
# key, value 쌍을 extract - items 사용

my_dict = {'김철수': 300, 'Anna': 180}
my_dict.items() # dict_items([('김철수', 300), ('Anna', 180)])
```

- key 또는 value를 기준으로 정렬하기 : operator 모듈의 itemgetter 사용
```sh
# key 기준으로 정렬 - itemgetter(0) // value 기준으로 정렬-itemgetter(1)
my_dict = {'김철수':300, 'Anna':180}
my_dict_sort= sorted(my_dict.items(),key=operator.itemgetter(1),reverse=True)

my_dict_sort # {'Anna':180,'김철수':300}
```

<br>

### Counter 활용
<u>collections</u> 모듈의 Counter 클래스는 파이썬 기본 구조인 사전(dictionary)를 확장하고 있다.<br>
따라서 사전에서 제공하는 API를 모두 사용할 수 있다.

- 예시 1 : counter 기본
```sh
from collections import Counter

Counter('hello world') # Counter({'l': 3, 'o': 2, 'h': 1, 'e': 1, ' ': 1, 'w': 1, 'r': 1, 'd': 1})
```

- 예시 2 : 포함되어있지 않은 사람 찾기
```sh
import collections

participant = ['leo','marin']
complection = ['leo']
answer = collections.Counter(participant) - collections.Counter(completion)
list(answer) # ['marin']

```

- 예시 3 : 데이터가 많은 순으로 정렬 most_common 메서드 사용
```sh
from collections import Counter

Counter('hello world').most_common() # [('l', 3), ('o', 2), ('h', 1), ('e', 1), (' ', 1), ('w', 1), ('r', 1), ('d', 1)]
```

<br>


## 출처
https://yunaaaas.tistory.com/46 <br>
https://mangkyu.tistory.com/102 <br>
https://www.daleseo.com/python-collections-counter/ <br>
https://hee96-story.tistory.com/48#:~:text=%ED%95%B4%EC%8B%9C(Hash)%20%EB%9E%80%20%EB%8D%B0%EC%9D%B4%ED%84%B0%EB%A5%BC,%EB%A1%9C%20%EB%A7%A4%ED%95%91%ED%95%98%EB%8A%94%20%ED%95%A8%EC%88%98%EC%9D%B4%EB%8B%A4.
