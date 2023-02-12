n = int(input())
xn = list(map(int, input().split()))

xd = {x:i for i, x in enumerate(sorted(list(set(xn))))}

for x in xn:
    print(xd[x])