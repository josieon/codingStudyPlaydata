x = int(input())
stk = [64, 32, 16, 8, 4, 2, 1]

cnt = 0

for i in range(len(stk)):
    if stk[i]<= x & x != 0:
        cnt += 1
        x -= stk[i]
        
print(cnt)