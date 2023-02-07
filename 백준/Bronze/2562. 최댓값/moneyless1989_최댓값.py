import sys

a, b = 0, 0
for x in range(9):
    tmp = int(sys.stdin.readline().replace("\n", ""))
    if a < tmp:
        a = tmp
        b = x+1
print(f"{a}\n{b}")