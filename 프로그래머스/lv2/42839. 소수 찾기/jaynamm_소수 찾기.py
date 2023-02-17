from itertools import permutations

def is_prime(n):
    if n == 0 or n == 1:
        return False
    for i in range(2, n):
        if n % i == 0:
            return False
    return True

def solution(numbers):
    answer = 0
    nums = []
    
    for i in range(1, len(numbers)+1):
        nums += list(set(permutations(numbers, i)))
    
    tmp = [int("".join(n)) for n in nums]
    
    for t in set(tmp):
        if is_prime(t):
            answer += 1
    
    return answer