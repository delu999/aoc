f = open("2021/day01/input.txt", "r")
lines = f.readlines()

answer = 0

for i in range(1, len(lines)):
    if int(lines[i]) > int(lines[i - 1]):
        answer += 1

print(answer)