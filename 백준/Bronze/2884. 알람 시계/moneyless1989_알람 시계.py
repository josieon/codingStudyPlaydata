import sys

def function(numbers):
    H, M = numbers[0], numbers[1]
    hour, minute = 0, 0
    if M < 45:
        minute = M + 15
        hour = 23 if H == 0 else H-1
    else:
        hour, minute = H, M-45
    return f"{hour} {minute}"

a = list(map(int, sys.stdin.readline().replace("\n", "").split(" ")))
print(function(a))