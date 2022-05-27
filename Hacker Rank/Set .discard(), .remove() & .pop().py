
n = int(input())
s = set(map(int, input().split()))

commands = int(input())

for _ in range(commands):
    command = input().split()
    if command[0] == "pop":
        try:
            s.pop()
        except KeyError:
            pass
    elif command[0] == "remove":
        try:
            s.remove(int(command[1]))
        except KeyError:
            pass
    else:
        s.discard(int(command[1]))

print(sum(s))




# 9
# 1 2 3 4 5 6 7 8 9
# 10
# pop
# remove 9
# discard 9
# discard 8
# remove 7
# pop
# discard 6
# remove 5
# pop
# discard 5