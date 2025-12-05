f = open("2020/day1/input.txt", "r")

numbers = set()
while True:
    l = f.readline()
    if l == '':
        break
    a = int(l)
    b = 2020 - a

    if b in numbers:
        print(a * b)
        break
    
    numbers.add(a)