n = int(input())

for _ in range(n):
    a, b = input().split()
    try:
        print(int(a) // int(b))
    except (ValueError, ZeroDivisionError) as error:
        print(f"Error Code: {error}")

