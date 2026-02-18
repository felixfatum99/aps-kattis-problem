import random
import string

def generate_number_row(n, picked):
    nums_below = list(range(1, picked))
    nums_above = list(range(picked+1, n+1))
    nums = nums_below+nums_above
    random.shuffle(nums)
    return nums

def generate_random_string(set):
    while True:
        word_one = ''.join(random.choices(string.ascii_lowercase, k=random.randint(1, 9)))
        word_two = ''.join(random.choices(string.ascii_lowercase, k=random.randint(1, 9)))
        word = word_one + " " + word_two
        if word not in set:
            break
    return word

for i in range(2, 7):
    file = str(10)
    n = pow(10, 5)*2

    distinct_wines = set()
    wine_and_id = []
    chosen_wine = None
    picked = 2
    nums = generate_number_row(n, picked)

    for i in range(1, n+1):
        word = generate_random_string(distinct_wines)
        distinct_wines.add(word)
        wine_and_id.append((word, i))
        if i == picked:
            chosen_wine = word

    #random id order
    wine_and_id.sort()

    with open(f"data/secret/{file}.in", "w") as f:
        f.write(str(n) + "\n")
        for wine_id in wine_and_id:
            f.write(wine_id[0] + " " + str(wine_id[1]) + "\n")
        f.write(" ".join(map(str, nums)) + "\n")

    with open(f"data/secret/{file}.ans", "w") as f:
        f.write(chosen_wine + "\n")