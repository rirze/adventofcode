from collections import deque

if __name__ == '__main__':
    with open("input.txt", "r") as f:
        line = f.readline()

    state = [int(x) for x in line.split(',')]

    hist = deque([0]*9)

    for s in state:
        hist[s] += 1

    for day in range(256):
        rep = hist[0]

        hist.rotate(-1)

        hist[6] += rep

    print(sum(hist))
