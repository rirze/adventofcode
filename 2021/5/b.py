import re
from collections import defaultdict

if __name__ == '__main__':
    with open("input.txt", "r") as f:
        lines = f.readlines()

    endpoints = [[int(n) for n in re.findall(r'\d+', line)] for line in lines]

    #print(endpoints)

    points = defaultdict(int)
    for x1, y1, x2, y2 in endpoints:
        if x1 == x2:
            ymin, ymax = min(y1, y2), max(y1, y2)
            for y in range(ymin, ymax+1):
                points[(x1, y)] += 1

        elif y1 == y2:
            xmin, xmax = min(x1, x2), max(x1, x2)
            for x in range(xmin, xmax+1):
                points[(x, y1)] += 1

        else:
            mx = [1, -1][x2-x1 < 0]
            my = [1, -1][y2-y1 < 0]
            #print(mx, my)
            for x, y in zip(range(x1, x2+mx, mx), range(y1, y2+my, my)):
                points[(x, y)] += 1


    #print(points)

    print(len([c for c in points.values() if c > 1]))
