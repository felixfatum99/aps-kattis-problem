n = int(input())

d = {}

for _ in range(n):
    wine, id = input().rsplit(" ", 1)
    d[int(id)] = wine

if n == 1:
    print(d[1])
else:
    total = sum([int(x) for x in input().split()])
    total_no_missing_number = n * (n + 1) // 2

    print(d[total_no_missing_number-total])