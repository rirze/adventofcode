from collections import defaultdict


if __name__ == '__main__':
    with open("input.txt", "r") as f:
        lines = f.readlines()

    edges = [line.strip().split('-') for line in lines]

    graph = defaultdict(list)

    for a, b in edges:
        graph[a].append(b)
        graph[b].append(a)


    def visit(start='start', cache=set()):

        if start in cache:
            return 0

        paths = 0

        if start == 'end':
            return 1

        nexts = graph[start]
        if start.islower():
            cache.add(start)

        for next in nexts:
            paths += visit(start=next, cache=cache.copy())

        return paths

    print(visit())
