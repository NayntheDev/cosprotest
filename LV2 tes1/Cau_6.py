def solution(height, k):
    answer = 0
    for h in height:
        if h > k:
            answer += 1
    return answer
scores=list(map(int,input().split()))
k=int(input())
print(solution(scores,k))