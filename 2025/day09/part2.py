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
    points_w_area = points_with_area(points)
    
    for p1, p2, a in points_w_area:
        x1, y1, x2, y2 = swap_points(p1[0], p1[1], p2[0],  p2[1])
        if check_col(perimeter, x1, y1, y2) and check_col(perimeter, x2, y1, y2) and check_row(perimeter, y1, x1, x2) and check_row(perimeter, y2, x1, x2):
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

def check_col(perimeter, x, y1, y2):
    in_out_in, ok = False, None
    ## replace y1 since the starting point is always in the perimeter
    for k in range(y1, y2 + 1):
        if ok is not None and ok == False and in_out_in:
            return False
        if (x, k) in perimeter:
            if ok == False:
                in_out_in = True
            ok = True
        else:
            ok = False
    
    if not ok:
        return True


def check_row(perimeter, y, x1, x2):
    in_out_in, ok = False, None
    for k in range(x1, x2 + 1):
        if ok is not None and ok == False and in_out_in:
            return False
        if (k, y) in perimeter:
            if ok == False:
                in_out_in = True
            ok = True
        else:
            ok = False
    
    if not ok:
        return True

if __name__ == "__main__":
    main()