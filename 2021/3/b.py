"""from statistics import multimode

if __name__ == '__main__':
    with open(\\\\\\\"test.txt\\\\\\\", \\\\\\\"r\\\\\\\") as f:
        lines = f.readlines()
        lines = [line.rstrip() for line in lines]

    most_common_num = ''.join(map(lambda n: max(multimode(n)), zip(*lines)))
    least_common_num = ''.join({'1': '0', '0': '1'}[n] for n in most_common_num)

    print(most_common_num, least_common_num)
    #print(int(most_common_num, 2), int(least_common_num, 2))

    def find_closest(number):
        ints = [abs(int(number, 2) - int(n, 2)) for n in lines]
        min_diff = min(ints)
        return lines[ints.index(min_diff)]

    print(int(find_closest(most_common_num), 2), int(find_closest(least_common_num), 2))

"""

from statistics import mode, multimode

if __name__ == '__main__':
    with open("input.txt", "r") as f:
        lines = f.readlines()
        lines = [line.rstrip() for line in lines]

    most_common_num = ''.join(map(mode, zip(*lines)))
    least_common_num = ''.join({'1': '0', '0': '1'}[n] for n in most_common_num)

    #print(most_common_num)
    print(most_common_num, least_common_num)
    print(int(most_common_num, 2), int(least_common_num, 2))

    def find_closest(number, invert=False):
        remaining, i, n = set(lines), 0, len(lines[0])
        while len(remaining) > 1 and i < n:
            bit = max(multimode(list(zip(*remaining))[i]))
            if invert:
                bit = {'1': '0', '0': '1'}[bit]
            new_remaining = set()
            for x in remaining:
                if x[i] == bit:
                    new_remaining.add(x)
            remaining = new_remaining
            i+=1

        return remaining.pop()

    print(int(find_closest(most_common_num), 2)* int(find_closest(least_common_num, True), 2))
