import sys

def get_prime(max_number):
    l = [False, False] + [True] * (max_number - 1)
    primes = []
    for idx, x in enumerate(l):
        if x:
            primes.append(idx)
            for t in range(idx, max_number+1, idx):
                l[t] = False
    return primes

def function(N, P):
    primes_small = [x for x in P if x<=N/2]
    primes_big = [x for x in P if x >= N/2]
    for x in reversed(primes_small):
        for y in primes_big:
            if x+y > N: break
            elif x+y == N: return f"{x} {y}"

T = sys.stdin.readline().replace("\n", "")
N = []
for x in range(int(T)):
    N.append(int(sys.stdin.readline().replace("\n", "")))
primes = get_prime(max(N))
for n in N:
    print(function(n, primes))