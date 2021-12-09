from statistics import median

if __name__ == '__main__':
    with open("input.txt", "r") as f:
        line = f.readline()

    positions = [int(x) for x in line.split(',')]

    m = median(positions)

    print(sum(abs(p - m) for p in positions))
