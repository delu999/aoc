def main():
    matrix = gen_matrix("./2025/day07/input.txt")
    sol = solve(matrix)
    print(sol)

def gen_matrix(file_path):
    def fill_col(start_row, col_to_fill, matrix, rows):
        for k in range(start_row, rows):
            if matrix[k][col_to_fill] == '^':
                break
            matrix[k][col_to_fill] = '|'
    lines = open(file_path, "r").readlines()
    matrix = [list(line.strip()) for line in lines]

    for i, e in enumerate(matrix[0]):
        if e == 'S':
            matrix[1][i] = '|'
            break

    rows, cols = len(matrix), len(matrix[0])
    for i in range(2, rows, 2):
        for j in range(cols):
            if matrix[i][j] != '^':
                continue
            if matrix[i-1][j] == '|':
                matrix[i][j-1], matrix[i][j+1] = '|', '|'
                matrix[i-1][j] = '|' if matrix[i-2][j] == '|' else matrix[i-1][j]
            fill_col(i+1, j-1, matrix, rows)
            fill_col(i+1, j+1, matrix, rows)
    return matrix

def solve(matrix):
    beam_pos = matrix[0].index('S')
    positions = {beam_pos: 1}
    
    for row in matrix:
        new_positions = {}
        for pos, count in positions.items():
            if row[pos] == '^':
                new_positions[pos - 1] = new_positions.get(pos - 1, 0) + count
                new_positions[pos + 1] = new_positions.get(pos + 1, 0) + count
            else:
                new_positions[pos] = new_positions.get(pos, 0) + count
        positions = new_positions
    return sum(positions.values())

if __name__ == "__main__":
    main()