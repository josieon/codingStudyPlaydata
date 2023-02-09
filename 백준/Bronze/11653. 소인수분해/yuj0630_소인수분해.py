n = int(input())
cnt = 2
if n != 0:
    for i in range(n):
        while n % cnt == 0:
            n = n//cnt
            print(cnt)
        else:
            cnt += 1