# 틀린 풀이
# def solution(name):
#     name = list(name)
#     answer = 0
#     i = 0
    
#     while name.count('A') != len(name):
#         if name[i] != 'A':
#             if name[i] <='M':
#                 answer+=ord(name[i])-ord('A')
#             else:
#                 answer+=ord('Z')-ord(name[i])+1
#             name[i] = 'A'
            
#         else:
#             left, right = 1,1
#             for l in range(1,len(name)):
#                 if name[i-l] == 'A': left += 1
#                 else: break

#             for r in range(1,len(name)):
#                 if name[i+r] == 'A': right += 1
#                 else: break

#             if left < right:
#                 answer += left
#                 i -= left
#             else:
#                 answer += right
#                 i += right
            
#     return answer