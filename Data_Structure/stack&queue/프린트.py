def solution(priorities, location):
    pop_list=[]
    i=0
    while len(pop_list)<=len(priorities):
        # print(pop_list)
        if priorities[i] == max(priorities):
            pop_list.append(i)
            priorities[i]=0
        
        else:
            i=priorities.index(max(priorities))
            pop_list.append(i)
            priorities[i]=0

        if i==len(priorities)-1:
            i=0
        else:
            i+=1    
    return pop_list.index(location)+1


##찾아낸 반례
# ([1,3,9,3,2,3],1) return 4 --> 하지만 이 코드는 return 3