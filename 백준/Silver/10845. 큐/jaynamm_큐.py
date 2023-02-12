import sys

queue = []

n = int(sys.stdin.readline().rstrip())

for _ in range(n):
    cmd = list(map(str, sys.stdin.readline().rstrip().split()))
    
    if cmd[0] == "push":
        queue.append(cmd[1])
    elif cmd[0] == "pop":
        if len(queue) == 0:
            print(-1)
        else:
            pop = queue.pop(0)
            print(pop)
    elif cmd[0] == "size":
        print(len(queue))
    elif cmd[0] == "empty":
        if len(queue) > 0:
            print("0")
        else:
            print("1")
    elif cmd[0] == "front":
        if len(queue) == 0:
            print("-1")
        else:
            print(queue[0])
    elif cmd[0] == "back":
        if len(queue) == 0:
            print("-1")
        else:
            print(queue[-1])