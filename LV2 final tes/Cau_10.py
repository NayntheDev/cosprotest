# đề bài câu 10 trong đề bị sai, đề chuẩn của nó là cho 1 mảng, tìm số lượng phần tử x trong mảng đó sao cho tồn tại phần tử x/2 trong mảng
# vd: [8,4,2] là 2 vì 8 có ptu 4 và 4 có ptu 2
def solution(arr):
    answer = 0
    for i in arr:
        if i/2 in arr:
            answer += 1
    return answer
arr = [4, 8, 3, 6, 7]
ret = solution(arr)
print(ret)