n = int(input())

for i in range(n):
    command = input().split()
    price_for_one_chocolate = int(command[0])
    folyo_for_one_chocolate = int(command[1])
    money = int(command[2])
    total_chocolates = 0
    temp_folyo = 0
    while money >= price_for_one_chocolate:
        total_chocolates += 1
        money -= price_for_one_chocolate
        temp_folyo += 1
        if folyo_for_one_chocolate == temp_folyo:
            money += price_for_one_chocolate
            temp_folyo = 0

    print(total_chocolates)
