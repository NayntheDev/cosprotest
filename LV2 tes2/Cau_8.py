def solution(n, votes):
    cnt=[0]*(n+1)
    for i in votes:
        cnt[i]+=1
    for i in range(0,n+1):
        if cnt[i] > len(votes)//2:
            return i
    return -1
n1 = 3
votes1 = [1, 2, 1, 3, 1, 2, 1]
ret1 = solution(n1, votes1)
print(ret1)
n2 = 2
votes2 = [2, 1, 2, 1, 2, 2, 1]
ret2 = solution(n2, votes2)
print(ret2)