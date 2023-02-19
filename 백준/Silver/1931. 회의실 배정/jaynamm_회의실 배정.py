n = int(input())

meetings = []

for _ in range(n):
    meetings.append(list(map(int, input().split())))
    
meetings.sort(key = lambda x:(x[1],x[0]))

cnt = 1
now_meeting = meetings[0]

for i in range(1, len(meetings)):
    if now_meeting[1] <= meetings[i][0]:
        now_meeting = meetings[i]
        cnt += 1
        
print(cnt)