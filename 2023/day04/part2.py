cards = []
for i, line in enumerate(open("./2023/day04/input.txt")):
    clean = line.split(": ")[1]
    winning, numbers = clean.strip().split(" | ")
    winning = [w for w in winning.split(" ") if len(w) != 0]
    numbers = [w for w in numbers.split(" ") if len(w) != 0]

    count = 0
    for w in winning:
        if w in numbers:
            count += 1
    cards.append(count)

len_cards = len(cards)
copies = [1 for _ in range(len_cards)]

for i in range(0, len_cards):
    for j in range(i + 1, i + 1 + cards[i]):
        if j < len_cards:
            copies[j] += copies[i]
sol = sum(copies)
print(sol)