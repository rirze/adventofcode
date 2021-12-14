from collections import Counter

if __name__ == '__main__':
    with open("input.txt", "r") as f:
        lines = f.readlines()

    polymer = lines[0].strip()

    rules = {}
    for line in lines[2:]:
        pair, replace = line.split(' -> ')

        rules[pair] = replace.strip() + pair[1]

    for i in range(40):
        polymer = ''.join([polymer[0]] + [rules[polymer[i:i+2]] for i in range(len(polymer) - 1)])
        print(polymer)
    counts = sorted(Counter(polymer).values())
    print(counts[-1] - counts[0])
