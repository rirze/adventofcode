if __name__ == '__main__':
    with open("input.txt", "r") as f:
        lines = f.readlines()

    grid = [[int(s) for s in line.strip()] for line in lines]

    ds = [
        [-1, -1],
        [-1, 0],
        [-1, 1],
        [0, -1],
        [0, 0],
        [0, 1],
        [1, -1],
        [1, 0],
        [1, 1]
    ]

    max_y, max_x = len(grid), len(grid[0])

    def step():
        flashed = set()
        greater_than_9 = set()

        for j, row in enumerate(grid):
            for i, n in enumerate(row):
                if n + 1 > 9:
                    greater_than_9.add((j, i))
                    flashed.add((j, i))
                    grid[j][i] = 0
                else:
                    grid[j][i] = n + 1

        left_to_flash = greater_than_9.copy()
        while left_to_flash:

            for j, i in greater_than_9:
                for dy, dx in ds:
                    new_y, new_x = j + dy, i + dx
                    if 0 <= new_y < max_y and 0 <= new_x < max_x:
                        new_value = grid[j + dy][i + dx]
                        if new_value + 1 > 9:
                            grid[new_y][new_x] = 0
                            left_to_flash.add((new_y, new_x))
                            flashed.add((new_y, new_x))
                        elif (new_y, new_x) not in flashed:
                            grid[new_y][new_x] = new_value + 1
                left_to_flash.remove((j, i))

            greater_than_9 = left_to_flash.copy()

        return len(flashed)

    step_n = 1
    while step() != max_y * max_x:
        step_n += 1

    print(step_n)
