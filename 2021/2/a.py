if __name__ == '__main__':
    with open("input.txt", "r") as f:
        lines = f.readlines()


    depths = [line.rstrip().split(' ')
              for line in lines
              ]

    print(depths)
    d = {
        'forward': 1j,
        'down': 1,
        'up': -1
    }

    z = sum(d[dir] * int(n) for dir, n in depths)
    print(int(z.real * z.imag))
