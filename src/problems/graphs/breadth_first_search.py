example_graph = {
    'A': {'B', 'C'},
    'B': {'A', 'D', 'E'},
    'C': {'A', 'F'},
    'D': {'B'},
    'E': {'B', 'F'},
    'F': {'C', 'E'}
}


def bfs(graph, start):
    visited = set()
    queue = [start, ]

    while queue:
        vertex = queue.pop(0)
        if vertex not in visited:
            visited.add(vertex)
            queue.extend(graph[vertex] - visited)

    return visited


def bfs_paths(graph, start, goal):
    queue = [(start, [start, ])]

    while queue:
        (vertex, path) = queue.pop(0)
        for nxt in graph[vertex] - set(path):
            if nxt == goal:
                yield path + [nxt]
            else:
                queue.append((nxt, path + [nxt]))


def shortest_path(graph, start, goal):
    try:
        return next(bfs_paths(graph, start, goal))
    except StopIteration:
        return None


if __name__ == '__main__':
    g = bfs(example_graph, 'A')
    print(g)
    ls = bfs_paths(example_graph, 'A', 'F')
    print(list(ls))
    sp = shortest_path(example_graph, 'A', 'F')
    print(sp)
