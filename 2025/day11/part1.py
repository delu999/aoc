import networkx as nx
from functools import lru_cache

mg = nx.DiGraph()
start_node, end_node = "you", "out"

@lru_cache(maxsize=None)
def solve_problem(node):
    if node == end_node:
        return 1
    return sum(solve_problem(a) for a in mg.successors(node))

def parse_lines(file_path: str):
    lines = open(file_path, "r").readlines()
    edges = []
    for l in lines:
        l = l.replace(":", "")
        l = l.replace("\n", "")
        nodes = l.split(" ")
        for i in range(1, len(nodes)):
            edges.append((nodes[0], nodes[i]))
    global mg
    mg.add_edges_from(edges)

def main():
    parse_lines("./2025/day11/input.txt")
    sol = solve_problem(start_node)
    print(sol)

if __name__ == "__main__":
    main()