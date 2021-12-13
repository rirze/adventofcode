import re

if __name__ == '__main__':
    with open("input.txt", "r") as f:
        lines = f.readlines()


    sep_ind = lines.index('\n')


    folds = []
    for fold in lines[sep_ind+1:]:
        fold_axis, fold_n = re.findall(r'([xy])=(\d+)', fold.strip())[0]
        folds.append((fold_axis, int(fold_n)))

    print(folds)

    dots = [[int(n) for n in line.strip().split(',')] for line in lines[:sep_ind]]

    for fold_axis, fold_n in folds:
        unique_dots = set()

        for dot_x, dot_y in dots:
            if fold_axis == 'x':
                unique_dots.add((fold_n - abs(dot_x - fold_n), dot_y))
            elif fold_axis == 'y':
                unique_dots.add((dot_x, fold_n - abs(dot_y - fold_n)))

        dots = unique_dots.copy()

    print(len(unique_dots))

    grid = [['.'] * 50 for _ in range(10)]

    for x, y in dots:
        grid[y][x] = '#'

    [print(''.join(row)) for row in grid]
