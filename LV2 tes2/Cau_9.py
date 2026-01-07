def solution(height):
    count = 0
    for i in range(len(height)):
        height[i].append(51)
    height.append([51]*(len(height[0])+1))
    for i in range(len(height)-1):
        for j in range(len(height[i])-1):
            if height[i][j] < height[i][j-1] and height[i][j] < height[i][j+1] and height[i][j] < height[i-1][j] and height[i][j] < height[i+1][j]:
                count+=1
    return count
height = [[3, 6, 2, 8],
          [7, 3, 4, 2],
          [8, 6, 7, 3],
          [5, 3, 2, 9]]
ret = solution(height)
print(ret)