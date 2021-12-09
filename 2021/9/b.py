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
                local_mins.append((y, x))

    print(local_mins)


    def find_dec(y, x, cache=set()):
        size = 1
        if (y, x) in cache:
            return 0
        cache.add((y,x))

        if x != 0:
            adj = heights[y][x-1]
            if adj != 9:
                size += find_dec(y, x-1, cache=cache)
        if x != max_x:
            adj = heights[y][x+1]
            if adj != 9:
                size += find_dec(y, x+1, cache=cache)
        if y != 0:
            adj = heights[y-1][x]
            if adj != 9:
                size += find_dec(y-1, x, cache=cache)
        if y != max_y:
            adj = heights[y+1][x]
            if adj != 9:
                size += find_dec(y+1, x, cache=cache)

        return size

    m3, m2, m1 = list(reversed(sorted(find_dec(y, x) for y, x in local_mins)))[:3]

    print(m3 * m2 * m1)
