s = [input() for _ in range(5)]

for i in range(max(map(len, s))):
    for j in range(5):
        if i < len(s[j]) and s[j][i]:
            print(s[j][i], end="")