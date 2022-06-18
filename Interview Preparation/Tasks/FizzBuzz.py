ll = [13, 16, 24, 44, 453, 21, 188]

for i, v in enumerate(ll):
    if v % 3 == 0 and v % 5 == 0:
        ll[i] = 'fizzbuzz'
    elif v % 3 == 0:
        ll[i] = 'fizz'
    elif v % 5 == 0:
        ll[i] = 'buzz'
