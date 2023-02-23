import sys

def function(numbers):
    mean = round(sum(numbers)/len(numbers))
    median = numbers[len(numbers)//2]
    if len(numbers) == 1:
        mode = numbers[0]
    else:
        counting = {}
        for x in numbers:
            if x not in counting:
                counting[x] = 1
            else:
                counting[x] += 1
        counted = sorted(counting.items(), key=lambda x: (x[1], -x[0]), reverse=True)[:2]
        mode = counted[0][0] if counted[0][1] > counted[1][1] else counted[1][0]
    range_ = numbers[-1] - numbers[0]
    return f"{mean}\n{median}\n{mode}\n{range_}"

N = int(sys.stdin.readline().replace("\n", ""))
numbers = []
for _ in range(N):
    numbers.append(int(sys.stdin.readline().replace("\n", "")))
print(function(sorted(numbers)))