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
    perimeter = gen_perimeter(points)
    vert = gen_vertical_segments(points)
    points_w_area = points_with_area(points)
    min_x = get_min_x_coordinate(points)
    
    for p1, p2, a in points_w_area:
        x1, y1, x2, y2 = swap_points(p1[0], p1[1], p2[0],  p2[1])
        if (
                check_col(vert, perimeter, x1, y1, y2, min_x) 
                and check_col(vert, perimeter, x2, y1, y2, min_x) 
                and check_row(vert, perimeter, y1, x1, x2, min_x) 
                and check_row(vert, perimeter, y2, x1, x2, min_x)
            ):
            return a
    return -1

def gen_perimeter(points) -> set[tuple[int, int]]:
    n = len(points)
    perimeter = set()
    for i in range(n):
        x1, y1, x2, y2 = points[i][0], points[i][1], points[(i + 1) % n][0], points[(i + 1) % n][1]
        if x1 == x2:
            if y1 > y2:
                y1, y2 = y2, y1
            
            for k in range(y1, y2 + 1):
                perimeter.add((x1, k))
        else:
            if x1 > x2:
                x1, x2 = x2, x1
            
            for k in range(x1, x2 + 1):
                perimeter.add((k, y1))
    return perimeter

def gen_vertical_segments(points) -> list[tuple[int, int, int]]:
    n = len(points)
    vert = []
    for i in range(n):
        x1, y1, x2, y2 = points[i][0], points[i][1], points[(i + 1) % n][0], points[(i + 1) % n][1]
        if x1 != x2:
            continue
        if y1 > y2:
            y1, y2 = y2, y1
        vert.append((x1, y1, y2))  # (x, y_lo, y_hi)
    return vert

def points_with_area(points: list[tuple[int, int]]) -> list[tuple[tuple[int, int], tuple[int, int], int]]:
    points_w_area = set()
    for x1, y1 in points:
        for x2, y2 in points:
            if x1 == x2 and y1 == y2:
                continue
            area = (abs(x2 - x1) + 1) * (abs(y2 - y1) + 1)
            points_w_area.add(((x1, y1), (x2, y2), area))
    points_w_area= list(points_w_area)
    points_w_area.sort(key=lambda x: x[2], reverse=True)
    return points_w_area

def get_min_x_coordinate(points: list[tuple[int, int]]):
    min_x = 99999
    for x, _ in points:
        if x < min_x:
            min_x = x
    return min_x - 1

def swap_points(x1, y1, x2, y2) -> tuple[int, int, int, int]:
    if y1 == y2:
        if x1 > x2:
            return x2, y1, x1, y2
        else:
            return x1, y1, x2, y2
    elif x1 == x2:
        if y1 > y2:
            return x1, y2, x2, y1
        else:
            return x1, y1, x2, y2
    if x1 > x2 and y1 > y2:
        return x2, y2, x1, y1
    if x1 > x2:
        return x2, y1, x1, y2
    if x2 > x1 and y2 < y1:
        return x1, y2, x2, y1
    return x1, y1, x2, y2

# straight line bottom - up
def check_col(vertical, perimeter, x, y1, y2, min_x):
    for i in range(y1, y2 + 1):
        if (x, i) in perimeter:
            continue
        if not is_inside_area(vertical, perimeter, x, i, min_x):
            return False
    return True

# straight line left to right
def check_row(vertical, perimeter, y, x1, x2, min_x):  
    for i in range(x1, x2 + 1):
        if (i, y) in perimeter:
            continue
        if not is_inside_area(vertical, perimeter, i, y, min_x):
            return False
    return True

def is_inside_area(vertical, perimeter, x, y, min_x):
    crossing = 0
    for vx, y_lo, y_hi in vertical:
        if vx < x and y_lo <= y < y_hi:
            crossing += 1
    return crossing % 2 == 1

if __name__ == "__main__":
    main()