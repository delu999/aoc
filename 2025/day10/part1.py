import re
import itertools as it
clean_regex = re.compile(r"[\[\]()]")

def main():
    sol = 0
    for line in open("./2025/day10/input.txt", "r"):
        goal_states, presses = get_goal_and_presses(line)
        sol += solve(goal_states, presses)
    print(sol)

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
    count, goals = 1, len(goal_states)
    while True:
        for e in it.permutations(presses, count):
            initial_states = [False] * goals
            for el in e:
                for i in range(goals):
                    initial_states[i] ^= el[i]
            if (check_equality(initial_states, goal_states)):
                return count
        count += 1

def check_equality(states1, states2):
    for i in range(len(states1)):
        if states1[i] != states2[i]:
            return False
    return True

if __name__ == "__main__":
    main()