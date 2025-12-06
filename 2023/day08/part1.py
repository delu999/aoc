mapping, direction = {}, []
for line in open("./2023/day08/input.txt", "r"):
    l = line.split()
    if len(l) == 0:
        continue
    elif len(l) == 1:
        direction = list(l[0])
    else:
        key, _, left, right = line.split()
        left, right = left.replace(",", "").replace("(", ""), right.replace(",", "").replace(")", "")
        mapping[key] = {"L": left, "R": right}

idx, steps, mod, k = 0, 0, len(direction), 'AAA'

while k != 'ZZZ':
    d = direction[idx]
    k = mapping[k][d]
    idx = (idx + 1) % mod
    steps += 1

print(steps)