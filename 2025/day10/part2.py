import re
import sys
clean_regex = re.compile(r"[\[\]{}()]")

def main():
    sol = 0
    for line in open("./2025/day10/input.txt"):
        goal_states, presses = get_goal_and_presses(line)
        sol += solve(goal_states, presses)
    print(sol)

def get_goal_and_presses(line: str):
    goal_states, presses = [], []
    l = [x.strip() for x in clean_regex.split(line) if x.strip()]
    
    goal_states = [int(el) for el in l[len(l) - 1].split(",")]
    for i in range(1, len(l) - 1):
        default = [0 for _ in range(len(goal_states))]
        buttons = l[i].split(',')
        for b in buttons:
            default[int(b)] = 1
        presses.append(default)

    return goal_states, presses

import z3
def solve(goal_states, presses) -> int:
    s, vars = z3.Optimize(), []
    
    for i in range(len(presses)):
        var = z3.Int("a" + str(i))
        s.add(var >= 0)
        vars.append(var)

    # build the equation by replacing the 1's with a coefficient
    for i in range(len(presses)):
        for j in range(len(presses[i])):
            presses[i][j] = vars[i] if presses[i][j] == 1 else 0
    
    zipped = list(zip(*presses))

    for zipp, r in zip(zipped, goal_states):
        s.add(z3.Sum(zipp) == r)

    s.minimize(z3.Sum(vars))
    if s.check() == z3.sat:
        m = s.model()
        return sum(m.eval(var, model_completion=True).as_long() for var in vars)
    return 0

if __name__ == "__main__":
    main()