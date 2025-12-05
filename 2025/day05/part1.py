def solve(ranges: set[tuple[int, int]], lines: list[str], starting_line: int) -> int:
    count = 0
    nl = len(lines)
    for i in range(starting_line, nl):
        l = int(lines[i].replace("\n", ""))
        for start, end in ranges:
            if l >= start and l <= end:
                count += 1
                break
    return count

def prepare_ranges(lines: list[str]) -> tuple[set, int]:
    ranges = set()
    i = 0
    while True:
        if lines[i] == '\n':
            i += 1
            break
        l = lines[i].split("-")
        r = (int(l[0]), int(l[1].replace("\n", "")))
        ranges.add(r)
        i += 1
    return ranges, i

def main():
    lines = open("./2025/day5/input.txt").readlines()
    ranges, starting_line = prepare_ranges(lines)
    sol = solve(ranges, lines, starting_line)
    print(sol)

if __name__ == "__main__":
    main()