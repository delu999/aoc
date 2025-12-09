def main():
    points = parse_input("./2025/day09/input.txt")
    sol = solve(points)
    print(sol)

def parse_input(file_path: str) -> list[tuple[int, int]]:
    points = []
    for line in open(file_path, "r"):
        x, y = line.strip().split(",")
        points.append((int(x), int(y)))
    return points
    
def solve(points: list[tuple[int, int]]) -> int:
    sol, n = -1, len(points)
    for i in range(n):
        for j in range(i + 1, n):
            tmp = (abs(points[i][0] - points[j][0]) + 1) * (abs(points[i][1] - points[j][1]) + 1)
            if tmp > sol:
                sol = tmp
    return sol

if __name__ == "__main__":
    main()