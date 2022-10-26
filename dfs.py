class Digraph:
    adjacency_list = []

    def __init__(self, size):
        self.adjacency_list = [[] for v in range(size)]

    def add_edge(self, v, w):
        self.adjacency_list[v].append(w)

    def adj(self, v):
        return adjacency_list[v]

    def size(self):
        return len(adjacency_list)


def main():
    dg = Digraph(5)
    dg.add_edge(0, 1)
    dg.add_edge(1, 2)
    dg.add_edge(2, 0)
    dg.add_edge(1, 3)
    print(dg.adjacency_list)


if __name__ == "__main__":
    main()
# keep state array 1 processing 2 processed 0 not visited
