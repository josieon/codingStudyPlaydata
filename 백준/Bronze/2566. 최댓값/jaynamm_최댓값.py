nums = [list(map(int, input().split())) for _ in range(9)]

max_list = [0, 0, 0]

for i in range(9):
    for j in range(9):
        if max_list[0] <= nums[i][j]:
            max_list = [nums[i][j], i+1, j+1]

print(max_list[0], max_list[1], max_list[2])