from collections import Counter
from functools import lru_cache


if __name__ == '__main__':
    with open("input.txt", "r") as f:
        lines = f.readlines()

    polymer = lines[0].strip()

    rules = {}
    for line in lines[2:]:
        pair, replace = line.split(' -> ')

        rules[pair] = pair[0] + replace.strip() + pair[1]

    def bin_split(string):
        m = len(string)//2
        return string[:m+1], string[m:]


    @lru_cache(maxsize=None)
    def get_sub(polymer):
        if len(polymer) == 2:
            return rules[polymer]

        else:
            first_string, second_string = bin_split(polymer)
            result = get_sub(first_string)[:-1] + get_sub(second_string)
            return result

    cache20 = {}
    for pair in rules:
        orig_pair = pair
        for i in range(20):
            pair = get_sub(pair)

        cache20[orig_pair] = Counter(pair[1:])

    for i in range(20):
        polymer = get_sub(polymer)

    print('l=', len(polymer))
    l = len(polymer)
    counters = [Counter(polymer[:1])]

    total_counter = Counter(polymer[:1])
    for i in range(len(polymer) - 1):
        if i % 100000 == 0:
            print(i)

        pair = polymer[i:i+2]

        total_counter += cache20[pair]

    print(total_counter)
    counts = sorted(total_counter.values())
    print(counts[-1] - counts[0])
