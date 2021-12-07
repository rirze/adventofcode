if __name__ == '__main__':
    with open("input.txt", "r") as f:
        line = f.readline()

    state = [int(x) for x in line.split(',')]

    for day in range(80):
        new = 0
        print(day)
        if day < 18:
            print(state)
        for i in range(len(state)):
            if state[i] == 0:
                new += 1
                state[i] = 6
            else:
                state[i] -= 1

        state += new * [8]

    print(len(state))
