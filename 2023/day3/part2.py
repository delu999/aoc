import re
top = [(-1, -1), (-1, 0), (-1, 1)]
bottom = [(1, -1), (1, 0), (1, 1)]
lateral = [(0, -1), (0, 1)]
cross = [(0, -1), (0, 1), (-1, 0), (1, 0)]

def is_valid(row, col):
    list = []
    for x, y in lateral:
        posx, posy = row + x, col + y
        if posx >= 0 and posy >= 0 and posx < rows and posy < cols and matrix[posx][posy].isdigit():
            list.append((posx, posy))
     
    
    posx, posy = row - 1, col
    if posx >= 0 and posy >= 0 and posx < rows and posy < cols and matrix[posx][posy].isdigit():
        list.append((posx, posy))
    else:
        posx, posy = row - 1, col - 1
        if posx >= 0 and posy >= 0 and posx < rows and posy < cols and matrix[posx][posy].isdigit():
            list.append((posx, posy))
        
        posx, posy = row - 1, col + 1
        if posx >= 0 and posy >= 0 and posx < rows and posy < cols and matrix[posx][posy].isdigit():
            list.append((posx, posy))

    posx, posy = row + 1, col
    if posx >= 0 and posy >= 0 and posx < rows and posy < cols and matrix[posx][posy].isdigit():
        list.append((posx, posy))
    else:
        posx, posy = row + 1, col - 1
        if posx >= 0 and posy >= 0 and posx < rows and posy < cols and matrix[posx][posy].isdigit():
            list.append((posx, posy))
        
        posx, posy = row + 1, col + 1
        if posx >= 0 and posy >= 0 and posx < rows and posy < cols and matrix[posx][posy].isdigit(): 
            list.append((posx, posy))
    return list

def solve():
    regex_for_numbers = re.compile(r'\d+')
    count = 0
    for i in range(0, rows):
        for j in range(0, cols):
            if not matrix[i][j] == '*':
                continue
            pos_list = is_valid(i, j)
            if len(pos_list) != 2:
                continue

            gear_ratio = 1 
            for x, y in pos_list:
                left = y
                right = y
                while True:
                    if left < 0:
                        left = 0
                        break
                
                    if matrix[x][left].isdigit():
                        left -= 1
                    else:
                        left += 1
                        break
                while True:
                    if right >= cols:
                        right = cols
                        break
                
                    if matrix[x][right].isdigit():
                        right += 1
                    else:
                        break
                gear_ratio *= int("".join(matrix[x][left:right])) 
            count += gear_ratio
    
    
    return count

matrix = []
rows = 0
cols = 0

def main():
    global rows, cols
    for line in open("./2023/day3/input.txt", "r"):
        matrix.append(list(line.strip()))
    rows = len(matrix)
    cols = len(matrix[0])  
    count = solve()
    print(count)

if __name__ == "__main__":
    main()