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

def function(string):
    numbers = list(map(int, string))
    primes = get_prime(max(numbers))
    return list(map(lambda x: x in primes, numbers)).count(True)

a = sys.stdin.readline().replace("\n", "")
b = sys.stdin.readline().replace("\n", "").split(" ")
print(function(b))