from collections import Counter


input_string = input()

while input_string != "0":
    try:
        n = int(input_string)
        all_sheep = []

        for _ in range(n):
            current_sheep = input().split()
            all_sheep.append(' '.join(sorted(current_sheep)))
        b = Counter(all_sheep)
        print(b.most_common(1)[0][1])
        input_string = input()
    except EOFError:
        break

# working


