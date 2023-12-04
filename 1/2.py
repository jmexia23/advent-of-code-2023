import re


words_to_look_for = ["one", "two", "three", "four", "five", "six", "seven", "eight", "nine", "1", "2", "3", "4", "5", "6", "7", "8", "9"]
words_to_numbers = {"one":"1", "two":"2", "three":"3", "four":"4", "five":"5", "six":"6", "seven":"7", "eight":"8", "nine":"9"}

def get_value(result):
    if re.search(r'\d', result):
        return result
    else:
        return words_to_numbers[result]


def find_digits(line):
    found = {}
    r_found = {}
    result = ''
    for word in words_to_look_for:
        if (position := line.find(word)) >= 0:
            found[word] = position
        if (r_position := line.rfind(word)) >= 0:
            r_found[word] = r_position
    result += get_value(min(found, key=found.get))
    result += get_value(max(r_found, key=r_found.get))
    return int(result)

lines = open('input.txt', 'r').read().split('\n')
sum = 0
for line in lines:
    sum += find_digits(line)
    
print(sum)
