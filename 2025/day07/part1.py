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
            matrix[i][j-1] = '|'
            matrix[i][j+1] = '|'
        elif matrix[i-2][j] == '|':
            sol += 1
            matrix[i-1][j] = '|'
            matrix[i][j-1] = '|'
            matrix[i][j+1] = '|'  
        for k in range(i+1, rows):
            if matrix[k][j-1] == '^':
                break
            matrix[k][j-1] = '|'
        for k in range(i+1, rows):
            if matrix[k][j+1] == '^':
                break
            matrix[k][j+1] = '|'           
print(sol)