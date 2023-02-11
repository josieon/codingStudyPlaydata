apb = ['c=', 'c-', 'dz=', 'd-', 'lj', 'nj', 's=', 'z=']
s = input()

for a in apb:
    if a in s:
        s = s.replace(a, "*")
        
print(len(s))