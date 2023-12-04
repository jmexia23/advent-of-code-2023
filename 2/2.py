import re
from math import prod

def get_power(line):
    matches = re.findall(r"\d+?\s(?:blue|red|green)", line)
    max_per_color = {"red": 0, "green": 0, "blue": 0}
    for match in matches:
        words = match.split()
        if max_per_color[words[1]] < int(words[0]):
            max_per_color[words[1]] = int(words[0])
    
    return prod(max_per_color.values())


lines = open('input.txt', 'r').read().split('\n')
sum = 0
for line in lines:
    sum += get_power(line)
print(sum)