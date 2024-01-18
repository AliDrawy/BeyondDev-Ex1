from collections import deque

def reach_target(n, m, grid, start, target, k):
    # Create a set to keep track of visited cells
    visited = set()
    # Initialize a queue for BFS with the starting position and moves count
    queue = deque([(start[0], start[1], 0)])  # (x, y, moves)

    while queue:
        # Dequeue the current position and moves count
        x, y, moves = queue.popleft()
        # Check if the target is reached within the allowed moves
        if (x, y) == target and moves <= k:
            return True

        # Skip already visited cells or cells with obstacles
        if (x, y) in visited or grid[x][y] == 1 or moves > k:
            continue

        # Mark the current cell as visited
        visited.add((x, y))
        # Define the four possible directions (up, down, left, right)
        directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]
        # Explore neighbors in all four directions
        for dx, dy in directions:
            nx, ny = x + dx, y + dy
            # Check if the neighbor is within the grid boundaries
            if 0 <= nx < n and 0 <= ny < m:
                # Enqueue the neighbor with updated moves count
                queue.append((nx, ny, moves + 1))

    # If the target is not reached return False
    return False



if __name__ == '__main__':
    # Example usage:
    n = 3
    m = 3
    grid = [[0, 0, 0], [1, 1, 0], [0, 0, 0]]
    start = (0, 0)
    target = (2, 2)
    k = 6
    result = reach_target(n, m, grid, start, target, k)
    print("Output:", result)
