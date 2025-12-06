time, distance = [], []
lines = open("./2023/day06/input.txt", "r").readlines()
time, distance = lines[0].strip().split(), lines[1].strip().split()
res = 1

for i in range(1, len(time)):
    d, t = int(distance[i]), int(time[i])
    comb = 0
    for j in range(t):
        if (t - j) * j > d:
            comb += 1
    res *= comb
print(res)