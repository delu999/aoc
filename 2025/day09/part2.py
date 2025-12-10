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
    area_points = gen_matrix(points)
    print("done")
    points_w_area = points_with_area(points)
    
    for p1, p2, a in points_w_area:
        x1, y1, x2, y2 = p1[0], p1[1], p2[0],  p2[1]

        if x1 == x2:
            if y1 > y2:
                y2, y1 = y1, y2
            if check_col(area_points, x1, y1, y2):
                return a
            continue
        if y1 == y2:
            if x2 > x1:
                x2, x1 = x1, x2
            if check_row(area_points, y1, x1, x2):
                return a
            continue

        x1, y1, x2, y2 = swap_points(x1, y1, x2, y2)
        if check_col(area_points, x1, y1, y2) and check_col(area_points, x2, y1, y2) and check_row(area_points, y1, x1, x2) and check_row(area_points, y2, x1, x2):
            return a
    return -1

def gen_matrix(points) -> set[tuple[int, int]]:
    n = len(points)
    tmp_perimeter = set()
    for i in range(n):
        x1, y1, x2, y2 = points[i][0], points[i][1], points[(i + 1) % n][0], points[(i + 1) % n][1]
        if x1 == x2:
            if y1 > y2:
                y1, y2 = y2, y1
            
            for k in range(y1, y2 + 1):
                tmp_perimeter.add((k, x1))
        else:
            if x1 > x2:
                x1, x2 = x2, x1
            
            for k in range(x1, x2 + 1):
                tmp_perimeter.add((y1, k))
    
    tmp_perimeter = list(tmp_perimeter)
    nn = len(tmp_perimeter)
    perimeter = set()
    
    for i in range(nn):
        for j in range(i + 1, nn):
            x, y1, x2, y2 = tmp_perimeter[i][0], tmp_perimeter[i][1], tmp_perimeter[j][0],  tmp_perimeter[j][1]
            if x != x2:
                continue
            
            if y1 > y2:
                y2, y1 = y1, y2
            
            switch, ok = 0, False
            for k in range(y1, y2 + 1):
                if switch == 2:
                    break
                if (x, k) in tmp_perimeter:
                    switch += 1
                    ok = True
                else:
                    switch = 0
                    ok = False
            if ok:
                for k in range(y1, y2 + 1):
                    perimeter.add((x, k))
    print("done3")
    area = set(perimeter)
    return area

def swap_points(x1, y1, x2, y2) -> tuple[int, int, int, int]:
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

def check_row(area_points, x, y1, y2):
    for i in range(y1, y2 + 1):
        if (x, i) not in area_points:
            return False
    return True

def check_col(area_points, y, x1, x2):
    for j in range(x1, x2 + 1):
        if (j, y) not in area_points:
            return False
    return True  


if __name__ == "__main__":
    main()