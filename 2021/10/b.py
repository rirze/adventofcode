#from collections import deque
from bidict import bidict
from statistics import median

if __name__ == '__main__':
    with open("input.txt", "r") as f:
        lines = f.readlines()

    chunk_lines = [line.strip() for line in lines]

    chars = bidict({
        ']': '[',
        ')': '(',
        '>': '<',
        '}': '{',
    })

    scores = {
        ')': 1,
        ']': 2,
        '}': 3,
        '>': 4,
    }

    total_scores = []
    for chunk in chunk_lines:
        stack = []
        illegal = False
        for i, c in enumerate(chunk):
            if c in chars.values():
                stack.append(c)
            else:
                if stack[-1] == chars[c]:
                    stack.pop()
                else:
                    #total_score += scores[c]
                    #illegal_chars.append(c)
                    illegal = True
                    break
        if not illegal:
            #print(stack)
            current_score = 0
            for s in reversed(stack):
                current_score = 5 * current_score + scores[chars.inverse[s]]

            total_scores.append(current_score)

    #print(illegal_chars)
    print(total_scores)
    print(median(total_scores))
