import heapq
from typing import List, Tuple

class PuzzleState:
    def __init__(self, board: List[List[int]]):
        self.board = board
        self.size = len(board)
        self.goal = [[1, 2, 3], [4, 5, 6], [7, 8, 0]]

    def __eq__(self, other):
        return self.board == other.board

    def __hash__(self):
        return hash(tuple(tuple(row) for row in self.board))

    def __lt__(self, other):
        return False

    def find_blank(self) -> Tuple[int, int]:
        for i in range(self.size):
            for j in range(self.size):
                if self.board[i][j] == 0:
                    return i, j

    def is_goal(self) -> bool:
        return self.board == self.goal

    def generate_successors(self) -> List["PuzzleState"]:
        successors = []
        i, j = self.find_blank()

        # Check possible moves: left, right, up, down
        moves = [(0, -1), (0, 1), (-1, 0), (1, 0)]

        for move in moves:
            ni, nj = i + move[0], j + move[1]

            if 0 <= ni < self.size and 0 <= nj < self.size:
                new_board = [row.copy() for row in self.board]
                new_board[i][j], new_board[ni][nj] = new_board[ni][nj], new_board[i][j]
                successors.append(PuzzleState(new_board))

        return successors

def manhattan_distance(state: PuzzleState) -> int:
    distance = 0
    for i in range(state.size):
        for j in range(state.size):
            value = state.board[i][j]
            if value != 0:
                goal_i, goal_j = divmod(value - 1, state.size)
                distance += abs(i - goal_i) + abs(j - goal_j)
    return distance

def a_star_search(initial_state: PuzzleState) -> List[PuzzleState]:
    heap = [(0, 0, initial_state)]
    visited = set()

    while heap:
        _, cost, current_state = heapq.heappop(heap)

        if current_state.is_goal():
            path = []
            while current_state:
                path.append(current_state)
                current_state = current_state.parent
            return path[::-1]

        if current_state not in visited:
            visited.add(current_state)

            for successor in current_state.generate_successors():
                if successor not in visited:
                    successor.cost = cost + 1
                    successor.heuristic = manhattan_distance(successor)
                    successor.parent = current_state
                    heapq.heappush(heap, (successor.cost + successor.heuristic, successor.cost, successor))

    return []

def print_solution(solution: List[PuzzleState]):
    for state in solution:
        for row in state.board:
            print(" ".join(map(str, row)))
        print()

if __name__ == "__main__":
    initial_board = [
        [1, 2, 3],
        [4, 5, 6],
        [7, 8, 0]
    ]

    initial_state = PuzzleState(initial_board)
    initial_state.cost = 0
    initial_state.heuristic = manhattan_distance(initial_state)

    solution = a_star_search(initial_state)

    if solution:
        print("Solution found:")
        print_solution(solution)
    else:
        print("No solution found.")
