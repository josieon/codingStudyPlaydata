x = int(input())
sum = 0

for _ in range(int(input())):
    # a = 가격 / b = 개수
    a, b = map(int, input().split())
    
    # 금액 = 가격 * 개수
    price = a*b
    
    sum += price

if x == sum:
    print("Yes")
else:
    print("No")