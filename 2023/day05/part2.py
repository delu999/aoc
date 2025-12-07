from multiprocessing import Pool

def main():
    seeds, mapping = parse_input("./2023/day05/input.txt")
    args_list = []
    for start, end in seeds:
        args_list.append((start, start + end, mapping))
    
    processes = len(seeds)
    with Pool(processes) as p:
        results = p.map(solve, args_list)
    res = min(results)
    print(res)

def parse_input(file_path):
    lines = open(file_path).readlines()
    s= lines[0].strip().split()[1::]
    seeds = []
    for i in range(0, len(s), 2):
        seeds.append((int(s[i]), int(s[i+1])))
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
    return seeds, mapping

def solve(args):
    start, end, mapping = args
    min = -1
    for seed in range(start, end):
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