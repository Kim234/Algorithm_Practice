def solution(n):
    n_one_num = one_check(n)
    # print(n_one_num)
    for i in range(n+1,1000001):
        if one_check(i)==n_one_num:
            return i

def one_check(n):
    one_number = 0
    while True:
        if n==1:
            one_number+=1
            break
        elif n==0:
            break
        
        else:
            if n%2==1:
                one_number+=1
            n = n//2
    return one_number

print(bin(78)) #0b1001100 bin(n).count => 4