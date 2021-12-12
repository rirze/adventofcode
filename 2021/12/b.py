from collections import defaultdict
from typing import Counter


if __name__ == '__main__':
    with open("input.txt", "r") as f:
        lines = f.readlines()

    edges = [line.strip().split('-') for line in lines]

    graph = defaultdict(list)

    for a, b in edges:
        graph[a].append(b)
        graph[b].append(a)

    print(graph)

    def visit(start='start', cache=defaultdict(int)):

        c = Counter(cache.values())

        if c[3] or c[2] > 1:
            return 0

        paths = 0

        if start == 'end':
            return 1

        nexts = graph[start]

        if start.islower():
            cache[start] += 1

        for next in nexts:
            if next != 'start':
                paths += visit(start=next, cache=cache.copy())

        return paths

    print(visit())
