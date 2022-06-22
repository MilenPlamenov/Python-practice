def take_all_divisors(n, divisors):
    for i in range(1, n):
        if n % i == 0:
            divisors.append(i)
    return divisors


def check_if_perfect_number(n):
    if sum(take_all_divisors(n, divisors)) == n:
        return 'Perfect number !'
    return 'Not a perfect number :c'


n = 28
divisors = []
print(check_if_perfect_number(n))
