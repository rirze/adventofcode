import numpy as np

if __name__ == '__main__':
    with open("input.txt", "r") as f:
        lines = f.readlines()

    positions = [[list(s.split()) for s in line.split('|')] for line in lines]

    # easy_numbers = {3: 7,
    #                 4: 4,
    #                 7: 8,
    #                 2: 1}

    numbers = np.array([
        [1, 1, 1, 0, 1, 1, 1], # + [0, 0, 0],
        [0, 0, 1, 0, 0, 1, 0], # + [0, 0, 0],
        [1, 0, 1, 1, 1, 0, 1], # + [0, 0, 0],
        [1, 0, 1, 1, 0, 1, 1], # + [0, 0, 0],
        [0, 1, 1, 1, 0, 1, 0], # + [0, 0, 0],
        [1, 1, 0, 1, 0, 1, 1], # + [0, 0, 0],
        [1, 1, 0, 1, 1, 1, 1], # + [0, 0, 0],
        [1, 0, 1, 0, 0, 1, 0], # + [0, 0, 0],
        [1, 1, 1, 1, 1, 1, 1], # + [0, 0, 0],
        [1, 1, 1, 1, 0, 1, 1], # + [0, 0, 0]
    ])

    ''' sorted array
[(2, 2, 2, [0, 0, 1, 0, 0, 1, 0]), 1
 (3, 2, 2, [1, 0, 1, 0, 0, 1, 0]), 7
 (4, 2, 4, [0, 1, 1, 1, 0, 1, 0]), 4
 (5, 1, 2, [1, 0, 1, 1, 1, 0, 1]), 2
 (5, 1, 3, [1, 1, 0, 1, 0, 1, 1]), 5
 (5, 2, 3, [1, 0, 1, 1, 0, 1, 1]), 3
 (6, 1, 3, [1, 1, 0, 1, 1, 1, 1]), 6
 (6, 2, 3, [1, 1, 1, 0, 1, 1, 1]), 0
 (6, 2, 4, [1, 1, 1, 1, 0, 1, 1]), 9
 (7, 2, 4, [1, 1, 1, 1, 1, 1, 1])] 8
    '''

    display_vars = 'abcdefg'

    result = 0
    for signal_patterns, output_value in positions:
        sorted_patterns = [sorted(s) for s in signal_patterns]
        arr = [
            [int(v in s) for v in display_vars]
            for s in sorted_patterns
        ]

        sorted_arr = sorted(arr, key=sum)

        r2, r4 = sorted_arr[0], sorted_arr[2]

        sorted_arr = sorted(arr,
                            key=lambda r:(sum(r), np.sum(np.extract(r2, r)), np.sum(np.extract(r4, r))))

        map = {''.join(c for c, bit in zip(display_vars, row) if bit): str(value)
               for row, value in zip(sorted_arr, (1,7,4,2,5,3,6,0,9,8))}

        #print(map)
        #print([sorted(o) for o in output_value])
        ans = int(''.join(map[''.join(sorted(s))] for s in output_value))
        print(ans)

        result+=ans

    print(result)
