import heapq

class Graph:
    def __init__(self):
        self.graph = {}

    def add_edge(self, node, neighbors):
        self.graph[node] = neighbors

def astar(graph, start, goal):
    heap = [(0, start, [])]
    visited = set()

    while heap:
        (cost, current_node, path) = heapq.heappop(heap)

        if current_node in visited:
            continue

        path = path + [current_node]

        if current_node == goal:
            return path

        visited.add(current_node)

        for neighbor, neighbor_cost in graph.graph[current_node].items():
            heapq.heappush(heap, (cost + neighbor_cost, neighbor, path))

    return None

if __name__ == "__main__":
    # Example graph structure
    example_graph = Graph()
    example_graph.add_edge("A", {"B": 5, "C": 3})
    example_graph.add_edge("B", {"D": 2})
    example_graph.add_edge("C", {"D": 1})
    example_graph.add_edge("D", {"E": 4})

    start_node = "A"
    goal_node = "E"

    result = astar(example_graph, start_node, goal_node)

    if result:
        print(f"Optimal path from {start_node} to {goal_node}: {result}")
    else:
        print(f"No path found from {start_node} to {goal_node}.")