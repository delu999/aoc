depth, horizontal, aim = 0, 0, 0
for line in open("./2021/day02/input.txt", "r"):
    direction, qty = line.split(" ")
    if direction == "forward":
        qty = int(qty)
        horizontal += qty
        depth += aim * qty
    elif direction == "up":
        aim -= int(qty)
    elif direction == "down":
        aim += int(qty)

sol = depth * horizontal
print(sol)