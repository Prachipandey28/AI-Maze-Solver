import time
import matplotlib.pyplot as plt
from matplotlib.colors import ListedColormap
import numpy as np
import heapq
from collections import deque


# ==========================================
# 1. CREATE THE MAZE
# ==========================================

maze = [
    ['S', 0, 1, 0, 0],
    [1,   0, 1, 0, 1],
    [0,   0, 0, 0, 0],
    [0,   1, 1, 1, 0],
    [0,   0, 0, 'G', 0]
]


# ==========================================
# 2. FIND START AND GOAL POSITIONS
# ==========================================

def find_position(maze, symbol):
    for r in range(len(maze)):
        for c in range(len(maze[0])):
            if maze[r][c] == symbol:
                return (r, c)

    return None


# ==========================================
# 3. GET VALID NEIGHBOURS
# ==========================================

def get_neighbours(maze, position):
    r, c = position

    directions = [
        (-1, 0),  # Up
        (1, 0),   # Down
        (0, -1),  # Left
        (0, 1)    # Right
    ]

    neighbours = []

    for dr, dc in directions:
        nr = r + dr
        nc = c + dc

        if (
            0 <= nr < len(maze)
            and 0 <= nc < len(maze[0])
            and maze[nr][nc] != 1
        ):
            neighbours.append((nr, nc))

    return neighbours


# ==========================================
# 4. BREADTH-FIRST SEARCH (BFS)
# ==========================================

def bfs(maze):
    start = find_position(maze, 'S')
    goal = find_position(maze, 'G')

    queue = deque([(start, [start])])
    visited = {start}

    while queue:
        current, path = queue.popleft()

        if current == goal:
            return path

        for neighbour in get_neighbours(maze, current):
            if neighbour not in visited:
                visited.add(neighbour)
                queue.append((neighbour, path + [neighbour]))

    return None


# ==========================================
# 5. DEPTH-FIRST SEARCH (DFS)
# ==========================================

def dfs(maze):
    start = find_position(maze, 'S')
    goal = find_position(maze, 'G')

    stack = [(start, [start])]
    visited = {start}

    while stack:
        current, path = stack.pop()

        if current == goal:
            return path

        for neighbour in get_neighbours(maze, current):
            if neighbour not in visited:
                visited.add(neighbour)
                stack.append((neighbour, path + [neighbour]))

    return None


# ==========================================
# 6. UNIFORM-COST SEARCH (UCS)
# ==========================================

weighted_graph = {
    'S': [('A', 2), ('B', 1)],
    'A': [('G', 2)],
    'B': [('C', 1)],
    'C': [('G', 1)],
    'G': []
}


def ucs(graph, start, goal):
    priority_queue = [(0, start, [start])]
    best_cost = {start: 0}

    while priority_queue:
        cost, current, path = heapq.heappop(priority_queue)

        if current == goal:
            return path, cost

        if cost > best_cost.get(current, float('inf')):
            continue

        for neighbour, edge_cost in graph[current]:
            new_cost = cost + edge_cost

            if new_cost < best_cost.get(neighbour, float('inf')):
                best_cost[neighbour] = new_cost

                heapq.heappush(
                    priority_queue,
                    (new_cost, neighbour, path + [neighbour])
                )

    return None, float('inf')


# ==========================================
# 7. VISUALIZE THE MAZE
# ==========================================

def visualize_maze(maze, path=None, algorithm="Maze Solver"):
    rows = len(maze)
    cols = len(maze[0])

    grid = np.zeros((rows, cols))

    # Mark walls
    for r in range(rows):
        for c in range(cols):
            if maze[r][c] == 1:
                grid[r][c] = 1

    # Mark solution path
    if path:
        for r, c in path:
            if maze[r][c] not in ('S', 'G'):
                grid[r][c] = 2

    colors = [
        'white',       # Empty cell
        'black',       # Wall
        'deepskyblue'  # Path
    ]

    cmap = ListedColormap(colors)

    fig, ax = plt.subplots(figsize=(7, 7))

    ax.imshow(grid, cmap=cmap, vmin=0, vmax=2)

    # Add cell labels
    for r in range(rows):
        for c in range(cols):
            if maze[r][c] == 'S':
                ax.text(
                    c, r, 'S',
                    ha='center', va='center',
                    color='green', fontsize=16, fontweight='bold'
                )

            elif maze[r][c] == 'G':
                ax.text(
                    c, r, 'G',
                    ha='center', va='center',
                    color='red', fontsize=16, fontweight='bold'
                )

    # Draw grid lines
    ax.set_xticks(np.arange(-0.5, cols, 1), minor=True)
    ax.set_yticks(np.arange(-0.5, rows, 1), minor=True)
    ax.grid(which='minor', color='gray', linewidth=1)

    ax.set_xticks([])
    ax.set_yticks([])

    ax.set_title(f"AI Maze Solver - {algorithm}")

    plt.tight_layout()
    plt.show()


# ==========================================
# 8. RUN BFS
# ==========================================

bfs_path = bfs(maze)

print("\n========== BFS ==========")
print("BFS Path:", bfs_path)
print(
    "BFS Moves:",
    len(bfs_path) - 1 if bfs_path else "No path found"
)

visualize_maze(maze, bfs_path, "BFS")


# ==========================================
# 9. RUN DFS
# ==========================================

dfs_path = dfs(maze)

print("\n========== DFS ==========")
print("DFS Path:", dfs_path)
print(
    "DFS Moves:",
    len(dfs_path) - 1 if dfs_path else "No path found"
)

visualize_maze(maze, dfs_path, "DFS")



# ==========================================
# 11. GREEDY BEST-FIRST SEARCH (GBFS)
# ==========================================

def heuristic(position, goal):
    r1, c1 = position
    r2, c2 = goal

    return abs(r1 - r2) + abs(c1 - c2)


def greedy_best_first_search(maze):
    start = find_position(maze, 'S')
    goal = find_position(maze, 'G')

    # Priority queue: (heuristic value, position, path)
    priority_queue = [
        (heuristic(start, goal), start, [start])
    ]

    visited = {start}

    while priority_queue:
        _, current, path = heapq.heappop(priority_queue)

        if current == goal:
            return path

        for neighbour in get_neighbours(maze, current):
            if neighbour not in visited:
                visited.add(neighbour)

                h = heuristic(neighbour, goal)

                heapq.heappush(
                    priority_queue,
                    (h, neighbour, path + [neighbour])
                )

    return None


# ==========================================
# 13. A* SEARCH ALGORITHM
# ==========================================

def a_star_search(maze):
    start = find_position(maze, 'S')
    goal = find_position(maze, 'G')

    # Priority queue: (f_score, g_score, position, path)
    priority_queue = [
        (heuristic(start, goal), 0, start, [start])
    ]

    best_cost = {start: 0}

    while priority_queue:
        f_score, g_score, current, path = heapq.heappop(
            priority_queue
        )

        # Ignore an outdated queue entry
        if g_score > best_cost.get(current, float('inf')):
            continue

        # Goal reached
        if current == goal:
            return path

        for neighbour in get_neighbours(maze, current):
            new_cost = g_score + 1

            if new_cost < best_cost.get(
                neighbour, float('inf')
            ):
                best_cost[neighbour] = new_cost

                h_score = heuristic(neighbour, goal)
                f_score = new_cost + h_score

                heapq.heappush(
                    priority_queue,
                    (
                        f_score,
                        new_cost,
                        neighbour,
                        path + [neighbour]
                    )
                )

    return None



# ==========================================
# 10. RUN UCS
# ==========================================

ucs_path, ucs_cost = ucs(weighted_graph, 'S', 'G')

print("\n========== UCS ==========")
print("UCS Path:", ucs_path)
print("UCS Total Cost:", ucs_cost)


# ==========================================
# 12. RUN GREEDY BEST-FIRST SEARCH
# ==========================================

greedy_path = greedy_best_first_search(maze)

print("\n========== GREEDY BEST-FIRST SEARCH ==========")
print("Greedy Path:", greedy_path)

print(
    "Greedy Moves:",
    len(greedy_path) - 1 if greedy_path else "No path found"
)

visualize_maze(maze, greedy_path, "Greedy Best-First Search")


# ==========================================
# 14. RUN A* SEARCH
# ==========================================

a_star_path = a_star_search(maze)

print("\n========== A* SEARCH ==========")
print("A* Path:", a_star_path)

print(
    "A* Moves:",
    len(a_star_path) - 1 if a_star_path else "No path found"
)

visualize_maze(maze, a_star_path, "A* Search")


# ==========================================
# 15. COMPARE SEARCH ALGORITHMS
# ==========================================

results = []

# Compare algorithms that solve the grid maze
maze_algorithms = [
    ("BFS", bfs),
    ("DFS", dfs),
    ("Greedy Best-First", greedy_best_first_search),
    ("A*", a_star_search)
]

for name, algorithm in maze_algorithms:
    start_time = time.perf_counter()

    path = algorithm(maze)

    end_time = time.perf_counter()
    execution_time = (end_time - start_time) * 1000

    moves = len(path) - 1 if path else "No path"

    results.append([
        name,
        "Grid Maze",
        moves,
        "-",
        f"{execution_time:.4f} ms"
    ])


# Measure UCS separately on the weighted graph
start_time = time.perf_counter()

ucs_path, ucs_cost = ucs(weighted_graph, 'S', 'G')

end_time = time.perf_counter()
execution_time = (end_time - start_time) * 1000

ucs_moves = len(ucs_path) - 1 if ucs_path else "No path"
ucs_cost_display = ucs_cost if ucs_path else "No path"

results.append([
    "UCS",
    "Weighted Graph",
    ucs_moves,
    ucs_cost_display,
    f"{execution_time:.4f} ms"
])


# Display comparison table
print("\n========== ALGORITHM COMPARISON ==========")

headers = [
    "Algorithm",
    "Problem",
    "Path Length",
    "Total Cost",
    "Time"
]

print("-" * 86)
print(
    f"{headers[0]:<20}"
    f"{headers[1]:<18}"
    f"{headers[2]:<15}"
    f"{headers[3]:<13}"
    f"{headers[4]:<15}"
)
print("-" * 86)

for row in results:
    print(
        f"{row[0]:<20}"
        f"{row[1]:<18}"
        f"{str(row[2]):<15}"
        f"{str(row[3]):<13}"
        f"{row[4]:<15}"
    )

print("-" * 86)


