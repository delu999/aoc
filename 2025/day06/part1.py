matrix = []
for line in open("./2025/day06/input.txt", "r"):
    matrix.append(line.split())

rows = len(matrix)
cols = len(matrix[0])
res, count = 0, 0

for i in range(cols):
    if matrix[rows-1][i] == '*':
        count = 1
        for j in range(rows-1):
            count *= int(matrix[j][i])
    else:
        count = 0
        for j in range(rows-1):
            count += int(matrix[j][i])    
    res += count
print(res)