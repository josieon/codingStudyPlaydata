def is_prime(num):
    if num == 1:
        return False

    for i in range(2, num):
        if num % i == 0:
            return False
    return True

for _ in range(int(input())):
    num = int(input())
    
    x, y = num//2, num//2
    
    while x > 0:
        if is_prime(x) and is_prime(y):
            print(x, y)
            break
        else:
            x -= 1
            y += 1