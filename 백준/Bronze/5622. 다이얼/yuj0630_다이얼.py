import sys
input = sys.stdin.readline

num = ['ABC', 'DEF', 'GHI', 'JKL', 'MNO', 'PQRS', 'TUV', 'WXYZ']

#answer += len(list)
alpha = list(input())

answer = 0
for i in alpha:
    for j in num:
        if i in j:
            answer += num.index(j) + 3

print(answer)            