def gcd(a, b):
    while b:
        a, b = b, a%b
    return a

def lcm(a, b):
    return a*b//gcd(a,b)

a, b, L = map(int, input().split())
c = -1

lst = []
lab = lcm(a, b)

for i in range(1, int(L**0.5)+1):
    if L % i == 0:
        lst.append(i)
        lst.append(L//i)
        
lst = sorted(lst)
        
for j in lst:
    if lcm(lab, j) == L:
        c = j
        break
print(c)