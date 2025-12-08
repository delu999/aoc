import math

def euclidean_distance(a: tuple[int, int, int], b: tuple[int, int, int]) -> float:
    px, py, pz = a
    qx, qy, qz = b
    return math.sqrt((px-qx)**2 + (py-qy)**2 + (pz-qz)**2)

lines: list[tuple[int, int, int]] = []
for l in open("./2025/day08/input.txt", "r"):
    x, y, z = l.strip().split(",")
    lines.append((int(x), int(y), int(z)))

min_dist, node1, node2, groups = None, None, None, []

distances: list[tuple[tuple[int, int, int], tuple[int, int, int], float]] = []
for e1 in lines:
    for e2 in lines:
        if e1 == e2:
            continue
        tmp = euclidean_distance(e1, e2)
        if not any(d[0] == e2 and d[1] == e1 for d in distances):
            distances.append((e1, e2, tmp))

distances.sort(key=lambda x: x[2])

print(distances)

groups = []
counter = 0
for a, b, _ in distances:
    if counter == 1000:
        break
    found = False
    for i, g in enumerate(groups):
        if a in g and b in g:
            found = True
            break
        elif a in g and b not in g:
            for gg in groups:
                if b in gg:
                    g.update(gg)
                    groups.remove(gg)
                    break
            g.add(b)
            found = True
            break
        elif b in g and a not in g:
            for gg in groups:
                if a in gg:
                    g.update(gg)
                    groups.remove(gg)
                    break
            g.add(a)
            found = True
            break
        elif a in g:
            found = True
            for gg in groups:
                if b in gg:
                    g.update(gg)
                    groups.remove(gg)
                    break
            g.add(b)
            break
        elif b in g:
            found = True
            for gg in groups:
                if a in gg:
                    g.update(gg)
                    groups.remove(gg)
                    break
            g.add(a)
            break
    if not found:
        groups.append(set([a, b]))
    counter += 1

leng = []

for g in groups:
    leng.append(len(g))

leng.sort(reverse=True)
print(leng)
print(leng[0] * leng[1] * leng[2])