 <div align="center">

# 🧠 AI MAZE SOLVER

### Find the Path. Explore the Search Space. Let AI Do the Thinking.

A visual Artificial Intelligence project that solves mazes using classic AI search algorithms, built with Python and Matplotlib.

![Python](https://img.shields.io/badge/Python-3.10%2B-3776AB?style=for-the-badge&logo=python&logoColor=white)
![AI](https://img.shields.io/badge/Artificial_Intelligence-Search_Algorithms-8A2BE2?style=for-the-badge)
![Matplotlib](https://img.shields.io/badge/Visualization-Matplotlib-11557C?style=for-the-badge)
![Status](https://img.shields.io/badge/Status-Active_Development-20A464?style=for-the-badge)

**Can an AI find its way through a maze? Let's find out! 🧩**

</div>

---

## 🌟 Overview

**AI Maze Solver** is a Python-based project that demonstrates how Artificial Intelligence search algorithms explore a maze and discover a path from a starting point to a goal.

The project implements both **uninformed search** and **informed search** techniques. It visualizes the solution path and prints the coordinates, number of moves, and execution time in the terminal.

The goal is to understand how different search strategies make decisions, explore states, and solve pathfinding problems.

## 🎬 Project in Action

### 🟦 BFS Maze Visualization

The visualization uses different colors to make the maze easy to understand.

![AI Maze Solver BFS Screenshot](assets/maze-solver-bfs.png)

**Color Legend**

| Color / Symbol | Meaning |
|---|---|
| 🟩 `S` | Starting position |
| 🟥 `G` | Goal position |
| ⬛ Black | Wall or blocked cell |
| 🟦 Blue | Solution path |
| ⬜ White | Walkable cell |

*The screenshot above demonstrates the BFS solution path from the start to the goal.*

---

## ✨ Features

- 🧭 **Multiple AI Search Algorithms** — BFS, DFS, UCS, Greedy Best-First Search, and A*.
- 🧱 **Grid-Based Maze** — walls, walkable cells, a start point, and a goal.
- 🎨 **Visual Pathfinding** — solution paths displayed using Matplotlib.
- 📍 **Path Reconstruction** — prints the sequence of coordinates or graph nodes.
- 👣 **Move Counting** — calculates the number of moves in a maze solution.
- ⚖️ **Cost-Based Search** — demonstrates Uniform-Cost Search on a weighted graph.
- ⏱️ **Performance Measurement** — records execution time for algorithm comparisons.
- 🧑‍💻 **Beginner-Friendly Code** — each search algorithm is implemented in a separate function.

## 🧠 AI Algorithms Implemented

### 1. Breadth-First Search (BFS)

Explores neighbouring states level by level using a queue.

- Finds a shortest path when every move has the same cost.
- Useful for unweighted pathfinding problems.

### 2. Depth-First Search (DFS)

Explores one branch deeply before backtracking, using a stack.

- Demonstrates depth-first exploration.
- Does not guarantee the shortest path.

### 3. Uniform-Cost Search (UCS)

Expands the node with the lowest accumulated path cost using a priority queue.

- Finds a minimum-cost path when edge costs are non-negative.
- Currently demonstrated using a separate weighted graph.

### 4. Greedy Best-First Search

Uses a heuristic to choose the position estimated to be closest to the goal.

The project uses Manhattan distance:

`h(n) = |row - goal_row| + |column - goal_column|`

- Uses goal-directed search.
- Does not guarantee the shortest path.

### 5. A* Search

Combines the cost already travelled with the estimated cost remaining.

**Evaluation function:**

`f(n) = g(n) + h(n)`

Where:

- `g(n)` = actual cost from the start to the current position.
- `h(n)` = estimated cost from the current position to the goal.
- `f(n)` = estimated total cost of the path through that position.

With unit-cost grid movements and an admissible Manhattan-distance heuristic, A* can find an optimal path.

## 📊 Algorithm Comparison

| Algorithm | Search Type | Main Data Structure | Shortest / Cheapest Path? |
|---|---|---|---|
| BFS | Uninformed | Queue | Yes, for equal-cost moves |
| DFS | Uninformed | Stack | Not guaranteed |
| UCS | Uninformed, cost-based | Priority queue | Yes, for non-negative edge costs |
| Greedy Best-First | Informed | Priority queue | Not guaranteed |
| A* | Informed | Priority queue | Yes, under suitable conditions |

> **Implementation note:** BFS, DFS, Greedy Best-First Search, and A* currently solve the grid maze. UCS runs on a separate weighted graph. Therefore, their path lengths and costs should not be compared directly until UCS is integrated into the same maze.

---

## 🗺️ How the Maze Works

The maze is represented as a two-dimensional Python list.

```python
maze = [
    ['S', 0, 1, 0, 0],
    [1,   0, 1, 0, 1],
    [0,   0, 0, 0, 0],
    [0,   1, 1, 1, 0],
    [0,   0, 0, 0, 'G']
]
```

**Cell meanings:**

- `'S'` — start position
- `'G'` — goal position
- `0` — walkable cell
- `1` — wall

The algorithms explore valid neighbouring cells while avoiding walls and tracking visited positions.

## ⚙️ Tech Stack

| Technology | Purpose |
|---|---|
| Python | Core implementation |
| `collections.deque` | BFS queue |
| `heapq` | Priority queues for UCS, Greedy, and A* |
| NumPy | Grid representation for visualization |
| Matplotlib | Maze rendering and path visualization |
| `time` | Execution-time measurement |

## 🚀 Getting Started

### Prerequisites

- Python 3.10 or newer recommended
- Git
- VS Code or another Python editor

### 1. Clone the repository

```bash
git clone https://github.com/Prachipandey28/AI-Maze-Solver.git
cd AI-Maze-Solver
```

If your repository has a different URL, replace the URL above with your actual GitHub repository URL.

### 2. Install dependencies

```bash
python3 -m pip install numpy matplotlib
```

### 3. Run the project

```bash
python3 main.py
```

The program prints the algorithm results in the terminal and opens visualization windows for the maze paths.

**Tip:** Close each Matplotlib window to let the program continue to the next visualization.

---

## 📈 Sample Output

The exact results depend on the algorithm, maze, and implementation.

```text
========== BFS ==========
BFS Path: [(0, 0), (0, 1), ...]
BFS Moves: 8

========== UCS ==========
UCS Path: ['S', 'B', 'C', 'G']
UCS Total Cost: 3
```

BFS finds an eight-move path in the current maze. UCS finds a total cost of `3` in its separate weighted graph.

Execution times can vary between runs, especially for very small problems.

## 📁 Project Structure

```text
AI-Maze-Solver/
│
├── main.py
├── README.md
└── assets/
    └── maze-solver-bfs.png
```

Make sure your screenshot is stored at `assets/maze-solver-bfs.png`. GitHub uses this relative path to display the image in the README.

## 🔮 Future Enhancements

- [ ] Implement UCS directly on the grid maze.
- [ ] Show all algorithm paths side by side.
- [ ] Visualize explored and visited cells.
- [ ] Compare the number of explored nodes.
- [ ] Generate random mazes.
- [ ] Allow users to select start and goal positions.
- [ ] Add an interactive interface using Streamlit or Pygame.
- [ ] Add more screenshots for DFS, Greedy Best-First Search, and A*.
- [ ] Export algorithm performance comparisons.

## 🎓 Learning Outcomes

This project provides practical experience with:

- State-space representation
- Initial states and goal states
- Successor generation
- Queues, stacks, and priority queues
- Visited-state tracking
- Path reconstruction
- Heuristic functions
- Cost-based search
- Search algorithm visualization
- Basic performance evaluation

## 👩‍💻 Author

**Prachi Pandey**

- GitHub: [@Prachipandey28](https://github.com/Prachipandey28)

---

<div align="center">

### ⭐ Enjoyed this project?

Explore the code, learn how the algorithms work, and consider giving the repository a star!

**Built with Python, curiosity, and a little maze-solving magic. 🧩**

</div>
