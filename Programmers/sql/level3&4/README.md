# ✔️ SQL JOIN
![join 방식](https://user-images.githubusercontent.com/28242121/152283566-52947b65-f72d-4b20-b38b-8bdc5d417f9b.png)

## JOIN이란?
두 개 이상의 테이블을 서로 연결하여 데이터를 검색할 때 사용하는 방법<br>
두 개의 테이블을 마치 하나의 테이블인 것처럼 보여준다.
<br>

### 1. 내부조인(Inner Join)
```sh
1) 
SELECT 조회할 컬럼
FROM 테이블1, 테이블2
[WHERE 조건문]

2)
SELECT 조회할 컬럼
FROM 테이블1
JOIN 테이블2
ON 테이블1.컬럼=테이블2.컬럼
[WHERE 추가조건]
```
기준 테이블과 조인 테이블 모두에 조인 컬럼 데이터가 존재해야 조회됨(ON절)
![INNER](https://user-images.githubusercontent.com/28242121/152287968-a24079f0-41e5-4dab-b394-7c6716619ca4.png)
<br>

### 2. 자연조인(Natural Join)
```sh
SELECT 조회할 컬럼
FROM 테이블1
NATURAL JOIN 테이블2
[WHERE 조건문]
```
- 내부 조인에 속함
- 두 테이블에서 동일한 컬럼명을 갖는 컬럼은 모두 조인이 된다.
- 두 테이블이 동시에 가지고 있는 컬럼의 값이 전부 같은 것만 골라냄 (동일한 이름, 타입)
- 기준 테이블과 조인 테이블 모두에 데이터가 존재해야 조회됨
- Inner Join에서 조건문 추가하여 같은 결과값을 얻을 수 있음


![natural](https://user-images.githubusercontent.com/28242121/152288315-485274a6-55ff-42c4-ac2c-b5433e2e8c08.png)

<br>

## 3. 전체 외부 조인(Full Outer Join)

```sh
SELECT 조회할 컬럼
FROM 테이블1
FULL OUTER JOIN 테이블2
ON 조건문
[WHERE 추가조건문]

```

- 공통된 부분만 골라 결합하는 Inner Join과 다르게 공통되지 않은 행도 유지한다.
- 이때 두 테이블 모두의 값을 유지하면 Full Outer Join
- MySQL에서는 FULL OUTER JOIN을 지원하지 않으므로 LEFT OUTER JOIN 결과와 RIGHT OUTER JOIN결과를 UNION하여 사용해야 함

![full](https://user-images.githubusercontent.com/28242121/152288659-c736186c-8ade-4fc0-bc5d-61e9d8da1c82.png)

<br>

### 4. Left Outer Join(=Left Join)

```sh
SELECT 조회할 컬럼
FROM 기준테이블1
LEFT OUTER JOIN 테이블2
ON 조건문
[WHERE 추가조건문]
```
왼쪽 테이블을 기준으로 일치하는 행만 결합되고, 일치하지 않는 부분은 NULL값으로 채워짐.

![left](https://user-images.githubusercontent.com/28242121/152288867-c6f72990-c250-4a85-b16a-2e249174d99b.png)

<br>

### 5. Right Outer Join(=Right Join)
```sh
SELECT 조회할 컬럼
FROM 테이블1
RIGHT OUTER JOIN 기준테이블2
ON 조건문
[WHERE 추가조건문]
```
오른쪽 테이블을 기준으로 일치하는 행만 결합되고, 일치하지 않는 부분은 NULL값으로 채워짐.
![right](https://user-images.githubusercontent.com/28242121/152289309-bd9d4353-5767-484e-aaa2-8307348005f8.png)

<br>

### 6. Cross Join
```sh
1)
SELECT 조회할컬럼
FROM 테이블1, 테이블2

2)
SELECT 조회할컬럼
FROM 테이블1
JOIN 테이블2

3)
SELECT 조회할컬럼
FROM 테이블1
CROSS JOIN 테이블2
```
- 곱집합
- 두 테이블 데이터의 모든 조합
- 테이블 1의 row * 테이블2의 row 개수만큼의 row를 가진 테이블 생성

![cross](https://user-images.githubusercontent.com/28242121/152289614-435d365c-d944-4df1-a4b9-8428cf9ea1ef.png)

<br>

## 출처
https://doh-an.tistory.com/30
