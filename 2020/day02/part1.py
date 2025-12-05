solution = 0
for line in open("./2020/day02/input.txt", "r"):
    range, letter, password = line.split(" ")
    start, end = range.split("-")
    start, end = int(start), int(end)
    letter = letter[0]
    password.strip()
    
    count = 0
    for e in password:
        if e == letter:
            count += 1
    
    if count >= start and count <= end:
        solution += 1

print(solution)