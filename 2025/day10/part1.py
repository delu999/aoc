def main():
    goal_states, presses = parse_input("./2025/day10/input.txt")
    print(goal_states)
    print(presses)
    sol = solve(goal_states)
    print(sol)

def parse_input(file_path: str):
    goal_states, presses = [], []
    for line in open(file_path, "r"):
        l = line.strip().split()
        state = []
        for c in l[0]:
            if c != '[' and c != ']':
                state.append(False if c == '.' else True)
        goal_states.append(state)
        presses.append(l[1::])
    return goal_states, presses

def solve(lines) -> int:
    return 0

if __name__ == "__main__":
    main()