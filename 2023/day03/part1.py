import re
regex_for_numbers = re.compile(r'\d+')

dir = [(-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1), (1, 0), (1, 1)]
symbols = ['#', '$', '%', '*', '+', '-', '&', '/', '=', '@']
matrix = []

for i, line in enumerate(open("./2023/day03/input.txt", "r")):
    matrix.append(list(line.strip()))

rows = len(matrix)
cols = len(matrix[0])
count = 0

for i, line in enumerate(open("./2023/day03/input.txt", "r")):
    nums = regex_for_numbers.findall(line)

    for n in nums:
        good = False
        s = line.find(n)
        start = line.find(n) - 1
        for c in n:
            start += 1
            if good:
                break
            for x, y in dir:
                posx, posy = i + x, start + y
                if posx >= 0 and posy >= 0 and posx < rows and posy < cols:
                    if matrix[posx][posy] in symbols:
                        good = True
                        break
        
        chars = list(line)
        while chars[s].isdigit():
            chars[s] = "."
            s += 1
        line = "".join(chars) 
        if good:
            count += int(n)
print(count)