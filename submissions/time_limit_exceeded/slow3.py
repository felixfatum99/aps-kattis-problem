n = int(input())

d = {}

for _ in range(n):
    wine, id = input().rsplit(" ", 1)
    d[int(id)] = wine

if n == 1:
    print(d[1])
else:
    arr = [int(x) for x in input().split()]

    for i in range(n, 0, -1):
        if i not in arr:
            print(d[i])
            break