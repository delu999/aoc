def solve(ranges: list[tuple[int, int]]) -> int:
    count = 1 + (ranges[0][1] - ranges[0][0])
    for i in range(1, len(ranges)):
        prev_start, prev_end = ranges[i-1][0], ranges[i-1][1]
        start, end = ranges[i][0], ranges[i][1]

        if start >= prev_start and start <= prev_end:
            start = prev_end + 1
        if end >= start:
            count += 1 + (end - start)
    return count

def parse_input() -> list[tuple[int, int]]:
    ranges = []
    for line in open("./2025/day5/input.txt"):
        if line == '\n':
            break
        left, right = line.split("-")
        ranges.append((int(left), int(right)))

    ranges.sort()
    return ranges

def main():
    ranges = parse_input()
    sol = solve(ranges)
    print(sol)

if __name__ == "__main__":
    main()