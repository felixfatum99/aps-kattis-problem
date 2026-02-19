import sys 
import re

n = sys.stdin.readline()
if not re.match(r"(0|([1-9][0-9]*))\n", n):
        sys.exit(43)
try:
    x = int(n)-1

    #Replace with actual values
    if not 0 <= x <= 1000000:
        sys.exit(43)
except ValueError:
    sys.exit(43)

line = sys.stdin.readline()

if not re.match(r"^(0|[1-9][0-9]*)( (0|[1-9][0-9]*))*$", line):
    print("Syntax error")
    sys.exit(43)

nums = line.split()

if len(nums) != x:
     print("Number of elements does not match n-1")
     sys.exit(43)

if len(set(nums)) != len(nums):
     print("Duplicate elements found")
     sys.exit(43)
    
if sys.stdin.read().strip() != "":
    sys.exit(43)

sys.exit(42)