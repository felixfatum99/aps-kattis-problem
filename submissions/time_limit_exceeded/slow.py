n = int(input())
arr = [int(x) for x in input().split()]

for i in range(1, n + 1):
    i_is_present = False

    for j in range(n - 1):
        if i == arr[j]:
            i_is_present = True
            break
    
    if not i_is_present:
        print(i)
        break