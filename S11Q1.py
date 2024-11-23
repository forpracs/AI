def mean_end_analysis(start, goal):
    current_state = list(start)
    goal_state = list(goal)
    steps = []

    while current_state != goal_state:
        for i in range(len(current_state)):
            if current_state[i] != goal_state[i]:
                current_state[i] = chr((ord(current_state[i]) - 97 + 1) % 26 + 97)
                steps.append(''.join(current_state))
        
        if current_state == goal_state:
            break

        steps.append(''.join(current_state))

    return steps

if __name__ == "__main__":
    start_string = "abcde"
    goal_string = "vwxyz"

    result = mean_end_analysis(start_string, goal_string)

    if result:
        print(f"Transformation steps from '{start_string}' to '{goal_string}':")
        for step in result:
            print(step)
    else:
        print(f"No transformation needed. The strings are already the same.")
