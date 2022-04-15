destination = input()

while destination != "End":
    destination_sum = float(input())
    money = 0
    while money < destination_sum:
        salary = float(input())
        money += salary

    print(f"Going to {destination}!")

    destination = input()