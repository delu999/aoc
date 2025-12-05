sol = 0
prices = {0: 0, 1: 1, 2: 2, 3: 4, 4: 8, 5: 16, 6: 32, 7: 64, 8: 128, 9: 256, 10: 512}
for line in open("./2023/day04/input.txt"):
    clean = line.split(": ")[1]
    winning, numbers = clean.strip().split(" | ")
    winning = [w for w in winning.split(" ") if len(w) != 0]
    numbers = [w for w in numbers.split(" ") if len(w) != 0]

    count = 0
    for w in winning:
        if w in numbers:
            count += 1
    sol += prices[count]
print(sol)