from collections import Counter
l = []
for line in open("./2023/day07/input.txt", "r"):
    cards, bid = line.strip().split()
    if 'A' in cards:
        cards = cards.replace('A', 'Z')
    if 'K' in cards:
        cards = cards.replace('K', 'Y')
    if 'Q' in cards:
        cards = cards.replace('Q', 'X')
    if 'J' in cards:
        cards = cards.replace('J', 'W')
    if 'T' in cards:
        cards = cards.replace('T', 'V')

    cards_eval = Counter(cards)
    cards_len = len(cards_eval)

    if cards_len == 1:
        l.append({"card": cards, "bid": int(bid), "order": 6}) # five of a kind
    elif cards_len == 2:
        if 4 in cards_eval.values():
            l.append({"card": cards, "bid": int(bid), "order": 5}) # poker
        else:
            l.append({"card": cards, "bid": int(bid), "order": 4}) # full
    elif cards_len == 3:
        if 3 in cards_eval.values():
            l.append({"card": cards, "bid": int(bid), "order": 3}) # tris
        else:
            l.append({"card": cards, "bid": int(bid), "order": 2}) # doppia coppia
    elif cards_len == 4:
        l.append({"card": cards, "bid": int(bid), "order": 1}) # coppia
    else:
        l.append({"card": cards, "bid": int(bid), "order": 0}) # carta più alta

l.sort(key=lambda x: x["order"])
done = []
count = 0
def insert_ordered(el):
    pos = 0
    found = False
    for i, d in enumerate(done):
        if d["order"] == el["order"] and el["card"] < d["card"]:
            pos = i
            found = True
            break
    if found:
        done.insert(pos, el)
    else:
        done.append(el)

for i, el in enumerate(l):
    insert_ordered(el)

sol = 0
for i, e in enumerate(done):
    print(e["card"])
    sol += (i+1) * e["bid"]

print(sol)