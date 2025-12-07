def main():
    seeds, mapping = parse_input("./2023/day05/input.txt")
    sol = solve(seeds, mapping)
    print(sol)

def parse_input(file_path):
    lines = open(file_path).readlines()
    seeds = lines[0].strip().split()[1::]
    mapping = []
    pos = -1
    for i in range(1, len(lines)):
        if len(lines[i].strip()) < 4:
            continue
        elif lines[i].find('map') != -1:
            pos += 1
            mapping.append([])
            continue
        s = lines[i].strip().split()
        for e in s:
            mapping[pos].append(int(e))
    return [int(seed) for seed in seeds], mapping

def solve(seeds, mapping):
    min = -1
    for seed in seeds:
        for row in mapping:
            for j in range(0, len(row), 3):
                dest, source, l = row[j], row[j+1], row[j+2]
                if seed >= source and seed <= source + l:
                    move_seed = abs(source - dest)
                    seed = seed - move_seed if source > dest else seed + move_seed           
                    break
        if min == -1 or seed < min:
            min = seed
    return min

if __name__ == '__main__':
    main()