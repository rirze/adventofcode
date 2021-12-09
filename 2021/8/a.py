if __name__ == '__main__':
    with open("input.txt", "r") as f:
        lines = f.readlines()

    positions = [[list(s.split()) for s in line.split('|')] for line in lines]

    #print(positions)
    easy_numbers = {3: 7,
                    4: 4,
                    7: 8,
                    2: 1}

    easy_number_count = 0
    #easy_number_set = set(easy_numbers.keys())
    #print(easy_number_set)
    for signal_patterns, output_value in positions:
        output_value_len = list(map(len, output_value))
        for c in output_value_len:
            easy_number_count += c in easy_numbers
    print(easy_number_count)
