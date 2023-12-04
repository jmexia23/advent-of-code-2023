def check_prize(ticket, nr_tickets):
    numbers_line = ticket.split(':')[1].split("|")
    winning_numbers = numbers_line[0].split()
    ticket_numbers = numbers_line[1].split()
    ticket_winning_numbers = set(winning_numbers) & set(ticket_numbers)
    return len(ticket_winning_numbers)

tickets = open('input.txt', 'r').read().split('\n')
total_tickets = {}
ticket_nr = 0
for ticket in tickets:
    ticket_nr += 1
    total_tickets[ticket_nr] = total_tickets.get(ticket_nr, 0) + 1
    prize = check_prize(ticket, total_tickets[ticket_nr])
    for i in range(1, prize + 1):
        if ticket_nr + i <= len(tickets):
            total_tickets[ticket_nr + i] = (total_tickets.get(ticket_nr + i, 0) +  (total_tickets[ticket_nr]))
sum = 0
for v in total_tickets.values():
    sum += v
print(sum)