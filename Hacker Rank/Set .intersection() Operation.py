n = int(input())

arr_one = set([int(i) for i in input().split()])

m = int(input())

arr_two = set([int(i) for i in input().split()])

print(len(arr_one.intersection(arr_two)))
