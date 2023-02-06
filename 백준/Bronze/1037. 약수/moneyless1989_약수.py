import sys

def function(numbers):
    divs = sorted([int(x) for x in numbers.split(" ")])
    return divs[0] * divs[-1]

a = int(sys.stdin.readline())
b = sys.stdin.readline().replace("\n", "")
print(function(b))