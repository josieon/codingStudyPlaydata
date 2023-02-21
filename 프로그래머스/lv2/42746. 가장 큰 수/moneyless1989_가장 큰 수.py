def solution(numbers):
    strings = list(map(str, numbers))
    times = len(str(max(numbers)))
    strings.sort(key=lambda x: x*times, reverse=True)
    return str(int(''.join(strings)))