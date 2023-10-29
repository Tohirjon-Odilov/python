def check_tickets(N, K, M, queries):
    booked_seats = set()
    result = []

    for x, y in queries:
        for seat in range(x, y):
            if seat in booked_seats:
                result.append("1")
                break
        else:
            for seat in range(x, y):
                booked_seats.add(seat)
            result.append("0")

    return "\n".join(result)

input_data = "5 2 40 4\n1 2\n1 4\n2 4"
lines = input_data.strip().split("\n")
N, K, M = map(int, lines[0].split())
queries = [tuple(map(int, line.split())) for line in lines[1:]]

output = check_tickets(N, K, M, queries)
print(output)

