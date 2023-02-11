import math

n = int(input())

for i in range(n):
    x1, y1, r1, x2, y2, r2 = map(int, input().split())
    
    # 두 원의 중심의 거리
    d = math.sqrt((x1-x2)**2 + (y1-y2)**2)
    
    # 두 원의 반지름과 거리가 0일 경우, 두 원이 일치 = 무한대
    if d == 0 and r1 == r2:
        print(-1)
    # 1) 두 원의 반지름의 합이 거리와 같은 경우, 원 밖의 한 점에서 만나는 경우 (외접)
    # 2) 두 원의 반지름의 차가 거리와 같은 경우, 원 안의 한 점에서 만나는 경우 (내접)
    elif abs(r1-r2) == d or r1+r2 == d:
        print(1)
    # 두 원의 반지름의 차가 거리보다 작고 두 원의 반지름의 합보다 큰 경우, 두 점에서 만다는 경우
    elif abs(r1-r2) < d and r1+r2 > d:
        print(2)
    else:
        print(0)
