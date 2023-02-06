import sys

def function(string):
    numbers = [int(x) for x in string.split(" ")]
    if numbers[0] == numbers[1]: return "=="
    else: return ">" if numbers[0] > numbers[1] else "<"

b = sys.stdin.readline().replace("\n", "")
print(function(b))