if __name__ == '__main__':
    with open("input.txt", "r") as f:
        lines = f.readlines()

    heights = [[int(n) for n in line.strip()] for line in lines]

    max_y, max_x = len(heights) - 1, len(heights[0]) - 1

    local_mins = []
    for y, row in enumerate(heights):
        for x, n in enumerate(row):
            nums_to_compare = set()
            if x != 0:
                nums_to_compare.add(heights[y][x-1])
            if x != max_x:
                nums_to_compare.add(heights[y][x+1])
            if y != 0:
                nums_to_compare.add(heights[y-1][x])
            if y != max_y:
                nums_to_compare.add(heights[y+1][x])

            if min(nums_to_compare) > n:
                local_mins.append(n)

    print(local_mins)
    print(sum(local_mins) + len(local_mins))
