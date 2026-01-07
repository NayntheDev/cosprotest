def solution(price, money):
    answer = 0
    if sum(price) - money <= 0:
        answer = sum(price) - money
    else:
        answer= 1
    return answer*-1
scores=list(map(int,input().split()))
k=int(input())
print(solution(scores,k))