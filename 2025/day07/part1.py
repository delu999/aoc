def fill_col(start_row, col_to_fill):
    for k in range(start_row, rows):
        if matrix[k][col_to_fill] == '^':
            break
        matrix[k][col_to_fill] = '|'

lines = open("./2025/day07/input.txt", "r").readlines()
matrix = [list(line.strip()) for line in lines]

for i, e in enumerate(matrix[0]):
    if e == 'S':
        matrix[1][i] = '|'
        break

sol = 0
rows, cols = len(matrix), len(matrix[0])
for i in range(2, rows, 2):
    for j in range(cols):
        if matrix[i][j] != '^':
            continue
        if matrix[i-1][j] == '|':
            sol += 1
            matrix[i][j-1], matrix[i][j+1] = '|', '|'
            matrix[i-1][j] = '|' if matrix[i-2][j] == '|' else matrix[i-1][j]
        fill_col(i+1, j-1)
        fill_col(i+1, j+1)
print(sol)