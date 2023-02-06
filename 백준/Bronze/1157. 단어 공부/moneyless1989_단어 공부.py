import sys

def function(word):
    result = {}
    dict__ = {}
    for letter in word.upper():
        if letter in result:
            result[letter] += 1
        else:
            result[letter] = 1
    for x in result:
        if result[x] in dict__:
            dict__[result[x]] = "?"
        else: 
            dict__[result[x]] = x
    return dict__[max(dict__)]

input_ = sys.stdin.readline().replace("\n", "")
print(function(input_))