import re

if __name__ == '__main__':
    with open("input.txt", "r") as f:
        lines = f.readlines()


    sep_ind = lines.index('\n')


    first_fold_axis, first_fold_n = re.findall(r'([xy])=(\d+)', lines[sep_ind+1])[0]
    first_fold_n = int(first_fold_n)
    print(first_fold_axis, first_fold_n)

    dots = [[int(n) for n in line.strip().split(',')] for line in lines[:sep_ind]]

    unique_dots = set()

    for dot_x, dot_y in dots:
        if first_fold_axis == 'x':
            unique_dots.add((first_fold_n - abs(dot_x - first_fold_n), dot_y))
        if first_fold_axis == 'y':
            unique_dots.add((dot_x, first_fold_n - abs(dot_y - first_fold_n)))

    print(len(unique_dots))
