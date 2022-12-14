# lookup knapsack optimisation

# change problem
# given an integer s and an array of coin values c, what's the fewest number of coins that sum together to make s? 
# It it's not possible, return -1
# You can use as many of each coin as you like
# e.g. s = 10, c = [7, 5, 2, 1]. Answer = 2 (5 + 5)

import big_o

def smallest_change(s, c):
    num_coins = 0
    cur_nodes = [0]
    visited = [False for i in range(s+1)]
    while len(cur_nodes) > 0:
        num_coins += 1
        new_nodes = []
        for node in cur_nodes:
            for child in get_children(node, c, s):
                if child == s:
                    return num_coins
                if not visited[child]:
                    visited[child] = True
                    new_nodes.append(child)
        cur_nodes = new_nodes
    return -1

def get_children(node, c, s):
    return [node + child for child in c if node + child <= s]

def test_smallest_change():
    s, c = 10, [7, 5, 2, 1]
    ans = 2
    assert smallest_change(s, c) == ans

def calculate_complexity():
    def smallest_change_wrapper(inputs):
        return smallest_change(*inputs)

    def input_generator(n):
        return (big_o.datagen.n_(n), [*set(big_o.datagen.integers(n, 1, n))])

    best, others = big_o.big_o(smallest_change_wrapper, input_generator, n_measures=1000, n_timings=2)
    print(best)
    for class_, residuals in others.items():
        print('{!s:<60s}    (res: {:.2G})'.format(class_, residuals))

if __name__ == "__main__":
    calculate_complexity()