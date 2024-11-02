import collections as cl

def bfs_goal(graph, start_node, goal_node):
  visited = set()
  queue = cl.deque([(start_node, [start_node])])
  visited.add(start_node)

  while queue:
    current_node, path = queue.popleft()

    if current_node == goal_node:
      return path  # Goal found, return the path

    for neighbor in graph.get(current_node, []):
      if neighbor not in visited:
        visited.add(neighbor)
        queue.append((neighbor, path + [neighbor]))

  return None  # Goal not found


# Example graph
graph = {
    'A': ['B', 'C'],
    'B': ['D', 'E'],
    'C': ['F'],
    'D': [],
    'E': ['F'],
    'F': []
}

start_node = 'A'
goal_node = 'F'

path = bfs_goal(graph, start_node, goal_node)

if path:
  print(f"Path from {start_node} to {goal_node}: {path}")
else:
  print(f"No path found from {start_node} to {goal_node}")