from ds_algs.graph_adjacency_list import Graph


def build_graph(word_file):
    d = {}
    g = Graph()
    w_file = open(word_file, 'r')
    # create buckets of words that differ by one letter

    for line in w_file:
        print(line)
        word = line[:-1]
        print(word)
        for i in range(len(word)):
            bucket = word[:i] + '_' + word[i + 1:]
            if bucket in d:
                d[bucket].append(word)
            else:
                d[bucket] = [word]

    for bucket in d.keys():
        for word_1 in d[bucket]:
            for word_2 in d[bucket]:
                if word_1 != word_2:
                    g.add_edge(word_1, word_2)

    return g


if __name__ == '__main__':
    graph = build_graph('words.txt')
    print(graph.get_vertices())
