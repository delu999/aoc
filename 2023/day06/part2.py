lines = open("./2023/day06/input.txt", "r").readlines()
time, distance = lines[0].strip().split(), lines[1].strip().split()
res, t, d = 1, "", ""
for i in range(1, len(time)):
    t += time[i]
    d += distance[i]

d, t = int(d), int(t)
comb = 0
for j in range(t):
    if (t - j) * j > d:
        comb += 1
res *= comb
print(res)