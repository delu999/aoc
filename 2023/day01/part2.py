nums = {
    "one": 1,
    "two": 2,
    "three": 3,
    "four": 4,
    "five": 5,
    "six": 6,
    "seven": 7,
    "eight": 8,
    "nine": 9
}

def get_first_digit(s: str) -> int:
    num_pos, num_string_pos = -1, -1
    for i, c in enumerate(s):
        if c.isdigit():
            num_pos = i
            break
    
    pos = []
    for key, value in nums.items():
        if (index := s.find(key)) != -1:
            pos.append((index, value))
    
    if not pos:
        return int(s[num_pos])
     
    num_string_pos, value = min(pos)

    if num_pos == -1 or num_string_pos < num_pos:
        return value

    return int(s[num_pos])
    

def get_last_digit(s: str) -> int:
    num_pos, num_string_pos = -1, -1
    for i, c in enumerate(s):
        if c.isdigit():
            num_pos = i
    
    pos = []
    a = s[::-1]
    for key, value in nums.items():
        if (index := a.find(key[::-1])) != -1:
            pos.append((index, value))
    
    if not pos:
        return int(s[num_pos])

    num_string_pos, value = min(pos)

    if num_pos == -1 or len(s)-num_string_pos > num_pos:
        return value

    return int(s[num_pos]) 

count = 0
for line in open("./2023/day1/input.txt", "r"):
    count += (get_first_digit(line) * 10) + get_last_digit(line)
print(count)