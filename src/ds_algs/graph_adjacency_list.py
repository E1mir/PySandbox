class Vertex(object):
    def __init__(self, key):
        self.id = key
        self.connected_to = {}

    def add_neighbor(self, nbr, weight=0):
        self.connected_to[nbr] = weight

    def get_connections(self):
        return self.connected_to.keys()

    def get_id(self):
        return self.id

    def get_weight(self, nbr):
        return self.connected_to[nbr]

    def __str__(self):
        return "{} connected to: {}".format(
            self.id,
            [x.id for x in self.connected_to]
        )


class Graph(object):
    def __init__(self):
        self.vertices_list = {}
        self.num_vertices = 0

    def add_vertex(self, key):
        self.num_vertices += 1
        new_vertex = Vertex(key)
        self.vertices_list[key] = new_vertex
        return new_vertex

    def get_vertex(self, key):
        if key in self.vertices_list:
            return self.vertices_list[key]
        else:
            return None

    def add_edge(self, f, t, cost=0):
        """
        :param f: From vertex
        :param t: To vertex
        :param cost: Weight of vertex
=        """
        if f not in self.vertices_list:
            new_vertex = self.add_vertex(f)
        if t not in self.vertices_list:
            new_vertex = self.add_vertex(t)

        self.vertices_list[f].add_neighbor(self.vertices_list[t], cost)

    def get_vertices(self):
        return self.vertices_list.keys()

    def __iter__(self):
        return iter(self.vertices_list.values())

    def __contains__(self, key):
        return key in self.vertices_list


if __name__ == '__main__':
    g = Graph()

    for i in range(6):
        g.add_vertex(i)

    print(g.vertices_list)

    g.add_edge(0, 1, 2)
    g.add_edge(0, 5, 3)
    g.add_edge(2, 4, 3)
    g.add_edge(4, 2, 2)
    g.add_edge(1, 4, 2)
    for v in g:
        print(v)
