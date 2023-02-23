n = int(input())
strings = [input() for _ in range(n)]

strs = list(set(strings))
strs.sort(key=lambda x:(len(x), x))

for s in strs:
    print(s)