depth, horizontal = 0, 0
for line in open("./2021/day02/input.txt", "r"):
    direction, qty = line.split(" ")
    if direction == "forward":
        horizontal += int(qty)
    elif direction == "up":
        depth -= int(qty)
    elif direction == "down":
        depth += int(qty)

sol = depth * horizontal
print(sol)