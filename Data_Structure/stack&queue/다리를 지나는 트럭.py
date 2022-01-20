def solution(bridge_length, weight, truck_weights):
    time = 0
    current_truck = [0]*bridge_length
    
    while current_truck:
        current_truck.pop(0)
        time+=1
        if len(truck_weights)>=1:
            if sum(current_truck)+truck_weights[0]<=weight:
                current_truck.append(truck_weights.pop(0))
            else:
                current_truck.append(0)

    return time

# 이미 다 지나간 트럭 past_truck을 지우고 current_truck이 다 비어있을 때만 계산
# current_truck에 bridge_legnth만큼 들어올 수 있는 트럭의 개수를 포함
# 다리 길이 : 2 , 트럭 무게 리스트: [7,4,5,6]
# [0,0] --> [0,7] --> [7,0] --> [0,4] --> [4,5] -->[5,0] -->[0.6] --> [6] 

# def solution(bridge_length, weight, truck_weights):
#     time = 0
#     past_truck = []
#     current_truck = []
#     truck_num = len(truck_weights)
#     while len(past_truck)!=truck_num:
#         current_truck.append(truck_weights.pop(0))
#         # 트럭이 몇 개 더 올라갔는지 체크
#         check=0
#         for i in range(0,bridge_length):
#             time+=1
#             if len(truck_weights)>=1:
#                 if sum(current_truck)+truck_weights[0]<=weight:
#                     check+=1
#                     current_truck.append(truck_weights.pop(0))  
                
#         past_truck.append(current_truck.pop(0))
        
#         for i in range(check):
#             time+=1
#             past_truck.append(current_truck.pop(0))
#         print(past_truck)
        
#     return time+1

## 히든테스트케이스를 통해 놓친 점 발견
# 이 코드는 다리 하나가 빌 때 채우질 못함
# ex) 6kg를 견디는 3m 다리가 있고, [2,3,2]에 해당하는 트럭 무게가 있다고 가정
# 모범답안 [2] 완료x--> [2,3] 완료x-->[3,2] 완료 2 --> [2] 완료 2 3 --> [] 완료 2 3 2
# 내 답안 [2] 완료x --> [2,3] 완료x --> [] 완료 2 3--> [2] 완료 2 3 --> [] 완료 2 3 2