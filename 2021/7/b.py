from statistics import mean
from math import floor, ceil

if __name__ == '__main__':
    with open("input.txt", "r") as f:
        line = f.readline()

    positions = [int(x) for x in line.split(',')]

    #c = Counter(positions)

    a = mean(positions)
    a_l, a_u = floor(a), ceil(a)
    print(a_l, a_u)


    print(min(sum((abs(p - a) * (abs(p - a) + 1))/ 2.0 for p in positions) for a in [a_l, a_u]))
