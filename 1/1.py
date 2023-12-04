import re


def find_digits(line):
    result = ''
    digits = re.findall(r'\d', line)
    result += digits[0]
    result += digits[-1]
    return int(result)



lines = open('input.txt', 'r').read().split('\n')
sum = 0
for line in lines:
    sum += find_digits(line)
    
print(sum)

