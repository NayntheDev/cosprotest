def solution(arr, k):
    answer = 0
    riel_arr=[]
    for i in arr:
        for j in i:
            riel_arr.append(j)
    riel_arr.sort()
    answer=riel_arr[k-1]
    return answer
inp=input()
k=int(input())
arr=eval(inp)
print(solution(arr,k))