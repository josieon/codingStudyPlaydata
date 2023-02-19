exp = input().split("-")
res = []

for e in exp:
    tmp = sum(list((map(int, e.split("+")))))
    res.append(tmp)
    
result = res[0]

for i in range(1, len(res)):
    result = result - res[i]
    
print(result)