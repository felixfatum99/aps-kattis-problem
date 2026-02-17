import sys

input = sys.stdin.buffer.readline

n = int(input())
total = sum([int(x) for x in input().split()])
total_no_missing_number = n * (n + 1) // 2

print(total_no_missing_number-total)