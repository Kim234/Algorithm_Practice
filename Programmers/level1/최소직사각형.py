def solution(sizes):

    #가로의 최대 길이와 세로의 최대 길이를 찾는다
    sizes_width = sorted(sizes,key=lambda size:size[0], reverse=True)[0][0]
    sizes_length = sorted(sizes,key=lambda size:size[1], reverse=True)[0][1]
    
    #모두 최대인 쪽에, 크기가 큰 사이즈가 가도록 회전
    if sizes_width>sizes_length:
        for i in range(len(sizes)):
            if sizes[i][0]<sizes[i][1]:
                tmp = sizes[i][0]
                sizes[i][0] = sizes[i][1]
                sizes[i][1] = tmp
    else:
        for i in range(len(sizes)):
            if sizes[i][0]>sizes[i][1]:
                tmp = sizes[i][0]
                sizes[i][0] = sizes[i][1]
                sizes[i][1] = tmp
    
    #가로 최대와 세로 최대끼리 곱한게 답
    max_sizes_width = sorted(sizes,key=lambda size:size[0], reverse=True)[0][0]
    max_sizes_length = sorted(sizes,key=lambda size:size[1], reverse=True)[0][1]
    return max_sizes_width*max_sizes_length

#다른사람 코드 -- 가장 최대 사이즈 * 최소 중 최대 사이즈(ex)[10,20],[15,30] --> 30 x (10,15)중 최소 10)
# def solution(sizes):
#     return max(max(x) for x in sizes) * max(min(x) for x in sizes)