import networkx as nx
import matplotlib.pyplot as plt

def best_first_search(graph, start, goal, heuristic):
    frontier = [(heuristic[start], start)]
    visited = set()
    parent = {}

    while frontier:
        (cost, current_node) = min(frontier)
        frontier.remove((cost, current_node))

        if current_node == goal:
            path = []
            node = current_node
            while node != start:
                path.append(node)
                node = parent[node]
            path.append(start)
            path.reverse()
            return path, cost

        visited.add(current_node)
        for neighbor in graph[current_node]:
            if neighbor not in visited:
                parent[neighbor] = current_node
                frontier.append((heuristic[neighbor], neighbor))
    return None, None


#graph
graph = {
    'A': ['B', 'C'],
    'B': ['D', 'E'],
    'C': ['F'],
    'D': [],
    'E': ['F'],
    'F': []
}

#heuristic values
heuristic = {
    'A': 7,
    'B': 6,
    'C': 3,
    'D': 5,
    'E': 2,
    'F': 1,
}

start_node = 'A'
goal_node = 'F'

path, cost = best_first_search(graph, start_node, goal_node, heuristic)

if path:
    print("BFS Graph: ", graph)
    print("BFS Heuristic: ", heuristic)
    print("Start Node:", start_node)
    print("Goal Node:", goal_node)
    print("BFS Nodes:", path)

# Visualize the graph
    G = nx.Graph()
    G.add_edges_from([(u, v) for u in graph for v in graph[u]])

    pos = nx.spring_layout(G)
    nx.draw(G, pos, with_labels=True, node_color='lightblue', node_size=500, edge_color='gray')

    path_edges = list(zip(path, path[1:]))
    nx.draw_networkx_edges(G, pos, edgelist=path_edges, edge_color='red', width=3)

    plt.title('Best-First Search')
    plt.show()

else:
    print("No path found.")