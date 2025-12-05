import networkx as nx
import random
from multiprocessing import Pool

def karger_algorithm(mg: nx.MultiGraph) -> nx.MultiGraph:
    while len(mg.nodes) > 2:
        u, v, _ = random.choice(list(mg.edges))
        u_neighbours = [node for node in mg.neighbors(u) if node != v]
        v_neighbours = [node for node in mg.neighbors(v) if node != u]

        super_node = u + " " + v
        mg.add_node(super_node)

        for n in u_neighbours:
            mg.add_edge(super_node, n)
        for n in v_neighbours:
            mg.add_edge(super_node, n)

        mg.remove_node(u)
        mg.remove_node(v)
    return mg

def get_solution(edges):
    for _ in range(0, 10000):
        mg = karger_algorithm(nx.MultiGraph(edges))  # pass a copy of the graph
        
        super_nodes = list(mg.nodes)
        s = super_nodes[0].split(" ")
        t = super_nodes[1].split(" ")

        # The C = (S, T) of G = (V, E) is: {(u, v) ∈ E | u ∈ S, v ∈ T} 
        count = 0
        for u, v in edges:
            if (u in s and v in t) or (u in t and v in s):
                count += 1
        if count == 3:
            print(len(s) * len(t))
            return len(s) * len(t)
        
    return -1

def solve_problem(edges):
    processes = 8
    args_list = [edges for _ in range(processes)]
    
    with Pool(processes) as p:
        results = p.map(get_solution, args_list)

    print(set(results))


def main():
    f = open("./2023/day25/input.txt", "r")
    lines = f.readlines()
    edges = []
    for l in lines:
        l = l.replace(":", "")
        l = l.replace("\n", "")
        nodes = l.split(" ")
        
        for i in range(1, len(nodes)):
            edges.append((nodes[0], nodes[i]))
    
    solve_problem(edges)
    f.close()

if __name__ == '__main__':
    main()