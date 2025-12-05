def get_first_digit(s: str) -> int:
    for i in s:
        if i.isdigit():
            return int(i)
    return 0

count = 0
for line in open("./2023/day1/input.txt", "r"):
    count += (get_first_digit(line) * 10) + get_first_digit(line[::-1])
print(count)