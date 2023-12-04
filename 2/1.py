import re

limits_per_color = {"red": 12, "green": 13, "blue": 14}


def check_if_possible(line):
    matches = re.findall(r"\d+?\s(?:blue|red|green)", line)
    for match in matches:
        words = match.split()
        if limits_per_color[words[1]] >= int(words[0]):
            continue
        else:
            return 0
    return(int(re.match(r"Game\s\d+", line.split(":")[0])[0].split()[1]))

lines = open('input.txt', 'r').read().split('\n')
sum = 0
for line in lines:
    sum += check_if_possible(line)
print(sum)