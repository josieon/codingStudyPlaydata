n = int(input())

line, max_index = 0, 0

while n > max_index:
    line += 1
    max_index += line
    
    cur = max_index - n
    
    if line%2 == 0:
        top = line - cur
        bot = cur + 1
    else:
        top = cur + 1
        bot = line - cur
        
print(f"{top}/{bot}")