def main():
    sol = 0
    for line in open("./2025/day10/input.txt", "r"):
        goal_states, presses = get_goal_and_presses(line)
        sol += solve(goal_states, presses)
    print(sol)

import re
clean_regex = re.compile(r"[\[\]()]")

def get_goal_and_presses(line: str):
    goal_states, presses = [], []
    l = [x.strip() for x in clean_regex.split(line) if x.strip()]
    
    for c in l[0]:
        goal_states.append(False if c == '.' else True)

    for i in range(1, len(l) - 1):
        default = [False for _ in range(len(goal_states))]
        buttons = l[i].split(',')
        for b in buttons:
            default[int(b)] = True
        presses.append(default)
    return goal_states, presses

def solve(goal_states, presses) -> int:
    count = 1

    return count

def press_buttons_makes_it_equal(goal_states, presses):
    initial_states = [False for _ in range(len(goal_states))]
    pr = presses.split(',')
    for i in range(len(pr)):
        initial_states[int(pr[i])] = not initial_states[int(pr[i])] 
    
    for i in range(len(initial_states)):
        if initial_states[i] != goal_states[i]:
            return False
    return True

if __name__ == "__main__":
    main()