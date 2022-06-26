t = int(input())
paths = ['n', 'e', 's', 'w']
for _ in range(t):
    commands = input()
    rescued = False
    curr_index = 0
    for command in commands:
        if command == 'R':
            curr_index += 1
        else:
            curr_index -= 1
        if curr_index == 3 or curr_index == -2:
            rescued = True
            break
    if rescued:
        print('YES')
    else:
        print('NO')
