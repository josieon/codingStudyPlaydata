import sys

def function(string):
    return max(map(int, "".join([x for x in reversed(string)]).split(" ")))

a = sys.stdin.readline().replace("\n", "")
print(function(a))