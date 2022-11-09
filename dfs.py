class Digraph:
    adjacency_list = []

    # adjacency_list[v] is a list of all vertices w where there's an edge v->w
    def __init__(self, size):
        self.adjacency_list = [[] for v in range(size)]

    def add_edge(self, v, w):
        self.adjacency_list[v].append(w)

    def adj(self, v):
        return self.adjacency_list[v]

    def size(self):
        return len(self.adjacency_list)

    def has_cycle(self):
        for v in range(self.size()):
            visited = [False for v in range(self.size())]
            if self.dfs(v, visited):
                return True
        return False


    def dfs(self, v, visited):
        # check if visited
        if visited[v]:
            return True
        # mark as visited
        visited[v] = True
        # visit all children
        for child in self.adjacency_list[v]:
            if self.dfs(child, visited):
                return True
        # no cycle containing this vertex
        return False




def main():
    dg = Digraph(5)
    dg.add_edge(0, 1)
    dg.add_edge(1, 4)
    dg.add_edge(2, 0)
    dg.add_edge(1, 3)
    print(dg.adjacency_list)
    print(dg.has_cycle())
    

def test_no_nodes():
    dg = Digraph(0)
    assert dg.has_cycle() == False

def test_no_edges():
    dg = Digraph(100)
    assert dg.has_cycle() == False


if __name__ == "__main__":
    main()
# lookup knapsack optimisation

# change problem
# given an integer s and an array of coin values c, what's the fewest number of coins that sum together to make s? 
# You can use as many of each coin as you like
# e.g. s = 10, c = [7, 5, 2, 1]. Answer = 2 (5 + 5)
