if __name__ == '__main__':
    with open("input.txt", "r") as f:
        lines = f.readlines()

    depths = [int(line.strip()) for line in lines]

    print(sum(y>x for x,y in zip(depths, depths[1:])))
