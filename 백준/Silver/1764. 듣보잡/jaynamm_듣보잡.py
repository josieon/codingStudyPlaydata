n, m = map(int, input().split())
nn = [input() for _ in range(n)]
mm = [input() for _ in range(m)]

dbjob = list(set(nn)&set(mm))
dbjob.sort()

print(len(dbjob))
for name in dbjob:
    print(name) 