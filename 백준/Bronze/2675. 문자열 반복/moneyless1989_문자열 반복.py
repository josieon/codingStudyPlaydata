import sys

def function(strings):
    number, string = int(strings[0]), strings[1]
    output = ""
    for x in string:
        output += x * number
    return output + "\n"

a = int(sys.stdin.readline().replace("\n", ""))
result = ""
for x in range(a):
    result += function(sys.stdin.readline().replace("\n", "").split(" "))
print(result)
