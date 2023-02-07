import sys

def function(subjects, string):
    numbers = [int(x) for x in string.split(" ")]
    return sum(map(lambda x: x/max(numbers)*100, numbers)) / subjects

a = sys.stdin.readline().replace("\n", "")
b = sys.stdin.readline().replace("\n", "")
print(function(int(a), b))