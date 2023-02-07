import sys

a = sys.stdin.readline().replace("\n", "")

string = ""
for x in range(1, int(a)+1):
    string += f"{'*'*x}\n"
print(string)