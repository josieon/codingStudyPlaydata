import sys

def function(string):
    numbers = [int(x) for x in string.split(" ")]
    return sum(map(lambda x: x**2, numbers)) % 10

a = sys.stdin.readline().replace("\n", "")
print(function(a))