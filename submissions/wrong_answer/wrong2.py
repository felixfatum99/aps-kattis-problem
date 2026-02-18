n = int(input())

d = {}

for _ in range(n):
    wine, id = input().rsplit(" ", 1)
    d[int(id)] = wine

arr = [int(x) for x in input().split()]

for i in range(2, n):
    if i not in arr:
        print(d[i])
        break