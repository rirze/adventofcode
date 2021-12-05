if __name__ == '__main__':
    with open("input.txt", "r") as f:
        lines = f.readlines()


    depths = [line.rstrip().split(' ')
              for line in lines
              ]

    aim, horiz, depth = 0,0,0
    for dir, n in depths:
        n = int(n)
        if dir == 'down':
            aim += n
        elif dir == 'up':
            aim -= n
        elif dir == 'forward':
            horiz += n
            depth += aim * n

    print(horiz, depth, horiz*depth)
