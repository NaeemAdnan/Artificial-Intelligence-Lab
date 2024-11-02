import heapq

# Graph
graph = {
    's': [('a', 1), ('g', 10)],
    'a': [('b', 2), ('c', 1)],
    'b': [('d', 5)],
    'c': [('d', 3), ('g', 4)],
    'd': [('g', 2)],
    'g': []
}

# Heuristic
heuristic = {
    's': 5,
    'a': 3,
    'b': 4,
    'c': 2,
    'd': 6,
    'g': 0
}

def a_star(start, goal):
    open_set = []
    heapq.heappush(open_set, (heuristic[start], start))
    g_cost = {start: 0}
    parent = {start: None}
    f_values = {start: heuristic[start]} 

    while open_set:
        _, current = heapq.heappop(open_set)

        if current == goal:
            path = []
            f_sum = 0
            while current:
                path.append(current)
                f_sum += f_values[current] 
                current = parent[current]
            path.reverse()
            return path, f_sum

        for neighbor, cost in graph[current]:
            tentative_g_cost = g_cost[current] + cost

            if neighbor not in g_cost or tentative_g_cost < g_cost[neighbor]:
                g_cost[neighbor] = tentative_g_cost
                f_cost = tentative_g_cost + heuristic[neighbor]
                f_values[neighbor] = f_cost
                heapq.heappush(open_set, (f_cost, neighbor))
                parent[neighbor] = current

    return None, float('inf')

path, f_sum = a_star('s', 'g')
print("Path:", path)
print(f"The optimal path's total f(n) (cost + heuristic estimate) is: {f_sum}")