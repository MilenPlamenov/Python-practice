total_tickets = 0
total_standard_tickets = 0
total_kid_tickets = 0
total_student_tickets = 0

command = input()
while command != "Finish":
    movie_seats = int(input())
    movie_tickets = 0
    while movie_seats > movie_tickets:
        ticket = input()

        if ticket == "standard":
            total_standard_tickets += 1
        elif ticket == "kid":
            total_kid_tickets += 1
        elif ticket == "student":
            total_student_tickets += 1
        else:
            break

        total_tickets += 1
        movie_tickets += 1
    print(f"{command} - {(movie_tickets / movie_seats) * 100:.2f}% full.")
    command = input()


print(f"Total tickets: {total_tickets}")
print(f"{(total_student_tickets / total_tickets) * 100:.2f}% student tickets.")
print(f"{(total_standard_tickets / total_tickets) * 100:.2f}% standard tickets.")
print(f"{(total_kid_tickets / total_tickets) * 100:.2f}% kids tickets.")