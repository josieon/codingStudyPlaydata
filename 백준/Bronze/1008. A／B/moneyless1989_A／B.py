import sys

def function(numbers):
    return int(numbers.split(" ")[0]) / int(numbers.split(" ")[1])

input_ = sys.stdin.readline().replace("\n", "")
print(function(input_))