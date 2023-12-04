
def check_prize(line):
    numbers_line = line.split(':')[1].split("|")
    winning_numbers = numbers_line[0].split()
    ticket_numbers = numbers_line[1].split()
    ticket_winning_numbers = set(winning_numbers) & set(ticket_numbers)
    return int((2 ** (len(ticket_winning_numbers) - 1)))

lines = open('test_input.txt', 'r').read().split('\n')
sum = 0
for line in lines:
    sum += check_prize(line)
print(sum)