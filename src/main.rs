use std::collections::VecDeque;

struct Digraph {
    // adjacency_list[v] is a list of all the vertices w where there are edges v->w
    adjacency_list: Vec<Vec<usize>>,
}

impl Digraph {
    // Create digraph with given number of vertices
    fn new(num_vertices: usize) -> Digraph {
        let entry: Vec<usize> = Vec::new();
        let adjacency_list: Vec<Vec<usize>> = vec![entry; num_vertices];
        Digraph { adjacency_list }
    }

    // Add edge from vertex v to vertex w
    // Panic if v isn't in the graph
    fn add_edge(&mut self, v: usize, w: usize) {
        if let Some(edges_from_v) = self.adjacency_list.get_mut(v) {
            edges_from_v.push(w);
        } else {
            panic!("Vertex {} not in graph", v);
        }
    }

    // All vertices w where there's an edge v->w
    // Get immutable reference
    fn adj(&self, v: usize) -> &Vec<usize> {
        if let Some(edges_from_v) = self.adjacency_list.get(v) {
            edges_from_v
        } else {
            panic!("Vertex {} not in graph", v);
        }
    }

    // Helper method
    fn num_vertices(&self) -> usize {
        self.adjacency_list.len()
    }
}

// All vertices in topological order
// If there's a cycle, return None
fn topological_sort(g: &Digraph) -> Option<Vec<usize>> {
    let size = g.num_vertices();

    let mut order: Vec<usize> = Vec::new(); // Topological order
    let mut visited = vec![false; size]; // Vertex-indexed vec of visited vertices (i.e. added to our order)
    let mut in_degree: Vec<usize> = vec![0; size]; // How many edges coming in to each vertex?
    let mut queue: VecDeque<usize> = VecDeque::new(); // Vertices with in-degree 0

    // Initialise in_degree
    for v in 0..size {
        let neighbours = g.adj(v);
        neighbours.iter().for_each(|w| in_degree[*w] += 1);
    }

    // Add all vertices with no incoming edges to the queue
    in_degree.iter().enumerate().for_each(|(v, degree)| {
        if *degree == 0 {
            queue.push_back(v)
        }
    });

    while !queue.is_empty() {
        let v = queue.pop_front().unwrap();
        order.push(v);
        visited[v] = true;

        for w in g.adj(v) {
            in_degree[*w] -= 1;
            if in_degree[*w] == 0 {
                queue.push_back(*w);
            }
        }
    }

    match order.len() {
        x if x == size => Some(order),
        _ => None,
    }
}

// // All vertices reachable from source s
// fn dfs(g: &Digraph, s: usize) -> Vec<usize> {
//     let mut visited = vec![false; g.num_vertices()];
//     let reachable: RefCell<Vec<usize>> = RefCell::new(Vec::new());
//     reachable.borrow_mut().push(s);
//     visited[s] = true;

//     g.adj(s).into_iter().for_each(|v| dfs_recur(g, reachable.borrow_mut(), visited, *v));

//     reachable.into_inner()
// }

// fn dfs_recur(g: &Digraph, mut reachable: RefMut<Vec<usize>>, mut visited: Vec<bool>, s: usize) {
//     reachable.push(s);
//     visited[s] = true;
//     g.adj(s).into_iter().for_each(move |v| dfs_recur(g, reachable, visited, *v))

// }

fn main() {
    let mut g = Digraph::new(8);
    g.add_edge(0, 1);
    g.add_edge(1, 2);
    g.add_edge(2, 0);
    g.add_edge(1, 3);
    g.add_edge(2, 5);
    g.add_edge(4, 3);
    g.add_edge(6, 4);
    g.add_edge(7, 0);

    let sorted = topological_sort(&g);
    println!("{:?}", sorted);
}
