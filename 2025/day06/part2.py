matrix = []
for line in open("./2025/day06/input.txt", "r"):
    matrix.append(list(line.strip("\n")))

rows, cols, sol, sum = len(matrix), len(matrix[0]), 0, 0

for i in range(cols):
    if matrix[rows-1][i] != ' ':
        op = matrix[rows-1][i]
        sum = 1 if op == '*' else 0

    s = "".join([matrix[j][i] for j in range(rows - 1)])

    if (s := s.strip()) != "":
        sum = sum * int(s) if op == '*' else sum + int(s)
    else:
        sol += sum
sol += sum
print(sol)