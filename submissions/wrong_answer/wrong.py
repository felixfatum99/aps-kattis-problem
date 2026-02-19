n = int(input())
nums = list(map(int, input().split()))

expected = n * (n + 1) / 2  
print(int(expected - sum(nums)))