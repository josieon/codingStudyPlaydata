a, b, v = map(int, input().split())
n =(v-b)//(a-b)
if (v-b) % (a-b):
    print(n+1)
else: 
    print(n)
    