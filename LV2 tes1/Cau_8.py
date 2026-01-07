def solution(name_list):
    answer = 0
    for name in name_list:
        if 'j' in name or 'k' in name:
            answer+=1
    return answer
s=list(input().split())
print(solution(s))