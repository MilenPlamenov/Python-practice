while True:
    try:
        a = []
        input_string = []
        days = 0
        while len(a) < 3:
            input_string = input()
            i = input_string.split()
            [a.append(int(j)) for j in i]
        meters_per_day = int(a[0])
        meters_per_night = int(a[1])
        needed_meters = int(a[2])
        days = (needed_meters - meters_per_night - 1) / (meters_per_day - meters_per_night) + 1
        print(int(days))

    except EOFError:
        break
