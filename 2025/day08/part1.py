import math

def main():
    connections = 1000
    lines = parse_input("./2025/day08/input.txt")
    distances = calculate_distances(lines, connections)
    solution = solve(distances)
    print(solution)

def parse_input(file_path):
    lines: list[tuple[int, int, int]] = []
    for l in open(file_path, "r"):
        x, y, z = l.strip().split(",")
        lines.append((int(x), int(y), int(z)))
    return lines

def calculate_distances(lines, connections):
    distances: list[tuple[tuple[int, int, int], tuple[int, int, int], float]] = []
    done = set()
    for e1 in lines:
        for e2 in lines:
            if e1 == e2:
                continue
            if (e1, e2) not in done:
                done.add((e1, e2))
                done.add((e2, e1))
                tmp = euclidean_distance(e1, e2)
                distances.append((e1, e2, tmp))
    distances.sort(key=lambda x: x[2])
    return distances[:connections]

def euclidean_distance(a: tuple[int, int, int], b: tuple[int, int, int]) -> float:
    px, py, pz = a
    qx, qy, qz = b
    return math.sqrt((px-qx)**2 + (py-qy)**2 + (pz-qz)**2)

def solve(distances) -> int:
    groups = []
    for a, b, _ in distances:
        groups.append(set([a, b]))
        break
    for a, b, _ in distances:
        for g in groups:
            if a in g and b in g:
                break
            elif a in g and b not in g:
                for gg in groups:
                    if b in gg:
                        g.update(gg)
                        groups.remove(gg)
                        break
                g.add(b)
                break
            elif b in g and a not in g:
                for gg in groups:
                    if a in gg:
                        g.update(gg)
                        groups.remove(gg)
                        break
                g.add(a)
                break
        else:
            groups.append(set([a, b]))

    leng = [len(g) for g in groups]
    leng.sort(reverse=True)
    return leng[0] * leng[1] * leng[2]

if __name__ == '__main__':
    main()