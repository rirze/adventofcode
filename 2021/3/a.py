from statistics import mode

if __name__ == '__main__':
    with open("input.txt", "r") as f:
        lines = f.readlines()
        lines = [line.rstrip() for line in lines]

    most_common_num = ''.join(map(mode, zip(*lines)))
    least_common_num = ''.join({'1': '0', '0': '1'}[n] for n in most_common_num)

    print(int(most_common_num, 2) * int(least_common_num, 2))
