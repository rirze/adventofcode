if __name__ == '__main__':
    with open("input.txt", "r") as f:
        lines = f.readlines()

    called_numbers = list(map(int, lines[0].split(',')))
    #print(list(called_numbers))
    mats = []
    for i in range(2, len(lines), 6):
        mats.append([list(map(int, line.rstrip().split())) for line in lines[i:i+5]])

    #[print(mat) for mat in mats]

    fives = {}
    for i, mat in enumerate(mats):
        fives[i] = [set(r) for r in mat] + [set(c) for c in zip(*mat)]

    #[print(f) for f in fives.values()]

    def bingo_loop():
        for n, call in enumerate(called_numbers):
            for i, rcs in fives.items():
                for five in rcs:
                    #print(five)
                    if call in five:
                        five.remove(call)

                    if not five:
                        return (i, n, call)

    i, n, last_called = bingo_loop()
    #print(i, n, list(called_numbers)[:n])

    m_sum = sum(x for c in mats[i]
                for x in c
                if x not in set(called_numbers[:n+1]))

    print(m_sum * last_called)
