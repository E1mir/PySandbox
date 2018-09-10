example_graph = {
    'A': {'B', 'C'},
    'B': {'A', 'D', 'E'},
    'C': {'A', 'F'},
    'D': {'B'},
    'E': {'B', 'F'},
    'F': {'C', 'E'}
}


def dfs(graph, start):
    visited = set()
    stack = [start, ]

    while stack:
        vertex = stack.pop()

        if vertex not in visited:
            visited.add(vertex)

            stack.extend(graph[vertex] - visited)

    return visited


def dfs_paths(graph, start, goal):
    stack = [(start, [start])]
    while stack:
        (vertex, path) = stack.pop()
        for nxt in graph[vertex] - set(path):
            if nxt == goal:
                yield path + [nxt]
            else:
                stack.append((nxt, path + [nxt]))


if __name__ == '__main__':
    s = dfs(example_graph, 'F')
    print(s)
    ls = dfs_paths(example_graph, 'D', 'C')
    print(list(ls))
