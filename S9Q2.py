def water_jug_problem(jug1, jug2, target):
    def pour(jug1, jug2):
        # Pour water from jug1 to jug2
        if jug1[0] > 0 and jug2[1] < jug2[2]:
            amount = min(jug1[0], jug2[2] - jug2[1])
            jug1[0] -= amount
            jug2[1] += amount
            yield jug1, jug2

        # Pour water from jug2 to jug1
        if jug2[1] > 0 and jug1[0] < jug1[1]:
            amount = min(jug2[1], jug1[1] - jug1[0])
            jug2[1] -= amount
            jug1[0] += amount
            yield jug1, jug2

    def dfs(current_state, visited):
        if current_state[0][0] == target or current_state[1][0] == target:
            return [current_state[0][0], current_state[1][0]]

        visited.add((current_state[0][0], current_state[1][0]))

        for next_state in pour(*current_state):
            if (next_state[0][0], next_state[1][0]) not in visited:
                result = dfs(next_state, visited)
                if result:
                    return [current_state[0][0], current_state[1][0]] + result

        return None

    initial_state = [[0, 5], [0, 7]]
    final_state = dfs(initial_state, set())

    if final_state:
        print(f"Solution found: {final_state[0]} gallons in the 5-gallon jug and {final_state[1]} gallons in the 7-gallon jug.")
    else:
        print("No solution found.")

if __name__ == "__main__":
    water_jug_problem(5, 7, 4)