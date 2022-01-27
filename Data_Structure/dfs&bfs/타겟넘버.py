def solution(numbers, target):
    answer = 0
    queue = []
    # numbers의 초기 값을 넣어준다 ex) 1 --> 1과 -1
    queue.append(numbers[0])
    queue.append(-numbers[0])

    # numbers 모든 값이 queue에 들어가도록
    for i in range (1,len(numbers)):
        # queue에 있는 모든 수가 연산할 수 있도록
        for j in range (len(queue)):
            current = queue.pop(0)
            queue.append(current + numbers[i])
            queue.append(current - numbers[i])
    answer = queue.count(target)

    return answer