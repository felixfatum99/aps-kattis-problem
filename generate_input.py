import random

def generate(n, picked):
    nums_below = list(range(1, picked))
    nums_above = list(range(picked+1, n+1))
    nums = nums_below+nums_above
    random.shuffle(nums)

    return nums

for i in range(1, 7):
    file = str(i)
    n = pow(10, i)
    picked = random.randint(2, n-1)
    nums = generate(n, picked)

    with open(f"data/secret/{file}.in", "w") as f:
        f.write(str(n) + "\n")
        f.write(" ".join(map(str, nums)) + "\n")

    with open(f"data/secret/{file}.ans", "w") as f:
        f.write(str(picked) + "\n")