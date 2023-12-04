import re 
from collections import namedtuple

Number = namedtuple("Number", ["start", "end", "value"])

def read_lines():
    numbers_per_line=[]
    lines = open('input.txt', 'r').read().split('\n')
    line_nr = 0
    p = re.compile("\d+")
    for line in lines:
        numbers_curr_line=[]
        matches = p.finditer(line)
        for m in matches:
            numbers =tuple()
            numbers_curr_line.append(Number(m.start(), m.end(), int(m.group())))
        line_nr += 1
        numbers_per_line.append(numbers_curr_line)
    line_nr = 0
    sum = 0
    p_2 = re.compile("\*")
    for line in lines:
        matches = p_2.finditer(line)
        for m in matches:
            gear_number = []
            if line_nr > 0:
                for n in numbers_per_line[line_nr - 1]:
                    if ((n.start <= m.start() and n.end >= m.start()) or (n.start == m.end())):
                        gear_number.append(n.value)
            for n in numbers_per_line[line_nr]:
                if (n.end == m.start() or n.start == m.end()):
                        gear_number.append(n.value)
            if line_nr < len(numbers_per_line):
                for n in numbers_per_line[line_nr + 1]:
                    if ((n.start <= m.start() and n.end >= m.start()) or (n.start == m.end())):
                        gear_number.append(n.value)
            if len(gear_number) == 2:
                sum += gear_number[0] * gear_number[1]
        line_nr += 1
    print(sum)

read_lines()