import heapq

class State:
    def __init__(self, room, remaining_rectangular, remaining_square, cost, heuristic):
        self.room = room
        self.remaining_rectangular = remaining_rectangular
        self.remaining_square = remaining_square
        self.cost = cost
        self.heuristic = heuristic

def is_valid_move(room, obj_type, row, col):
    rows, cols = len(room), len(room[0])

    if obj_type == 'rectangular':
        return row + 1 < rows and col + 2 < cols and all(room[row + i][col + j] == 0 for i in range(2) for j in range(3))
    elif obj_type == 'square':
        return row + 1 < rows and col + 1 < cols and all(room[row + i][col + j] == 0 for i in range(2) for j in range(2))

def apply_move(room, obj_type, row, col):
    if obj_type == 'rectangular':
        for i in range(2):
            for j in range(3):
                room[row + i][col + j] = 1
    elif obj_type == 'square':
        for i in range(2):
            for j in range(2):
                room[row + i][col + j] = 1

def heuristic(room, remaining_rectangular, remaining_square):
    return remaining_rectangular * 6 + remaining_square * 4  # Heuristic based on the number of empty cells

def a_star_search():
    rows, cols = 6, 6
    initial_room = [[0] * cols for _ in range(rows)]

    initial_state = State(initial_room, 5, 4, 0, heuristic(initial_room, 5, 4))
    heap = [(initial_state.cost + initial_state.heuristic, initial_state)]
    visited = set()

    while heap:
        _, current_state = heapq.heappop(heap)

        if current_state.remaining_rectangular == 0 and current_state.remaining_square == 0:
            return current_state.room

        if tuple(map(tuple, current_state.room)) in visited:
            continue

        visited.add(tuple(map(tuple, current_state.room)))

        for i in range(rows):
            for j in range(cols):
                for obj_type in ['rectangular', 'square']:
                    if is_valid_move(current_state.room, obj_type, i, j):
                        new_room = [row[:] for row in current_state.room]
                        apply_move(new_room, obj_type, i, j)
                        new_remaining_rectangular = current_state.remaining_rectangular - (1 if obj_type == 'rectangular' else 0)
                        new_remaining_square = current_state.remaining_square - (1 if obj_type == 'square' else 0)
                        new_cost = current_state.cost + 1
                        new_heuristic = heuristic(new_room, new_remaining_rectangular, new_remaining_square)
                        new_state = State(new_room, new_remaining_rectangular, new_remaining_square, new_cost, new_heuristic)
                        heapq.heappush(heap, (new_state.cost + new_state.heuristic, new_state))

    return None

def print_room(room):
    for row in room:
        print(" ".join(map(str, row)))

if __name__ == "__main__":
    final_room = a_star_search()

    if final_room:
        print("Optimal arrangement:")
        print_room(final_room)
    else:
        print("No solution found.")