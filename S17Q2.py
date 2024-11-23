def objective_function(x):
    return -(x ** 4) + 4 * (x ** 3) - 6 * (x ** 2) + 4 * x

def hill_climbing(initial_x, step_size, max_iterations):
    current_x = initial_x

    for _ in range(max_iterations):
        current_value = objective_function(current_x)
        next_x = current_x + step_size
        next_value = objective_function(next_x)

        if next_value > current_value:
            current_x = next_x
        else:
            break

    return current_x, objective_function(current_x)

if __name__ == "__main__":
    initial_x = float(input("Enter the initial value of x: "))
    step_size = float(input("Enter the step size: "))
    max_iterations = int(input("Enter the maximum number of iterations: "))

    result_x, result_value = hill_climbing(initial_x, step_size, max_iterations)

    print("\nHill Climbing Results:")
    print(f"Optimal x: {result_x}")
    print(f"Optimal value: {result_value}")