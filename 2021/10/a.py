#from collections import deque

if __name__ == '__main__':
    with open("input.txt", "r") as f:
        lines = f.readlines()

    chunk_lines = [line.strip() for line in lines]

    chars = {
        ']': '[',
        ')': '(',
        '>': '<',
        '}': '{',
    }

    scores = {
        ')': 3,
        ']': 57,
        '}': 1197,
        '>': 25137,
    }

    total_score = 0
    for chunk in chunk_lines:
        stack = []
        for i, c in enumerate(chunk):
            if c in chars.values():
                stack.append(c)
            else:
                if stack[-1] == chars[c]:
                    stack.pop()
                else:
                    total_score += scores[c]
                    #illegal_chars.append(c)
                    break

    #print(illegal_chars)
    print(total_score)
