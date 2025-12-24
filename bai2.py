def solution(watering_can, N, M):
    NO_WATER = 0
    WATER = 1
    garden = [[NO_WATER] * N for i in range(N)]
    for i in range(M) :
        can = watering_can[i]
        garden[can[0]][can[1]] = WATER
        for j in range(1,can[2]+1):
            if can[0]+j < N:
                garden[can[0]+j][can[1]] = WATER
            if can[0]-j >= 0:
                garden[can[0]-j][can[1]] = WATER
            if can[1]+j < N:
                garden[can[0]][can[1]+j] = WATER
            if can[1]-j >= 0:
                garden[can[0]][can[1]-j] = WATER
    answer = 0
    for i in range(N):
        for j in range(N):
            if garden[i][j] == NO_WATER:
                answer += 1
    return answer
watering_can1 = [[2,2,2],[0,0,1]]
N1 = 5
M1 = 2
ret1 = solution(watering_can1, N1, M1)
print(ret1)