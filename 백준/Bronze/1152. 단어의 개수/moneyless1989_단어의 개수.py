import sys

def function(words):
    if words.strip().split(" ") == [""]:
        return 0
    else: return len(words.strip().split(" "))

input_ = sys.stdin.readline().replace("\n", "")
print(function(input_))