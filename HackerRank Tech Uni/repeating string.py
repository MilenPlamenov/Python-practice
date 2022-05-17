def most_c(ll):
    return max(ll, key=ll.count)


n = int(input())

for _ in range(n):
    str_input = input()
    ll = []
    [ll.append(i) for i in str_input]
    ll.sort()
    most_common = most_c(ll)
    if ll.count(most_common) % 2 == 0:
        print(most_common * (ll.count(most_common) // 2))


