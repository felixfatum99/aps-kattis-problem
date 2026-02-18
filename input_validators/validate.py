import sys 
import re

# N -> Amount of wines
n = sys.stdin.readline().strip()
if not re.fullmatch(r"[1-9]\d*", n):
        sys.exit(43)

x = int(n)

if not 1 <= x <= 200000:
    sys.exit(43)

wines = []
ids = []

# N lines of distinct wines and their distinct ids
for _ in range(x):
    line = sys.stdin.readline()
    line = line.rstrip("\r\n")

    if not re.match(r"^[a-z]+(?: [a-z]+)* [1-9]\d*$", line):
         sys.exit(43)

    wine, id = line.rsplit(" ", 1)

    if len(wine) > 20:
         sys.exit(43)
    
    wines.append(wine)

    y = int(id)
    if not 1 <= y <= x:
        sys.exit(43)

    ids.append(y)

idset = set(ids)
if len(idset) != x:
     sys.exit(43)

if len(set(wines)) != x:
     sys.exit(43)

if x > 1:
    # N-1 id's
    line = sys.stdin.readline().strip()

    if not re.match(r"^[1-9][0-9]*( [1-9][0-9]*)*$", line):
        sys.exit(43)

    nums = [int(t) for t in line.split()]

    if len(nums) != x-1:
        sys.exit(43)
    if len(set(nums)) != len(nums):
        sys.exit(43)
    if any(not (1 <= v <= x) for v in nums):
        sys.exit(43)
    if any(v not in idset for v in nums):
        sys.exit(43)
        
if sys.stdin.read().strip() != "":
    sys.exit(43)

sys.exit(42)